# 목표 달성여부 체크 페이지 (check)

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from streamlit_extras.switch_page_button import switch_page

st.session_state['logout_object']

username = st.session_state['username']

with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# user의 page 정보 갱신 및 저장
with open('config.yaml', 'w', encoding='utf-8') as file:
    config['credentials']['usernames'][username]['page'] = 'check'
    yaml.dump(config, file, default_flow_style=False, allow_unicode=True, encoding='utf-8')

'오늘의 목표'
st.session_state['goal'] = config['credentials']['usernames'][username]['goal']

success_check = st.radio('목표를 달성했나요?', ('성공', '실패'))

st.session_state['success'] = True if success_check == '성공' else False

if success_check:
    if st.button('다음'):
        switch_page('loading')