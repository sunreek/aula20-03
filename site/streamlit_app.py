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
if st.button("🔍 Calcular previsão de fechamento"):
    preco_unitario = empresas[empresa]
    fechamento_estimado = volume * preco_unitario
    st.success(f"✅ Previsão estimada: **R$ {fechamento_estimado:,.2f}**")