'''
## Problema 3: Identificação de Mutação em Genomas Virais

#### Contexto

Você está colaborando com uma equipe de virologistas que está estudando mutações específicas em 
genomas de vírus da família Flaviviridae. Eles identificaram uma mutação de interesse que ocorre 
na posição 1000 das sequências, onde o nucleotídeo 'A' é substituído por 'G'. 
Seu trabalho é identificar se essa mutação está presente nas sequências fornecidas e gerar um relatório. 
Esta análise é crucial para entender a evolução dos vírus e suas possíveis implicações na virulência e 
resistência a tratamentos.

#### Objetivo
Aprender a usar Python para procurar mutações específicas em sequências de DNA e gerar relatórios detalhados.

### Tarefa - Fazer script que:

1. Faça o parse do arquivo multiFASTA contendo os genomas virais.
2. Verifique se a mutação específica (substituição de nucleotídeo) na posição 1000 está presente em cada sequência.
3. Gerar um relatório que indique quais sequências possuem a mutação e quais não possuem.
'''

import sys
import os

# Adicionando o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importando funcoes
from bio.ler_fasta import ler_multifasta,verificar_mutacao


# Funcao para gerar e imprimir o relatorio
def gerar_relatorio(sequencias, posicao, original, mutacao):
    relatorio = {
        'com_mutacao': [],
        'sem_mutacao': []
    }
    
    for id, seq in sequencias.items():
        if verificar_mutacao(seq, posicao, original, mutacao):
            relatorio['com_mutacao'].append(id)
        else:
            relatorio['sem_mutacao'].append(id)
    
    return relatorio

# Funcao para imprimir o relatorio
def imprimir_relatorio(relatorio):
    print('\nSequências com a mutação:')
    for id in relatorio['com_mutacao']:
        print(f'- {id}')
    
    print('\nSequências sem a mutação:')
    for id in relatorio['sem_mutacao']:
        print(f'- {id}')

# Execucao
nome_arquivo = './arquivos/Flaviviridae-genomes.fasta'
posicao_mutacao = 999  # Índice 1000 na sequência (começando de 0)
nucleotideo_original = 'A'
nucleotideo_mutacao = 'G'

# Ler as sequências do arquivo multiFASTA
sequencias = ler_multifasta(nome_arquivo)

# Gerar o relatório de mutações
relatorio = gerar_relatorio(sequencias, posicao_mutacao, nucleotideo_original, nucleotideo_mutacao)

# Imprimir o relatório
imprimir_relatorio(relatorio)