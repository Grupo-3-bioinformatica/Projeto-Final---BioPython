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
from bio.ler_fasta import ler_fasta

# Definicao das funcoes:
# Funcao para verifica se a mutacao ocorre na posição especificada.
def verificar_mutacao(sequencia, posicao_mutacao, nucleotideo_original, nucleotideo_mutado):
    # Verifica se a posicao eh valida
    if len(sequencia) >= posicao_mutacao:
        # Checa a mutacao na posicao dada (considerando a posicao indexada)
        return sequencia[posicao_mutacao] == nucleotideo_original and nucleotideo_mutado
    return False

# Gera um relatorio indicando se a mutação estah presente nas sequencias.
def gerar_relatorio(arquivo_fasta, posicao_mutacao, nucleotideo_original, nucleotideo_mutado):
    organismos = ler_fasta(arquivo_fasta)
    
    with open(arquivo_mutacoes, 'w') as relatorio:
        relatorio.write('\n--------------------------------------------------------')
        relatorio.write('\nRelatorio de Identificacao de Mutacoes\n')
        relatorio.write('--------------------------------------------------------\n')

        for organismo in organismos:
            sequencia = organismo.sequencia
            tem_mutacao = verificar_mutacao(sequencia, posicao_mutacao, nucleotideo_original, nucleotideo_mutado)
            status_mutacao = 'Presente' if tem_mutacao else 'Ausente'
            
            relatorio.write(f'ID: {organismo.id}\n')
            relatorio.write(f'Nome: {organismo.nome}\n')
            relatorio.write(f'Sequencia: {sequencia[:100]}... (total {len(sequencia)} nucleotideos)\n')
            relatorio.write(f'Mutacao na posicao 1000 ({nucleotideo_original} -> {nucleotideo_mutado}): {status_mutacao}\n')
            relatorio.write('--------------------------------------------------------\n')

# Variaveis
arquivo_fasta = './arquivos/Flaviviridae-genomes.fasta'
arquivo_mutacoes = './arquivos/relatorio_mutacoes.txt'
posicao_mutacao = 999  # Indice 1000 na sequencia (comecando de 0) eh 999
nucleotideo_original = 'A'
nucleotideo_mutado = 'G'

# Gera o relatorio
gerar_relatorio(arquivo_fasta, posicao_mutacao, nucleotideo_original, nucleotideo_mutado)
