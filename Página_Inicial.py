# --- Importar a biblioteca --- #
import streamlit as st

# --- Configuração base da página --- #
st.set_page_config(page_title='Página Inicial')

# --- Colocar o título na página --- #
st.title('Ferramentas de Bioinformática')
st.write('---')

# --- Colocar o menu das opções --- #
st.subheader('Abaixo estão as opções de funcionalidade do site. Para acessar qualquer uma, '
             'basta selecionar no menu lateral.', divider='grey')
st.subheader('- Contador de nucleotídeos')
st.subheader('- Contador de aminoácidos')
st.subheader('- Tradução de nucleotídeos')