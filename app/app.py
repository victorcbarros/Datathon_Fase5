import streamlit as st



st.set_page_config(layout='wide')

st.title('DATATHON: Impacto da ONG Passos Mágicos 📚')

# Introdução
st.header("Introdução💡")
st.write(
  "A **ONG Passos Mágicos** tem desempenhado um papel fundamental na transformação da educação de crianças e jovens em situação de vulnerabilidade social. Seu compromisso vai além do ensino tradicional, proporcionando suporte acadêmico, social e emocional para garantir que cada estudante tenha oportunidades reais de crescimento e desenvolvimento."  
"Este relatório apresenta uma análise detalhada do impacto da ONG entre **2022 e 2024**, destacando os avanços no desempenho acadêmico, as diferenças entre escolas públicas e privadas, o engajamento dos alunos e os desafios ainda existentes. Através de indicadores educacionais e sociais, buscamos compreender como a ONG tem impulsionado a melhoria da educação e o que pode ser feito para potencializar ainda mais seus resultados.  "
)





# Pergunta 1
st.header("1. Como a ONG tem transformado a educação de crianças em vulnerabilidade social?✏️")
st.write(
    "A **ONG Passos Mágicos** tem uma missão poderosa: transformar vidas por meio da educação. "
    "Com foco em crianças e jovens em situação de vulnerabilidade social, a organização oferece suporte "
    "que vai além do ensino tradicional. Este relatório traz uma análise detalhada do impacto da ONG "
    "no desempenho acadêmico e no desenvolvimento social dos estudantes, com base em dados coletados "
    "entre **2022 e 2024**."
)

st.divider()

# Seção 2: Perfil dos Alunos
st.header("2. Quem são os alunos impactados pela ONG?📖")
st.write("A maioria dos alunos atendidos está na faixa etária de **5 a 17 anos**, com maior concentração aos **10 anos**.")

st.divider()

# Seção 3: Desempenho Acadêmico
st.header("3. O desempenho acadêmico tem melhorado?📈")
st.write("Evolução do Índice de Desempenho Educacional (INDE):")
st.metric("2022", "6.41")
st.metric("2023", "6.58")
st.metric("2024", "6.64")

# Sub-seção: Comparação por escola
st.subheader("3.1 Diferenças entre escolas privadas e públicas🔍")
col1, col2 = st.columns(2)
with col1:
    st.write("### Instituições Privadas")
    st.metric("2022", "6.99")
    st.metric("2023", "6.69")
    st.metric("2024", "7.48")
with col2:
    st.write("### Instituições Públicas")
    st.metric("2022", "6.33")
    st.metric("2023", "6.56")
    st.metric("2024", "6.56")

st.divider()

# Seção 4: Classificação por Pedras
st.header("4. O que significa a classificação por 'Pedras'?🤝")
st.write("A categorização dos alunos mostra avanços no aprendizado.")
st.table({
    "Categoria": ["Quartzo", "Ágata", "Ametista", "Topázio"],
    "Total de Alunos": [837, 1242, 724, 35],
    "Escolas Públicas": [784, 1100, 565, 24],
    "Escolas Privadas": [142, 159, 53, 11]
})

st.divider()

# Seção 5: Desenvolvimento Social
st.header("5. Além do aprendizado acadêmico, como está o desenvolvimento social dos alunos?🏫")
st.write("Os indicadores sociais também mostram melhorias:")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Índice de Aproveitamento Acadêmico (IAA)", "8.5", delta="+1.6")
with col2:
    st.metric("Índice de Proficiência Social (IPS)", "6.8", delta="+1.7")
with col3:
    st.metric("Índice de Progresso de Vida (IPV)", "7.3", delta="-0.7")

st.divider()

# Seção 6: Engajamento
st.header("6. Engajamento: quanto maior, melhor o desempenho?🎓")
st.write("Os alunos com maior número de atividades concluídas apresentam melhor desempenho.")
st.metric("Índice de Engajamento", "6.4", delta="-0.3")

st.divider()
st.markdown(
f"<div style='display: flex; justify-content: center;'><iframe src='{'https://app.powerbi.com/view?r=eyJrIjoiMGZlYjg3NTYtZTU2OC00MmQ1LTgwN2QtMGI2NzcxMzVkOGQ3IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9'}' width='2000' height='1000' frameborder='0' allowFullScreen='true'></iframe></div>",
unsafe_allow_html=True)

# Conclusão
st.header("7. Conclusão🌟")
st.write(
"Os dados evidenciam que a atuação da **ONG Passos Mágicos** tem gerado um impacto positivo na vida de centenas de crianças e jovens. O aumento no desempenho acadêmico e no engajamento demonstra que as estratégias pedagógicas adotadas estão no caminho certo, reduzindo desigualdades entre escolas públicas e privadas."  

"No entanto, ainda há desafios a serem superados, especialmente no desenvolvimento social dos alunos e na manutenção do engajamento a longo prazo. O crescimento da participação de alunos mais velhos e a recuperação dos índices acadêmicos em 2024 reforçam a importância de continuar investindo em metodologias inovadoras, suporte individualizado e ações que incentivem a permanência na escola."  

"Com um olhar atento para os desafios e um compromisso contínuo com a educação, a **ONG Passos Mágicos** segue transformando vidas, oferecendo novas oportunidades e construindo um futuro mais promissor para crianças e jovens em situação de vulnerabilidade social. 🚀"

"Este projeto faz parte do projeto Tech Challenge da Pós Tech Data Analytics FIAP e conta como nota da quinta fase da pós-graduação."
"O grupo que desenvolveu esse projeto é composto por:"

"Aelton Pereira de Lacerda"

"André Martins Pontes"

"Arthur do Nascimento Siqueira"

"Matheus Martins Matias Rodrigues"

"Victor Campanha Barros"


"O link do repositorio do github com todos os arquivos pode ser acessado clicando no simbolo do github no menu superior direito"
"e no link abaixo : "
"https://github.com/victorcbarros/Datathon_Fase5"    

)