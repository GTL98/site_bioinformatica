# --- Importar as bibliotecas --- #
import streamlit as st
from io import StringIO
from contagem_aa import contagem_aa

# --- Configuração da página --- #
st.set_page_config(page_title='Contador de aminoácidos')

# --- Colocar o título na página --- #
st.title('Contador de aminoácidos')
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
    entrada = st.text_area(label='Coloque a sequência de aminoácidos abaixo:').upper()

    # --- Colocar o botão para fazer a análise --- #
    analise = st.button('Análise')
    if analise:
        # --- Realizar a contagem dos nucleotídeos --- #
        dic_aa = contagem_aa(escolha, entrada)

        # --- Criar as colunas --- #
        col_1, col_2 = st.columns(2)

        # --- Colocar a informação de modo escrito --- #
        with col_1:
            st.subheader(f'- Glicina (G): {dic_aa["G"]}')
            st.subheader(f'- Alanina (A): {dic_aa["A"]}')
            st.subheader(f'- Leucina (L): {dic_aa["L"]}')
            st.subheader(f'- Valina (V): {dic_aa["V"]}')
            st.subheader(f'- Isoleuceina (I): {dic_aa["I"]}')
            st.subheader(f'- Prolina (P): {dic_aa["P"]}')
            st.subheader(f'- Fenilalanina (F): {dic_aa["F"]}')
            st.subheader(f'- Serina (S): {dic_aa["S"]}')
            st.subheader(f'- Treonina (T): {dic_aa["T"]}')
            st.subheader(f'- Cisteina (C): {dic_aa["C"]}')
            st.subheader(f'- Tirosina (Y): {dic_aa["Y"]}')
            st.subheader(f'- Asparagina (N): {dic_aa["N"]}')
            st.subheader(f'- Glutamina (Q): {dic_aa["Q"]}')
            st.subheader(f'- Aspartato (D): {dic_aa["D"]}')
            st.subheader(f'- Glutamato (E): {dic_aa["E"]}')
            st.subheader(f'- Arginina (R): {dic_aa["R"]}')
            st.subheader(f'- Lisina (K): {dic_aa["K"]}')
            st.subheader(f'- Histidina (H): {dic_aa["H"]}')
            st.subheader(f'- Triptofano (W): {dic_aa["W"]}')
            st.subheader(f'- Metionina (M): {dic_aa["M"]}')

        with col_2:
            # --- Colocar o gráfico no site --- #
            grafico = st.bar_chart(data=dic_aa)

elif escolha == 'FASTA':
    # --- Criar a caixa de upload do arquivo FASTA --- #
    upload = st.file_uploader('Escolha um arquivo FASTA:')

    # --- Colocar o botão para fazer a análise --- #
    analise = st.button('Análise')
    if analise:
        # --- Realizar a contagem dos nucleotídeos --- #
        dic_aa = contagem_aa(escolha, upload)

        # --- Criar as colunas --- #
        col_1, col_2 = st.columns(2)

        # --- Colocar a informação de modo escrito --- #
        with col_1:
            st.subheader(f'- Glicina (G): {dic_aa["G"]}')
            st.subheader(f'- Alanina (A): {dic_aa["A"]}')
            st.subheader(f'- Leucina (L): {dic_aa["L"]}')
            st.subheader(f'- Valina (V): {dic_aa["V"]}')
            st.subheader(f'- Isoleuceina (I): {dic_aa["I"]}')
            st.subheader(f'- Prolina (P): {dic_aa["P"]}')
            st.subheader(f'- Fenilalanina (F): {dic_aa["F"]}')
            st.subheader(f'- Serina (S): {dic_aa["S"]}')
            st.subheader(f'- Treonina (T): {dic_aa["T"]}')
            st.subheader(f'- Cisteina (C): {dic_aa["C"]}')
            st.subheader(f'- Tirosina (Y): {dic_aa["Y"]}')
            st.subheader(f'- Asparagina (N): {dic_aa["N"]}')
            st.subheader(f'- Glutamina (Q): {dic_aa["Q"]}')
            st.subheader(f'- Aspartato (D): {dic_aa["D"]}')
            st.subheader(f'- Glutamato (E): {dic_aa["E"]}')
            st.subheader(f'- Arginina (R): {dic_aa["R"]}')
            st.subheader(f'- Lisina (K): {dic_aa["K"]}')
            st.subheader(f'- Histidina (H): {dic_aa["H"]}')
            st.subheader(f'- Triptofano (W): {dic_aa["W"]}')
            st.subheader(f'- Metionina (M): {dic_aa["M"]}')

        with col_2:
            # --- Colocar o gráfico no site --- #
            grafico = st.bar_chart(data=dic_aa)
