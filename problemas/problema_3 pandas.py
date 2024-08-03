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
3. Gerar um relatório vi pandas que indique quais sequências possuem a mutação e quais não possuem.
'''

import sys
import os
import pandas as pd

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
    df_relatorio_mutacao = []

    for organismo in organismos:
        sequencia = organismo.sequencia
        tem_mutacao = verificar_mutacao(sequencia, posicao_mutacao, nucleotideo_original, nucleotideo_mutado)
        status_mutacao = 'Presente' if tem_mutacao else 'Ausente'
        
        df_relatorio_mutacao.append({
                                    "ID": organismo.id,
                                     "Nome": organismo.nome,
                                     "Sequencia": sequencia[:100], # Mostra os primeiros 100 nucleotideos
                                     "Total_Sequencia": len(sequencia),
                                     "Posicao_Mutacao": posicao_mutacao + 1,  # Corrige para indice 1-based
                                     "Mutacao_Original": nucleotideo_original,
                                     "Nucleotideo_Mutado": nucleotideo_mutado,
                                     "Status_Mutacao": status_mutacao,
                                    })
    
    df = pd.DataFrame(df_relatorio_mutacao)
    df.to_csv(arquivo_mutacoes, index=False)
    print(f'Relatorio de mutacoes gerado com sucesso: {arquivo_mutacoes}')

# Variaveis
arquivo_fasta = './arquivos/Flaviviridae-genomes.fasta'
arquivo_mutacoes = './arquivos/relatorio_mutacoes.csv'
posicao_mutacao = 999  # Indice 1000 na sequencia (comecando de 0) eh 999
nucleotideo_original = 'A'
nucleotideo_mutado = 'G'

# Gera o relatorio
gerar_relatorio(arquivo_fasta, posicao_mutacao, nucleotideo_original, nucleotideo_mutado)
