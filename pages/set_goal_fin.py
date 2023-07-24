import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.balloons()

'💪'
'목표가 설정되었습니다. 저녁에 다시 만나요!'

if st.button('홈으로'):
    switch_page('main')