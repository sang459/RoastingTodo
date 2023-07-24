import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import yaml
import os

with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

authenticator2 = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
RAPID_API_KEY = os.environ['RAPID_API_KEY']
# OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
# RAPID_API_KEY = st.secrets['RAPID_API_KEY']

st.session_state['username'] = ''
st.session_state['username'] = None
st.session_state['authentication_status'] = None
st.session_state['username'] = None



def main():
    st.title("채찍봇 SPICY")
    st.write("우리의 친구 SPICY가 당신의 하루를 응원(?)해줍니다.")
    st.write("피드백 (리이잉크)")

    # 로그인 페이지 (authorization)
    name, authentication_status, username = authenticator2.login('Login', 'main')
    st.session_state['username'] = username

    
    if authentication_status:
        st.session_state['logout_object'] = authenticator2.logout('Logout', 'main')
        first_time = config['credentials']['usernames'][username]['first_time']
        with open('config.yaml', 'w', encoding='utf-8') as file:
            config['credentials']['usernames'][username]['first_time'] = False
            yaml.dump(config, file, default_flow_style=False, allow_unicode=True, encoding='utf-8')
        
        switch_page('set_goal' if first_time else 'check')

    elif authentication_status == False:
        st.error('아이디 혹은 비밀번호가 틀렸습니다.')
    elif authentication_status == None:
        st.warning('아이디와 비밀번호를 입력해 주세요.')
    


if __name__ == "__main__":
    main()
