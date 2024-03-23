# --- Importar as bibliotecas --- #
import streamlit as st
from traducao_nt import traducao

# --- Configuração base da página --- #
st.set_page_config('Tradução de nucleotídeos')

# --- Colocar o título da página --- #
st.title('Tradução de nucleotídeos')
st.write('---')

# --- Escolher entre colar a sequência ou upar o arquivo FASTA --- #
escolha = st.radio(
    'Escolha uma opção:',
    (
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
        # --- Traduzir os nucleotídeos --- #
        resultado = traducao(escolha, entrada)

        # --- Escrever o primeiro frame de leitura --- #
        st.subheader('Primeiro frame de leitura:')
        st.write(resultado[0])
        st.write('---')

        # --- Escrever o segundo frame de leitura --- #
        st.subheader('Segundo frame de leitura:')
        st.write(resultado[1])
        st.write('---')

        # --- Escrever o terceiro frame de leitura --- #
        st.subheader('Terceiro frame de leitura:')
        st.write(resultado[2])
        st.write('---')

elif escolha == 'FASTA':
    # --- Criar a caixa de upload do arquivo FASTA --- #
    upload = st.file_uploader('Escolha um arquivo FASTA:')

    # --- Colocar o botão para fazer a análise --- #
    analise = st.button('Análise')
    if analise:
        # --- Traduzir os nucleotídeos --- #
        resultado = traducao(escolha, upload)

        # --- Escrever o primeiro frame de leitura --- #
        st.subheader('Primeiro frame de leitura:')
        st.write(resultado[0])
        st.write('---')

        # --- Escrever o segundo frame de leitura --- #
        st.subheader('Segundo frame de leitura:')
        st.write(resultado[1])
        st.write('---')

        # --- Escrever o terceiro frame de leitura --- #
        st.subheader('Terceiro frame de leitura:')
        st.write(resultado[2])
        st.write('---')
