
import streamlit as st
import pandas as pd

# Função para processar os dados da planilha
def processar_planilha(uploaded_file):
    # Ler os dados da planilha
    df = pd.read_excel(uploaded_file)
    
    # Agrupar por categoria e somar os valores
    df_agrupado = df.groupby('CATEGORIA').agg({'ORÇAMENTO': 'sum', 'REALIZADO': 'sum', 'COMPROMETIDO': 'sum'}).reset_index()
    
    # Calcular a diferença entre orçamento e realizado
    df_agrupado['DIFERENÇA'] = df_agrupado['ORÇAMENTO'] - df_agrupado['REALIZADO']
    
    return df_agrupado

# Cabeçalho do app
st.title("Relatório de Dados da Planilha")

# Upload da planilha
uploaded_file = st.file_uploader("Faça o upload da sua planilha Excel", type=["xlsx"])

# Se o arquivo foi carregado, processar os dados
if uploaded_file is not None:
    st.write("Processando os dados...")
    # Processar e mostrar o relatório
    df_agrupado = processar_planilha(uploaded_file)
    
    # Mostrar o DataFrame no app
    st.dataframe(df_agrupado)
    
    # Permitir ao usuário baixar o relatório gerado
    st.download_button(
        label="Baixar Relatório",
        data=df_agrupado.to_excel(index=False),
        file_name="relatorio_formatado.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
