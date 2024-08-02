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
from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia

# Funcao de traducao das sequencias em proteinas
def traduzir_sequencias_em_proteinas(caminho_do_arquivo):
    # Ler o arquivo FASTA e obter as sequências
    organismos = ler_fasta(caminho_do_arquivo)
    
    for organismo in organismos:
        # Cria um objeto Sequencia para cada sequência de nucleotídeos
        sequencia_obj = Sequencia(organismo.sequencia)
        # Traduz a sequência de nucleotídeos em uma sequência de proteínas
        sequencia_proteina = sequencia_obj.traduzir()
        # Imprime a sequência de proteínas
        print(f'ID: {organismo.id}')
        print(f'Nome: {organismo.nome}')
        print(f'Sequencia de Proteinas: {sequencia_proteina}\n')
        print('------------------------------------------------------\n')

# Execucao:
arquivo_fasta = './arquivos/Flaviviridae-genomes.fasta'
traduzir_sequencias_em_proteinas(arquivo_fasta)
