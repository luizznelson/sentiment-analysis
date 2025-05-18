import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")
st.title("🔎 Análise de Sentimento em Reviews de Serviços")

# Carrega os dados já analisados
df = pd.read_csv("data/reviews_sentimentos.csv")

# Sidebar para filtro
servico_sel = st.sidebar.multiselect(
    "Filtrar por serviço", options=df["servico"].unique(),
    default=list(df["servico"].unique())
)
sentimento_sel = st.sidebar.multiselect(
    "Filtrar por sentimento", options=df["sentimento"].unique(),
    default=list(df["sentimento"].unique())
)
df_filtro = df[
    (df["servico"].isin(servico_sel)) &
    (df["sentimento"].isin(sentimento_sel))
]

# Cards de contagem
col1, col2, col3 = st.columns(3)
col1.metric("Total de Reviews", len(df_filtro))
col2.metric("Positivos", (df_filtro["sentimento"] == "Positivo").sum())
col3.metric("Negativos", (df_filtro["sentimento"] == "Negativo").sum())

# Gráfico 1: Distribuição dos sentimentos
st.subheader("Distribuição dos Sentimentos")
fig, ax = plt.subplots()
sns.countplot(x="sentimento", data=df_filtro, palette="RdYlGn", ax=ax)
st.pyplot(fig)

# Gráfico 2: Sentimento por serviço
st.subheader("Sentimento por Serviço")
fig2, ax2 = plt.subplots(figsize=(10,4))
sns.countplot(x="servico", hue="sentimento", data=df_filtro, palette="RdYlGn", ax=ax2)
st.pyplot(fig2)

# Tabela: Exemplo de reviews recentes
st.subheader("Exemplos de Reviews")
st.dataframe(df_filtro[['cliente', 'servico', 'review', 'sentimento']].sample(10))

# Review aleatório destacado
st.info(df_filtro.sample(1)['review'].values[0])
