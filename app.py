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
