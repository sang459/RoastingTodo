# 목표 달성여부 체크 페이지 (check)

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page

username = st.session_state['username']

with open('config.yaml', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

# user의 page 정보 갱신 및 저장
with open('config.yaml', 'w') as file:
    config['credentials']['usernames'][username]['page'] = 'check'
    yaml.safe_dump(config, file, default_flow_style=False, allow_unicode=True)

'오늘의 목표'
st.session_state['goal']
'\n목표를 달성했나요?'

success_check = st.checkbox('성공')
fail_check = st.checkbox('실패')

if success_check:
    st.session_state['success'] = True
    st.checkbox('실패', value=False)

if fail_check:
    st.session_state['success'] = True
    st.checkbox('성공', value=False)

if success_check or fail_check:
    if st.button('다음'):
        switch_page('loading')