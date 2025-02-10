import streamlit as st

st.button("boop", type="primary")

if st.button("Say goodbye"):
    st.write("Why goodbye there")
else:
    st.write("fuck")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="secondary"):
    st.write("Ciao")