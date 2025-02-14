import streamlit as st
import textos

power_bi_url_parte1 = "https://app.powerbi.com/view?r=eyJrIjoiMGZlYjg3NTYtZTU2OC00MmQ1LTgwN2QtMGI2NzcxMzVkOGQ3IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"


st.set_page_config(layout='wide')

st.title('DATATHON: Impacto da ONG Passos Mágicos')


st.header('Introdução 🌍')
st.markdown(textos.texto_introducao, unsafe_allow_html=True)
#st.image('images/image2.webp', use_container_width=True)
st.header('Dashboard e Insights 📊')
st.markdown(textos.texto_analise_parte1_introdutorio, unsafe_allow_html=True)
st.markdown(textos.texto_analise_parte1, unsafe_allow_html=True)
st.markdown(
f"<div style='display: flex; justify-content: center;'><iframe src='{'https://app.powerbi.com/view?r=eyJrIjoiMGZlYjg3NTYtZTU2OC00MmQ1LTgwN2QtMGI2NzcxMzVkOGQ3IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9'}' width='2000' height='1000' frameborder='0' allowFullScreen='true'></iframe></div>",
unsafe_allow_html=True)
st.markdown(textos.texto_analise_parte2, unsafe_allow_html=True)
st.header('Conclusão 📝')
st.markdown(textos.texto_conclusao, unsafe_allow_html=True)
st.header('Referências')
st.markdown(textos.texto_final, unsafe_allow_html=True)