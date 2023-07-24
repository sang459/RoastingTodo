import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json


OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']

with open('users.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

if 'page' not in st.session_state:
    st.session_state['page'] = 'main'
if 'username' not in st.session_state:
    st.session_state['username'] = ''


def main():
    st.title("채찍봇 SPICY")
    st.write("우리의 친구 SPICY가 당신의 하루를 응원(?)해줍니다.")
    st.write("피드백 (리이잉크)")

    # 로그인 페이지 (main)
    username = st.text_input('유저명을 입력하세요 👇', help='엔터를 눌러 확인')
    if username in config.keys():
        pass
    else:
        st.error('존재하지 않는 유저명입니다.')
        if st.button('유저명 등록'):
            config[username] = {
                "first_time" : True,
                "page" : "main",
                "goal" : "dummy",
                "feedback" : "dummy"
            }

    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False)
    
    st.session_state['username'] = username

    switch_page('set_goal' if config[username]['first_time'] == True else 'check')
    # 나중에 user의 page 정보 확인해서 directing해주는 코드로 바꾸기




if __name__ == "__main__":
    main()
