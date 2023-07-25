import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(initial_sidebar_state="expanded")

st.text('버그 제보 : https://open.kakao.com/o/sr6Mcjxf')

st.markdown("""
            <style>
            .css-vk3wp9.eczjsme11 {
                display: none
            }

            .css-10zg0a4.eczjsme1 {
                display: none
            }
            </style>
            """, unsafe_allow_html=True)

st.balloons()

'💪'
'목표가 설정되었습니다. 저녁에 다시 만나요!'

if st.button('홈으로'):
    switch_page('main')