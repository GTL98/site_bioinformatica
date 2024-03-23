# --- Importar as bibliotecas --- #
from Bio.Seq import Seq
from io import StringIO
from typing import Tuple


def traducao(tipo: str, entrada: str) -> Tuple[str, str, str]:
    """
    Função responsável por traduzir os nucleotídeos.
    :param tipo: Tipo da análise ('Manual' ou 'FASTA').
    :param entrada: Sequência de DNA.
    :return: Tupla com os 3 frames de leitura.
    """
    # --- Se a escolha for "Manual" --- #
    if tipo == 'Manual':
        # --- Tratar a sequência --- #
        entrada = entrada.replace('\n', '')

        # --- Transformar a sequência de entrada em um objeto Seq --- #
        sequencia = Seq(entrada)

        # --- Criar os frames de leitura --- #
        seq_1 = sequencia[0:]
        seq_2 = sequencia[1:]
        seq_3 = sequencia[2:]

        # --- Traduzir os frames de leitura --- #
        t_1 = seq_1.translate(stop_symbol='^')
        t_2 = seq_2.translate(stop_symbol='^')
        t_3 = seq_3.translate(stop_symbol='^')

        return str(t_1), str(t_2), str(t_3)

    # --- Se a escolha for "FASTA" --- #
    if tipo == 'FASTA':
        # --- Carregar o arquivo --- #
        fasta_caregado = entrada.getvalue()

        # --- Converter de bytes para letras --- #
        fasta_io = StringIO(fasta_caregado.decode())

        # --- Obter somente a sequência --- #
        fasta = fasta_io.read().split('\n')
        sequencia = ''.join(fasta[1:])

        # --- Transformar a sequência de entrada em um objeto Seq --- #
        sequencia = Seq(sequencia)

        # --- Criar os frames de leitura --- #
        seq_1 = sequencia[0:]
        seq_2 = sequencia[1:]
        seq_3 = sequencia[2:]

        # --- Traduzir os frames de leitura --- #
        t_1 = seq_1.translate(stop_symbol='^')
        t_2 = seq_2.translate(stop_symbol='^')
        t_3 = seq_3.translate(stop_symbol='^')

        return str(t_1), str(t_2), str(t_3)
