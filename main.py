import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json
from functools import partial

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown('버그 제보 : https://open.kakao.com/o/sr6Mcjxf')

st.markdown("""
            <style>
            [data-testid="stSidebar"] {
                display: none
            }

            [data-testid="collapsedControl"] {
                display: none
            }
            </style>
            """, unsafe_allow_html=True)

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']


with open('users.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

if 'page' not in st.session_state:
    st.session_state['page'] = 'main'

def user_register(reg_username):
    
    with open('users.json', 'r', encoding='utf-8') as file:
        reg_config = json.load(file)

    reg_config[reg_username] = {
        "first_time" : True,
        "page" : "main",
        "goal" : "dummy",
        "feedback" : "dummy"
    }
        
    st.session_state['username'] = reg_username
    print('session state 갱신')

    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(reg_config, file, ensure_ascii=False)
    print('저장완료')

    st.experimental_rerun()

def main():
        
    with open('users.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    st.title("쓴소리봇 SPICY")
    st.write("우리의 친구 SPICY가 당신의 하루를 응원(?)해줍니다.")
    st.write("피드백 (리이잉크)")

    # 로그인 페이지 (main)
    username = st.text_input('유저명을 입력하세요 👇', help='엔터를 눌러 확인')
    login_button = st.button('로그인')

    if username not in st.session_state:
        st.session_state['username'] = username

    if st.session_state['username'] and login_button:

        if st.session_state['username'] == 'debugger00':
            with open('users.json', 'r', encoding='utf-8') as file:
                config = json.load(file)
                downloadable_data = json.dumps(config)
                st.download_button('debugging', data=downloadable_data, file_name='users.json')

        if st.session_state['username'] not in config.keys(): # 등록 안된 유저
            st.error('존재하지 않는 유저명입니다.')
            register_func = partial(user_register, st.session_state['username'])
            st.button('유저 등록', on_click=register_func)
            st.stop()


        elif st.session_state['username'] in config.keys():
            id = st.session_state['username']
            switch_page('set_goal' if config[id]['first_time'] == True else 'check')


        
        # 나중에 user의 page 정보 확인해서 directing해주는 코드로 바꾸기




if __name__ == "__main__":
    main()
