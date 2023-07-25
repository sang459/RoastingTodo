# 목표 설정 페이지 (set_goal)

import streamlit as st
import json
from streamlit_extras.switch_page_button import switch_page

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

try:
    username = st.session_state['username']
except Exception as e:
    print(e)
    switch_page('main')

f"안녕하세요, {username}님!"

with open('users.json', 'r', encoding='utf-8') as file:
    config = json.load(file)


OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']


# user의 page 정보 갱신 및 저장
with open('users.json', 'w', encoding='utf-8') as file:
    config[username]['page'] = 'set_goal'
    json.dump(config, file, ensure_ascii=False)


# 이거 챗봇으로 바꾸기
goal = st.text_input('내일의 목표를 정할 시간입니다!') 

if 'goal' not in st.session_state:
    st.session_state['goal'] = goal

st.session_state['goal'] = goal
config[username]['goal'] = goal

if st.button('다음'):
    # 유저의 goal 정보 할당
    # config['credentials']['usernames'][username]['first_time'] = False
    config[username]['goal'] = goal
    config[username]['first_time'] = False

    # 유저 정보 저장
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False)

    switch_page("set_goal_fin")
    