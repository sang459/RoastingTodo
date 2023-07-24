# 로딩 페이지 (loading)

import streamlit as st
import openai
import yaml
import requests
from streamlit_extras.switch_page_button import switch_page

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
RAPID_API_KEY = st.secrets['RAPID_API_KEY']

username = st.session_state['username']

with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


#def translate(text):
#    url = "https://deepl-translator.p.rapidapi.com/translate"
#    headers = {
#        "content-type": "application/json",
#        "X-RapidAPI-Key": RAPID_API_KEY,
#        "X-RapidAPI-Host": "deepl-translator.p.rapidapi.com"
#    }
#    payload = {
#        "text": text,
#        "source": "EN",
#        "target": "KO"
#    }
#
#    try:
#        response = requests.post(url, json=payload, headers=headers)
#        return response.json()['text']
#    
#    except Exception as e:
#        print(f"An error occurred during translation: {e}")

def feedback(goal, succeeded: bool):
    st.session_state['goal'] = goal
    st.session_state['check'] = "Succeeded" if succeeded else "Failed"
    
    intensity = "slighty" if succeeded else "BRUTALLY"
    prompt = f"""Instruction: You are an AI that {intensity} roasts the user. But you don't really "mean it": You just want the user to be better. Answer in English. Keep it less than 300 words.\n\nSituation: The user's goal was "{goal}", and they checked "{succeeded}." """
    chat_history = [{"role": "system", "content": prompt}]

    eng_response = openai.ChatCompletion.create(
                    model= "gpt-4",
                    messages=chat_history,
                    stream=False,
                    temperature=0.9
                    )
    
    eng_message = eng_response['choices'][0]['message']['content']
    
    print(eng_message)

    return eng_message


st.write('축하해요! 목표를 멋지게 완수하셨네요. 당신이라면 해낼 줄 알았어요!' if st.session_state['success'] == True else '목표를 달성하지 못했어도 괜찮아요. 내일은 내일의 해가 뜨니까요!')
if st.session_state['success'] == True:
    st.balloons()

image_placeholder = st.empty()
image_placeholder.image('sources/breakdance.gif')
"그런데 잠깐...SPICY가 할 말이 있는 것 같네요..."

robots_response = feedback(st.session_state['goal'], st.session_state['success'])
st.session_state['feedback'] = robots_response
# translated_response = translate(robots_response)
# st.session_state['translated_response'] = translated_response

with open('config.yaml', 'w', encoding='utf-8') as file:
    config['credentials']['usernames'][username]['feedback'] = robots_response
    # config['credentials']['usernames'][username]['feedback'] = translated_response
    yaml.dump(config, file, default_flow_style=False, allow_unicode=True, encoding='utf-8')

switch_page('feedback')