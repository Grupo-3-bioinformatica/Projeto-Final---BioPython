'''
## Problema 2: Tradução de Sequências de Nucleotídeos para Sequências de Proteínas

Objetivo: Traduzir sequências de nucleotídeos para sequências de proteínas.

Tarefa: Escreva um script em Python para:

1) Fazer o parse do arquivo multiFASTA.
2) Traduzir cada sequência de nucleotídeos para sua sequência de proteína correspondente.
3) Imprimir as sequências de proteínas.  

Dica: Use sua classe Sequencia e sua função de traduzir
'''

import sys
import os

# Adicionando o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bio.sequencia import Sequencia

# Problema_2:
# Fazer o parse do arquivo multiFASTA.
def ler_multifasta(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        sequencias = {}
        sequencia_atual = ''
        id_atual = None
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith('>'):
                if id_atual is not None:
                    sequencias[id_atual] = sequencia_atual
                id_atual = linha[1:]
                sequencia_atual = ''
            else:
                sequencia_atual += linha
        if id_atual is not None:
            sequencias[id_atual] = sequencia_atual
    return sequencias

# Traduzir cada sequência de nucleotídeos para sua sequência de proteína correspondente.
def traduzir_sequencias(sequencias):
    sequencias_proteinas = {}
    for id, seq in sequencias.items():
        sequencia_obj = Sequencia(seq)
        sequencia_proteina = sequencia_obj.traduzir()
        sequencias_proteinas[id] = sequencia_proteina
    return sequencias_proteinas

# Imprimir as sequências de proteínas.
def imprimir_sequencias_proteinas(sequencias_proteinas):
    for id, seq in sequencias_proteinas.items():
        print(f'>{id}\n{seq}')

# Execucao:
nome_arquivo = './arquivos/Flaviviridae-genomes.fasta'
sequencias = ler_multifasta(nome_arquivo)
sequencias_proteinas = traduzir_sequencias(sequencias)

imprimir_sequencias_proteinas(sequencias_proteinas)
