# --- Importar a biblioteca --- #
from io import StringIO
from typing import Dict


def contagem_nt(tipo: str, entrada: object) -> Dict[str, int]:
    """
    Função responsável por realizar a contegem de nucleotídeos.
    :param tipo: Tipo da entrada ('Manual' ou 'FASTA')
    :param entrada: Sequência de DNA.
    :return: Dicionário com a contagem de cada nucleotídeo.
    """
    # --- Se a opção escolhida for "Manual" --- #
    if tipo == 'Manual':
        # --- Contar a quantidade de cada nucleotídeo --- #
        adenina = entrada.count('A')
        timina = entrada.count('T')
        guanina = entrada.count('G')
        citosina = entrada.count('C')

        # --- Criar o dicionário para armazenar as informações --- #
        dic = {
            'A': adenina,
            'T': timina,
            'G': guanina,
            'C': citosina
        }

        return dic

    # --- Se a opção escolhida for "FASTA" --- #
    elif tipo == 'FASTA':
        # --- Carregar o arquivo --- #
        fasta_carregado = entrada.getvalue()

        # --- Converter de bytes para letras --- #
        fasta_io = StringIO(fasta_carregado.decode())

        # --- Obter somente a sequência --- #
        fasta = fasta_io.read().split('\n')
        sequencia = ''.join(fasta[1:])

        # --- Contar a quantidade de cada nucleotídeo --- #
        adenina = sequencia.count('A')
        timina = sequencia.count('T')
        guanina = sequencia.count('G')
        citosina = sequencia.count('C')

        # --- Criar o dicionário para armazenar as informações --- #
        dic = {
            'A': adenina,
            'T': timina,
            'G': guanina,
            'C': citosina
        }

        return dic
