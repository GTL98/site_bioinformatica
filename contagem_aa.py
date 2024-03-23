# --- Importar a biblioteca --- #
from io import StringIO
from typing import Dict


def contagem_aa(tipo: str, entrada: object) -> Dict[str, int]:
    """
    Função responsável por realizar a contegem de aminoácidos.
    :param tipo: Tipo da entrada ('Manual' ou 'FASTA')
    :param entrada: Sequência de aminoácidos.
    :return: Dicionário com a contagem de cada aminoácido.
    """
    # --- Se a opção escolhida for "Manual" --- #
    if tipo == 'Manual':
        # --- Contar a quantidade de cada aminoácido --- #
        glicina = entrada.count('G')
        alanina = entrada.count('A')
        leucina = entrada.count('L')
        valina = entrada.count('V')
        isoleucina = entrada.count('I')
        prolina = entrada.count('P')
        fenilalanina = entrada.count('F')
        serina = entrada.count('S')
        treonina = entrada.count('T')
        cisteina = entrada.count('C')
        tirosina = entrada.count('Y')
        asparagina = entrada.count('N')
        glutamina = entrada.count('Q')
        aspartato = entrada.count('D')
        glutamato = entrada.count('E')
        arginina = entrada.count('R')
        lisina = entrada.count('K')
        histidina = entrada.count('H')
        triptofano = entrada.count('W')
        metionina = entrada.count('M')

        # --- Criar o dicionário para armazenar as informações --- #
        dic = {
            'G': glicina,
            'A': alanina,
            'L': leucina,
            'V': valina,
            'I': isoleucina,
            'P': prolina,
            'F': fenilalanina,
            'S': serina,
            'T': treonina,
            'C': cisteina,
            'Y': tirosina,
            'N': asparagina,
            'Q': glutamina,
            'D': aspartato,
            'E': glutamato,
            'R': arginina,
            'K': lisina,
            'H': histidina,
            'W': triptofano,
            'M': metionina
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

        # --- Contar a quantidade de cada aminoácido --- #
        glicina = sequencia.count('G')
        alanina = sequencia.count('A')
        leucina = sequencia.count('L')
        valina = sequencia.count('V')
        isoleucina = sequencia.count('I')
        prolina = sequencia.count('P')
        fenilalanina = sequencia.count('F')
        serina = sequencia.count('S')
        treonina = sequencia.count('T')
        cisteina = sequencia.count('C')
        tirosina = sequencia.count('Y')
        asparagina = sequencia.count('N')
        glutamina = sequencia.count('Q')
        aspartato = sequencia.count('D')
        glutamato = sequencia.count('E')
        arginina = sequencia.count('R')
        lisina = sequencia.count('K')
        histidina = sequencia.count('H')
        triptofano = sequencia.count('W')
        metionina = sequencia.count('M')

        # --- Criar o dicionário para armazenar as informações --- #
        dic = {
            'G': glicina,
            'A': alanina,
            'L': leucina,
            'V': valina,
            'I': isoleucina,
            'P': prolina,
            'F': fenilalanina,
            'S': serina,
            'T': treonina,
            'C': cisteina,
            'Y': tirosina,
            'N': asparagina,
            'Q': glutamina,
            'D': aspartato,
            'E': glutamato,
            'R': arginina,
            'K': lisina,
            'H': histidina,
            'W': triptofano,
            'M': metionina
        }

        return dic
