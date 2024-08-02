'''
## Problema 1: Análise de Composição de Nucleotídeos

Tarefa: Escreva um script que:

1) Faça o parse do arquivo multiFASTA, usando a função ler_fasta.
2) Imprima o percentual de cada nucleotídeo (A, T, C, G) e o conteúdo GC (percentual de C + G) para cada sequência.

Dica: Use sua classe Sequencia e sua função .calcular_percentual(bases)
'''
import sys
import os

# Adicionando o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia

# Funcao para calcular percentual de nucleotideos:
def calcular_percentual_nucleotideos(sequencia):
    percentual_nucleotideos = {
        "A": sequencia.calcular_percentual(bases=["A"]),
        "T": sequencia.calcular_percentual(bases=["T"]),
        "G": sequencia.calcular_percentual(bases=["G"]),
        "C": sequencia.calcular_percentual(bases=["C"]),
    }

    # Calcular o conteudo GC (percentual de C + G)
    percentual_gc = percentual_nucleotideos["G"] + percentual_nucleotideos["C"]

    return percentual_nucleotideos, percentual_gc

# Execucao
organismos = ler_fasta('./arquivos/Flaviviridae-genomes.fasta')#[0:1]

for organismo in organismos:
    # Inclui a sequencia de onganismos na variavel
    sequencia_obj = Sequencia(organismo.sequencia)
    # Calcula o percentual de nucleotideos
    percentual_nucleotideos, percentual_gc = calcular_percentual_nucleotideos(sequencia_obj)
    # Imprime os percentuais separados por Organismo ID
    print(f'ID: {organismo.id}')
    print(f'Nome: {organismo.nome}')
    print('Percentual de cada nucleotideo:')
    for nucleotideo, percentual in percentual_nucleotideos.items():
        # Imprimir o percentual de nucleotideos
        print(f'  {nucleotideo}: {percentual * 100:.2f}%')
    # Imprime o percentual de C e G
    print(f'Conteúdo GC: {percentual_gc * 100:.2f}%')
    print('-------------------------------------\n')
