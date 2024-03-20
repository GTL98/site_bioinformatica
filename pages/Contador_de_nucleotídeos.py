# --- Importar as bibliotecas --- #
from Bio import SeqIO
import streamlit as st
from io import StringIO

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
        # --- Contar a quantidade de adeninas --- #
        adenina = entrada.count('A')

        # --- Contar a quantidade de timinas --- #
        timina = entrada.count('T')

        # --- Contar a quantidade de guaninas --- #
        guanina = entrada.count('G')

        # --- Contar a quantidade de citosinas --- #
        citosina = entrada.count('C')

        # --- Criar as colunas --- #
        col_1, col_2 = st.columns((1, 2))

        # --- Colocar a informação de modo escrito --- #
        with col_1:
            st.subheader(f'- Adenina (A): {adenina}')
            st.subheader(f'- Timina (T): {timina}')
            st.subheader(f'- Guanina (G): {guanina}')
            st.subheader(f'- Citosina (C): {citosina}')

        with col_2:
            # --- Criar um dicionário com a contagem de nucleotídeos --- #
            dic_contagem = {
                'A': adenina,
                'T': timina,
                'G': guanina,
                'C': citosina
            }
            # --- Colocar o gráfico no site --- #
            grafico = st.bar_chart(data=dic_contagem)

elif escolha == 'FASTA':
    # --- Criar a caixa de upload do arquivo FASTA --- #
    upload = st.file_uploader('Escolha um arquivo FASTA:')

    # --- Colocar o botão para fazer a análise --- #
    analise = st.button('Análise')
    if analise:
        # --- Carregar o arquivo --- #
        fasta_carregado = upload.getvalue()

        # --- Conveter de bytes para letras --- #
        fasta_io = StringIO(fasta_carregado.decode())

        # --- Obter somente a sequência --- #
        fasta = fasta_io.read().split('\n')
        sequencia = ''.join(fasta[1:])

        # --- Contar a quantidade de adeninas --- #
        adenina = sequencia.count('A')

        # --- Contar a quantidade de timinas --- #
        timina = sequencia.count('T')

        # --- Contar a quantidade de guaninas --- #
        guanina = sequencia.count('G')

        # --- Contar a quantidade de citosinas --- #
        citosina = sequencia.count('C')

        # --- Criar as colunas --- #
        col_1, col_2 = st.columns((1, 2))

        # --- Colocar a informação de modo escrito --- #
        with col_1:
            st.subheader(f'- Adenina (A): {adenina}')
            st.subheader(f'- Timina (T): {timina}')
            st.subheader(f'- Guanina (G): {guanina}')
            st.subheader(f'- Citosina (C): {citosina}')

        with col_2:
            # --- Criar um dicionário com a contagem de nucleotídeos --- #
            dic_contagem = {
                'A': adenina,
                'T': timina,
                'G': guanina,
                'C': citosina
            }
            # --- Colocar o gráfico no site --- #
            grafico = st.bar_chart(data=dic_contagem)
