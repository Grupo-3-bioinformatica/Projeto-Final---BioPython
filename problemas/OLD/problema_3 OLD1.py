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
# Função para verificar a mutação
def verificar_mutacao(sequencia, posicao, nucleotideo_original, nucleotideo_mutado):
    # Verifica se a posição é válida para a sequência
    if posicao < len(sequencia):
        return sequencia[posicao] == nucleotideo_original
    return False

# Funcao para gerar e imprimir o relatorio
def gerar_relatorio(arquivo_fasta, posicao, nucleotideo_original, nucleotideo_mutado):
    organismos = ler_fasta(caminho_do_arquivo)
    resultados = []

    for organismo in organismos:
        possui_mutacao = verificar_mutacao(organismo.sequencia, posicao, nucleotideo_original, nucleotideo_mutado)
        resultados.append({
            "id": organismo.id,
            "nome": organismo.nome,
            "possui_mutacao": possui_mutacao
        })

    return resultados

# Funcao para salvar relatorio
def salvar_relatorio(resultados, caminho_relatorio):
    with open(caminho_relatorio, 'w') as file:
        for resultado in resultados:
            mutacao_status = "Presente" if resultado["possui_mutacao"] else "Não Presente"
            file.write(f'ID: {resultado["id"]}\n')
            file.write(f'Nome: {resultado["nome"]}\n')
            file.write(f'Mutação na posição 1000: {mutacao_status}\n')
            file.write('---\n')



# Variaveis
arquivo_fasta = './arquivos/Flaviviridae-genomes.fasta'
arquivo_mutacoes = './arquivos/relatorio_mutacoes.txt'
posicao_mutacao = 1000 - 1  # Índice 1000 na sequência (começando de 0)
nucleotideo_original = 'A'
nucleotideo_mutado = 'G'

# Gerar o relatório de mutações
resultado_relatorio = gerar_relatorio(arquivo_fasta, posicao_mutacao, nucleotideo_original, nucleotideo_mutado)
salvar_relatorio(resultado_relatorio, arquivo_mutacoes)

# Imprimir o relatório
print(f'Relatório gerado em: {arquivo_mutacoes}')