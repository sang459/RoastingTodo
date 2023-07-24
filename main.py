import streamlit as st

import openai
import requests


OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']

def translate(text):
    url = "https://deepl-translator.p.rapidapi.com/translate"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "deepl-translator.p.rapidapi.com"
    }
    payload = {
        "text": text,
        "source": "EN",
        "target": "KO"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.json()['text']
    
    except Exception as e:
        print(f"An error occurred during translation: {e}")

def feedback(goal, succeeded: bool):
    st.session_state['goal'] = goal
    st.session_state['check'] = "Succeeded" if succeeded else "Failed"
    
    prompt = f"""Instruction: You are an AI that brutally roasts the user. But you don't really "mean it": You just want the user to be better.\n\nSituation: The user's goal was "{goal}", and they checked "{succeeded}." """
    chat_history = [{"role": "system", "content": prompt}]

    response = openai.ChatCompletion.create(
                    model= "gpt-4",
                    messages=chat_history,
                    stream=False
                    )
    
    return response['choices'][0]['delta']['content']


def main():
    st.title("채찍봇 SPICY")
    st.write("우리의 친구 SPICY가 당신의 하루를 응원(?)해줍니다.")
    st.write("피드백 (리이잉크)")

    # 1. 로그인 페이지 (authorization)
    if st.session_state['page'] == 'authorization':
        
        # (로그인 기능 넣기)

        first_time = "유저 정보로부터 불러온 값"
        if st.button('다음'):
            st.session_state['page'] = 'set_goal' if first_time == True else 'check'
    
    # 2. 목표 설정 페이지 (set_goal)
    elif st.session_state['page'] == 'set_goal':
        # 이거 챗봇으로 바꾸기
        goal = st.text_input('내일의 목표를 정할 시간입니다!') 
        # goal을 서버에 저장, 다음 번 접속 때도 불러올 수 있어야 함
        if st.button('다음'):
            st.session_state['page'] = 'check'
    
    # 3. 목표 달성 체크 페이지 (check)
    elif st.session_state['page'] == 'check':
        success_check = st.checkbox('성공')
        fail_check = st.checkbox('실패')
        if success_check:
            success=True
            st.checkbox('실패', value=False)
        
        if fail_check:
            success=False
            st.checkbox('성공', value=False)

        if success_check or fail_check:
            if st.button('다음'):
                st.session_state['page'] = 'loading'

    # 4. 로딩 (loading)
    elif st.session_state['page'] == 'loading':
        st.write('축하해요! 목표를 멋지게 완수하셨네요. 당신이라면 해낼 줄 알았어요!' if success == True else '목표를 달성하지 못했어도 괜찮아요. 내일은 내일의 해가 뜨니까요!')
        if success == True:
            st.balloons()

        image_placeholder = st.empty()
        image_placeholder.image('sources/breakdance.gif')
        "그런데 잠깐...SPICY가 할 말이 있는 것 같네요..."
        robots_response = feedback(goal, success)
        st.session_state['page'] = 'feedback'

    # 5. 피드백 (feedback)
    elif st.session_state['page'] == 'feedback':
        st.image('sources/hujup.jpg')
        st.info('_SPICY says..._\n' + translate(robots_response))
        if st.button('내일 목표 설정하기'):
            st.session_state['page'] = 'set_goal'




if __name__ == "__main__":
    st.session_state['page'] = 'authorization'
    main()
