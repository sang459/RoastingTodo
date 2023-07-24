# 목표 설정 페이지 (set_goal)

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page

username = st.session_state['username']

with open('config.yaml', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']

# user의 page 정보 갱신 및 저장
with open('config.yaml', 'w') as file:
    config['credentials']['usernames'][username]['page'] = 'set_goal'
    yaml.safe_dump(config, file, default_flow_style=False, allow_unicode=True)


# 이거 챗봇으로 바꾸기
goal = st.text_input('내일의 목표를 정할 시간입니다!') 
st.session_state['goal'] = goal

if st.button('다음'):
    # 유저의 goal 정보 할당
    # config['credentials']['usernames'][username]['first_time'] = False
    config['credentials']['usernames'][username]['goal'] = goal
    # 유저 정보 저장
    with open('config.yaml', 'w') as file:
        yaml.safe_dump(config, file, default_flow_style=False, allow_unicode=True)
    
    st.toast('목표가 설정되었습니다. 저녁에 다시 만나요!', icon='🔥')

    switch_page("check")
    