import streamlit as st
import textos

power_bi_url_parte1 = "https://app.powerbi.com/view?r=eyJrIjoiZTZlNmFhMWMtY2I4Zi00ZmRhLTllMTItMzk2ZGI2Y2IzM2EzIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"
power_bi_url_parte2 = "https://app.powerbi.com/view?r=eyJrIjoiMDVjNWQwM2EtZDljOS00NjJmLTkzODktYjc0NDhhZjIzODUyIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"
power_bi_url_parte3 = "https://app.powerbi.com/view?r=eyJrIjoiMmZiYjcxMGEtNmNjOC00ODU2LWEwNGMtMTRiMmUyNjhmOThkIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"

st.set_page_config(layout='wide')

st.title('DATATHON: Impacto da ONG Passos Mágicos')


st.header('Introdução 🌍')
st.markdown(textos.texto_introducao, unsafe_allow_html=True)
st.image('images/image2.webp', use_container_width=True)
st.header('Dashboard e Insights 📊')
st.markdown(textos.texto_analise_parte1_introdutorio, unsafe_allow_html=True)
st.markdown(
f"<div style='display: flex; justify-content: center;'><iframe src='{power_bi_url_parte1}' width='2000' height='1000' frameborder='0' allowFullScreen='true'></iframe></div>",
unsafe_allow_html=True)
st.markdown(textos.texto_analise_parte1, unsafe_allow_html=True)
st.markdown(
f"<div style='display: flex; justify-content: center;'><iframe src='{power_bi_url_parte2}' width='2000' height='1000' frameborder='0' allowFullScreen='true'></iframe></div>",
unsafe_allow_html=True)
st.markdown(textos.texto_analise_parte2, unsafe_allow_html=True)
st.header('Conclusão 📝')
st.markdown(textos.texto_conclusao, unsafe_allow_html=True)
st.header('Referências')
st.markdown(textos.texto_final, unsafe_allow_html=True)