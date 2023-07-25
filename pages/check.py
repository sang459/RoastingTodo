# 목표 달성여부 체크 페이지 (check)

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
    config[username]['page'] = 'check'
    json.dump(config, file, ensure_ascii=False)

goal = config[username]['goal']
st.session_state['goal'] = goal

'오늘의 목표'
goal

success_check = st.radio('목표를 달성했나요?', ('성공', '실패'))

st.session_state['success'] = True if success_check == '성공' else False

if success_check:
    if st.button('다음'):
        switch_page('loading')