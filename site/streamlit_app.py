import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
empresa = st.selectbox("Empresa", ["PETR4", "VALE3", "MGLU3", "ABEV3"])
volume = st.number_input("Quantidade de ações", min_value=1, step=1)

precos = {
    "PETR4": 34.70,
    "VALE3": 67.20,
    "MGLU3": 3.80,
    "ABEV3": 15.45
}

if st.button("Calcular"):
    total = volume * precos[empresa]
    st.write(f"💰 Valor estimado: **R$ {total:,.2f}**")