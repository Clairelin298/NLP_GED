from multiprocessing.sharedctypes import Value
import os
import streamlit as st
from pridectUI import predict_for_UI
st.title('GEC MASKER')

sent = st.text_input( label="input tour sentences " ) 
result = predict_for_UI(sent)
st.write(result)
#submit = form.form_submit_button("submit")
#if submit:
