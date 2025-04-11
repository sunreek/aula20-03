import streamlit as st

st.title("🎈 💹 Ferramenta de Previsão de Ações")
st.write(
    "Simule aqui o valor estimado de fechamento de ações baseado no volume [docs.streamlit.io](https://docs.streamlit.io/)."
)
empresas = {
    "Petrobras (PETR4)": 34.70,
    "Vale (VALE3)": 67.20,
    "Magazine Luiza (MGLU3)": 3.80,
    "Ambev (ABEV3)": 15.45
}

# 👩‍💼 Seletor da empresa
empresa = st.selectbox("📊 Selecione a empresa:", list(empresas.keys()))

# 🔢 Volume de ações
volume = st.number_input("🧮 Quantidade de ações:", min_value=1, step=1)

# 📉 Cálculo da previsão
prev_fecham = st.number_input("Previsão de Fechamento:", step=0.01)


# URL da API (exemplo usando uma API pública)
url = "https://aula-2010-62jk.onrender.com/previsoes"

# Parâmetros opcionais da requisição (se necessário)
payload = {
    "empresa": empresa,
    "volume": volume,
    "prev_fecham" : prev_fecham
}

# Fazendo a requisição GET
response = requests.get(url, body=payload)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    dados = response.json()
    st.write(f"Previsão: {dados}")
else:
    st.write(f"Erro na requisição: {response.status_code}")
    st.write(response.text)
