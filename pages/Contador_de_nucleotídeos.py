# --- Importar as bibliotecas --- #
import streamlit as st
from contagem_nt import contagem_nt

# --- Configuração da página --- #
st.set_page_config(page_title='Contador de nucleotídeos')

# --- Colocar o título na página --- #
st.title('Contador de nucleotídeos')
st.write('---')

# --- Escolher entre colar a sequência ou upar o arquivo FASTA --- #
escolha = st.radio(
    label='Escolha uma opção:',
    options=(
        'Manual',
        'FASTA'
    ),
    horizontal=True,
    index=None
)

# --- Escolha de colocar a sequência de modo manual --- #
if escolha == 'Manual':
    # --- Criar o campo de entrada de texto --- #
    entrada = st.text_area(label='Coloque a sequência de DNA abaixo:').upper()

    # --- Colocar o botão para fazer a análise --- #
    analise = st.button('Análise')
    if analise:
        # --- Realizar a contagem dos nucleotídeos --- #
        dic_nt = contagem_nt(escolha, entrada)

        # --- Criar as colunas --- #
        col_1, col_2 = st.columns((1, 2))

        # --- Colocar a informação de modo escrito --- #
        with col_1:
            st.subheader(f'- Adenina (A): {dic_nt["A"]}')
            st.subheader(f'- Timina (T): {dic_nt["T"]}')
            st.subheader(f'- Guanina (G): {dic_nt["G"]}')
            st.subheader(f'- Citosina (C): {dic_nt["C"]}')

        with col_2:
            # --- Colocar o gráfico no site --- #
            grafico = st.bar_chart(data=dic_nt)

elif escolha == 'FASTA':
    # --- Criar a caixa de upload do arquivo FASTA --- #
    upload = st.file_uploader('Escolha um arquivo FASTA:')

    # --- Colocar o botão para fazer a análise --- #
    analise = st.button('Análise')
    if analise:
        # --- Realizar a contagem dos nucleotídeos --- #
        dic_nt = contagem_nt(escolha, upload)

        # --- Criar as colunas --- #
        col_1, col_2 = st.columns((1, 2))

        # --- Colocar a informação de modo escrito --- #
        with col_1:
            st.subheader(f'- Adenina (A): {dic_nt["A"]}')
            st.subheader(f'- Timina (T): {dic_nt["T"]}')
            st.subheader(f'- Guanina (G): {dic_nt["G"]}')
            st.subheader(f'- Citosina (C): {dic_nt["C"]}')

        with col_2:
            # --- Colocar o gráfico no site --- #
            grafico = st.bar_chart(data=dic_nt)
