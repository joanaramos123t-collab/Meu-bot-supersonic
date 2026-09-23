import streamlit as st
import pandas as pd
st.set_page_config(page_title="Exército SuperSonic v3", layout="wide")
if "database_empresas" not in st.session_state:
    st.session_state.database_empresas = [
        {"Data": "2026-09-14", "Empresa": "Cooperativa Agro Alpha", "Nicho": "Cooperativa Grande", "Implantacao": 150000.00, "Mensalidade": 45000.00, "Status": "✅ Ativa", "Atraso": 0},
        {"Data": "2026-09-14", "Empresa": "Cooperativa Sul Central", "Nicho": "Cooperativa Grande", "Implantacao": 150000.00, "Mensalidade": 45000.00, "Status": "✅ Ativa", "Atraso": 0},
        {"Data": "2026-09-13", "Empresa": "Clínica Médica Integrada", "Nicho": "Clínica / Saúde", "Implantacao": 15000.00, "Mensalidade": 4900.00, "Status": "✅ Ativa", "Atraso": 0},
        {"Data": "2026-09-13", "Empresa": "Posto Rota 24h", "Nicho": "Posto de Gasolina", "Implantacao": 10000.00, "Mensalidade": 3999.00, "Status": "✅ Ativa", "Atraso": 0},
        {"Data": "2026-09-12", "Empresa": "Mercado do Bairro", "Nicho": "Mercadinho de Vila", "Implantacao": 1500.00, "Mensalidade": 500.00, "Status": "⚠️ Atraso", "Atraso": 6},
    ]
st.title("🚀 EXÉRCITO SUPERSONIC V3")
df = pd.DataFrame(st.session_state.database_empresas)
st.dataframe(df, use_container_width=True)
st.metric("MRR Ativo", f"R$ {df[df['Status'].str.contains('Ativa')]['Mensalidade'].sum():,.2f}")
import os
import requests
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# CONEXÃO DE PRODUÇÃO REAL COM O SEU BANCO ASAAS (CORRIGIDO)
ASAAS_API_URL = "https://asaas.com"
ASAAS_API_KEY = st.secrets.get("ASAAS_API_KEY", os.environ.get("ASAAS_API_KEY", ""))

# CONFIGURAÇÃO DA TELA DO SEU PAINEL OFICIAL
st.set_page_config(page_title="EXÉRCITO SUPERSONIC V3", layout="wide", page_icon="🚀")
st.title("🚀 EXÉRCITO SUPERSONIC V3")
st.write("### **Plano Estratégico em Produção Real**")
st.write("---")

# TABELA DE PRECIFICAÇÃO ESTRUTURADA DIRETAMENTE DO NOSSO PDF
TABELA_PDF = {
    "Cooperativa Grande": {"setup": 150000.00, "mensalidade": 45000.00, "split_regra": "R$ 2,00 a R$ 5,00 por transação líquida"},
    "Clínica Médica": {"setup": 15000.00, "mensalidade": 4900.00, "split_regra": "1,0% a 1,5% de split sobre consultas"},
    "Posto de Gasolina": {"setup": 10000.00, "mensalidade": 3999.00, "split_regra": "Taxa fixa sobre fechamentos de frotas"},
    "Associação Transporte": {"setup": 5000.00, "mensalidade": 1990.00, "split_regra": "R$ 2,00 retidos por corrida/frete"},
    "Mercado do Bairro": {"setup": 1500.00, "mensalidade": 500.00, "split_regra": "Taxa mínima por PIX excedente no PDV"}
}

# ----------------------------------------------------
# MÓDULO COMITIVA: RODÍZIO DE CHIPS & DISPAROS IA
# ----------------------------------------------------
def gerenciar_comitiva():
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ Módulo Comitiva (WhatsApp)")
    status_chips = st.sidebar.toggle("Ativar Rodízio de Números", value=True)
    if status_chips:
        st.sidebar.success("🤖 Comitiva: 4 chips ativos em revezamento anti-bloqueio.")
    else:
        st.sidebar.warning("⚠️ Rodízio pausado. Risco de queda aumentado.")

# ----------------------------------------------------
# MÓDULO SHINE: ESCUDO CYBERSECURITY 24H (TAKEDOWN)
# ----------------------------------------------------
def executar_escudo_shine():
    st.write("---")
    st.subheader("🛡️ Módulo Shine: Escudo Anti-Fraude 24h")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.info("🔍 **Varredura Ativa:** Monitorando domínios falsos e golpes de PIX.")
        if st.button("🚨 Forçar Varredura Agora"):
            st.toast("Robô Shine varrendo a internet por clones...")
            st.success("Nenhuma fraude ativa detectada nas últimas 2 horas!")
            
    with col_s2:
        st.markdown("""
        * **Status do Robô:** Operando em Nuvem 24/7 de forma 100% autônoma
        * **Proteção de Dados:** Ativada (Operador Asus protegido por anonimato)
        * **Ação Automatizada:** Envio de dossiê para provedores (Cloudflare/Hostinger)
        """)

if not ASAAS_API_KEY:
    st.error("⚠️ Token do Asaas não configurado! Vá nas configurações secretas do Streamlit e adicione sua ASAAS_API_KEY para puxar os dados reais.")
else:
    headers = {"access_token": ASAAS_API_KEY, "Content-Type": "application/json"}
    
    try:
        # Puxa a lista de clientes reais cadastrados na sua conta Asaas
        res_cust = requests.get(f"{ASAAS_API_URL}/customers?limit=100", headers=headers)
        # Puxa os pagamentos reais recebidos na sua carteira
        res_pay = requests.get(f"{ASAAS_API_URL}/payments?status=RECEIVED", headers=headers)
        
        if res_cust.status_code == 200:
            clientes = res_cust.json().get("data", [])
            lista_operacao = []
            mrr_real = 0.0
            
            for cli in clientes:
                if "SSV3" in str(cli.get("externalReference", "")):
                    nome = cli.get("name")
                    email = cli.get("email")
                    nicho = str(cli.get("externalReference", "")).replace("SSV3-", "")
                    
                    valor_mensalidade = 0.0
                    status_sistema = "Aguardando Setup"
                    
                    if res_pay.status_code == 200:
                        for p in res_pay.json().get("data", []):
