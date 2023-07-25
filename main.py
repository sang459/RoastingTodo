import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown('버그 제보 : https://open.kakao.com/o/sr6Mcjxf')

st.markdown("""
            <style>
            .css-vk3wp9.eczjsme11 {
                display: none
            }

            .css-10zg0a4.eczjsme1 {
                display: none
            }
            </style>
            """, unsafe_allow_html=True)

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']

try:
    with open('users.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
except Exception as e:
    print(e)
    st.download_button('debugging', data=config, file_name='users.json')

if 'page' not in st.session_state:
    st.session_state['page'] = 'main'


def main():
    st.title("채찍봇 SPICY")
    st.write("우리의 친구 SPICY가 당신의 하루를 응원(?)해줍니다.")
    st.write("피드백 (리이잉크)")

    # 로그인 페이지 (main)
    username = st.text_input('유저명을 입력하세요 👇', help='엔터를 눌러 확인')

    if username not in st.session_state:
        st.session_state['username'] = username
    else:
        st.error('존재하지 않는 유저명입니다.')

        if st.button('유저명 등록'):
            try:
                config[username] = {
                    "first_time" : True,
                    "page" : "main",
                    "goal" : "dummy",
                    "feedback" : "dummy"
                }
                st.session_state['username'] = username
            except Exception as e:
                print(e)

            try:
                with open('users.json', 'w', encoding='utf-8') as file:
                    json.dump(config, file, ensure_ascii=False)
            except Exception as e:
                print(e)
    
    if username:
        switch_page('set_goal' if config[username]['first_time'] == True else 'check')
    # 나중에 user의 page 정보 확인해서 directing해주는 코드로 바꾸기




if __name__ == "__main__":
    main()
