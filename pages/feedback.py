# 로딩 페이지 (loading)

import streamlit as st
import yaml
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']

username = st.session_state['username']

with open('config.yaml', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)


st.image('sources/hujup.jpg')
st.info('_SPICY says..._\n' + st.session_state['translated_response'])

# 유저 정보 저장
with open('config.yaml', 'w') as file:
    config['credentials']['usernames'][username]['page'] = 'feedback'
    try:
        config['credentials']['usernames'][username]['feedback'] = st.session_state['translated_response']
        yaml.safe_dump(config, file, default_flow_style=False, allow_unicode=True)
    except Exception as e:
        print(e)

if st.button('내일 목표 설정하러 가기'):
    switch_page('set_goal')