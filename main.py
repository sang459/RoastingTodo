import streamlit as st
import openai
import requests
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page

import yaml
from yaml.loader import SafeLoader
with open('config.yaml', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']




def main():
    st.title("채찍봇 SPICY")
    st.write("우리의 친구 SPICY가 당신의 하루를 응원(?)해줍니다.")
    st.write("피드백 (리이잉크)")

    # 로그인 페이지 (authorization)
    if st.session_state['page'] == 'authorization':
        # Check if keys exist in session_state before accessing
        if 'name' in st.session_state and 'authentication_status' in st.session_state and 'username' in st.session_state:
            name, authentication_status, username = st.session_state['name'], st.session_state['authentication_status'], st.session_state['username']
        else:
            name, authentication_status, username = None, None, None

        if authentication_status:
            name, authentication_status, username = authenticator.login('Login', 'main')
            st.session_state['username'] = username

            if authentication_status:
                # authenticator.logout('Logout', 'main') 로그아웃 기능은 나중에......
                first_time = config['credentials']['usernames'][username]['first_time']
                
                with open('config.yaml', 'w') as file:
                    config['credentials']['usernames'][username]['first_time'] = False
                    yaml.safe_dump(config, file, default_flow_style=False, allow_unicode=True)
                
                switch_page('set_goal' if first_time else 'check')

            elif authentication_status == False:
                st.error('아이디 혹은 비밀번호가 틀렸습니다.')
            elif authentication_status == None:
                st.warning('아이디와 비밀번호를 입력해 주세요.')
        


if __name__ == "__main__":
    st.session_state['page'] = 'authorization'
    main()
