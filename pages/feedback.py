# 로딩 페이지 (loading)

import streamlit as st
import yaml
import openai
from streamlit_extras.switch_page_button import switch_page
import re

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']

username = st.session_state['username']



def starts_with_hangul(text):
    hangul = re.compile('^[가-힣]')
    result = hangul.match(text)

    return result is not None

with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# 유저 정보 저장
with open('config.yaml', 'w', encoding='utf-8') as file:
    config['credentials']['usernames'][username]['page'] = 'feedback'
    yaml.dump(config, file, default_flow_style=False, allow_unicode=True, encoding='utf-8')

st.image('sources/hujup.jpg')
# st.info('_SPICY says..._\n\n' + st.session_state['feedback'])
# st.info('_SPICY says..._\n\n' + st.session_state['translated_response'])


saved_feedback = config['credentials']['usernames'][username]['feedback']
if starts_with_hangul(saved_feedback): # 유저가 번역 후 재접속했다면
    fin_res = saved_feedback
    st.info(saved_feedback)
else:
    # streaming
    fin_res = ''
    res_box = st.empty()
    report = []
    result = ''

    kor_response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [{"role": "system", "content": "당신은 전문 번역가입니다. 다음 대사를 한글로 번역하세요. 존댓말을 사용하세요. 'you'는 '당신'으로 번역하세요.: " + st.session_state['feedback']}],
        stream=True,
        temperature=0.7
        )
    
    for resp in kor_response:
        try:
            report.append(resp['choices'][0]['delta']['content'])
        except KeyError:
            report.append(' ')
        result = "".join(report)
        res_box.info('_SPICY says..._\n\n' + result)

    # chat_history.append({"role": "assistant", "content": result}) (히스토리 추가시...)
    fin_res += result
    res_box.info('_SPICY says..._\n\n' + result)

with open('config.yaml', 'w', encoding='utf-8') as file:
    config['credentials']['usernames'][username]['feedback'] = fin_res
    yaml.dump(config, file, default_flow_style=False, allow_unicode=True, encoding='utf-8')



if st.button('내일 목표 설정하러 가기'):
    switch_page('set_goal')