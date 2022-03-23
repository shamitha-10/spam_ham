%%writefile app.py
import streamlit as st 
import joblib
st.title("SPAM HAM CLASSIFIER")
text_model=joblib.load('spam_ham')
ip=st.text_input("enter your message:")
op=text_model.predict([ip])
if st.button("perdict"):
  st.title(op[0])
