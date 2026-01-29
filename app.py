import streamlit as st
import os
import platform

st.title("Mini Server Info")

st.write("Sistema:", platform.system())
st.write("CPU:", os.cpu_count())
st.write("Diretório atual:", os.getcwd())

cmd = st.text_input("Comando")
if st.button("Executar"):
    output = os.popen(cmd).read()
    st.code(output)
