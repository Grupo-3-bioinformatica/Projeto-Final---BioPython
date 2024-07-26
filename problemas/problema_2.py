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

# Importando funcoes:
from bio.sequencia import Sequencia,traduzir_sequencias
from bio.ler_fasta import ler_fasta,ler_multifasta

# Imprimir as sequências de proteínas
def imprimir_sequencias_proteinas(sequencias_proteinas):
    for id, seq in sequencias_proteinas.items():
        print(f'>{id}\n{seq}')

# Execucao:
nome_arquivo = './arquivos/Flaviviridae-genomes.fasta'
sequencias = ler_multifasta(nome_arquivo)
sequencias_proteinas = traduzir_sequencias(sequencias)

imprimir_sequencias_proteinas(sequencias_proteinas)
