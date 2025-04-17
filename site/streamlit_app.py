import streamlit as st

# Base simples de conhecimento (você pode expandir depois)
base_conhecimento = {
    "dub 002": {
        "cliente": "Esse erro indica falha de comunicação com o S@T. Verifique se o cabo está conectado, ou entre em contato com o suporte técnico da franquia.",
        "analista": "Erro DUB 002: Verifique conexão física com o S@T, reinicie o serviço FiscalFlow, valide o status do SATMonitor e teste comunicação."
    },
    "pdv não abre": {
        "cliente": "Verifique se o caixa foi aberto corretamente. Se for franquia, contate o responsável pela abertura. Caso contrário, tente reiniciar o sistema.",
        "analista": "Validar licenciamento, comunicação com o banco, integridade do banco local e se há erro de DLL ou FiscalFlow."
    },
    "cadastrar produto": {
        "cliente": "Se você for franquia, o cadastro de produto deve ser feito pela matriz. Caso contrário, acesse o menu Produtos > Novo Produto e preencha os dados obrigatórios.",
        "analista": "Verifique se o cliente é franquia. Se não for, oriente a acessar Cadastros > Produto > Novo. Lembre de validar a tributação antes de liberar a venda."
    }
}

# Título da página
st.title("🤖 DesenrolaBot – Seu Assistente de Suporte Degust")

# Seleção de perfil
perfil = st.radio("Você é:", ["Cliente", "Analista"])

# Entrada de texto
duvida = st.text_input("Digite sua dúvida ou palavra-chave:")

# Botão para buscar resposta
if st.button("Buscar Resposta"):
    chave = duvida.strip().lower()
    if chave in base_conhecimento:
        resposta = base_conhecimento[chave][perfil.lower()]
        st.success(resposta)
    else:
        st.warning("🤔 Não encontrei essa informação ainda. Tente uma palavra-chave diferente ou entre em contato com o suporte.")
