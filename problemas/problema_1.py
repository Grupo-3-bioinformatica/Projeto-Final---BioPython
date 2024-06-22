# Problema 1: Análise de Composição de Nucleotídeos

# Tarefa: Escreva um script que:

# 1) Faça o parse do arquivo multiFASTA, usando a função ler_fasta.
# 2) Imprima o percentual de cada nucleotídeo (A, T, C, G) e o conteúdo GC (percentual de C + G) para cada sequência.

# Dica: Use sua classe Sequencia e sua função .calcular_percentual(bases)

from bio.ler_fasta import ler_fasta

organismos = ler_fasta('./arquivos/Flaviviridae-genomes.fasta')[0:1]

for organismo in organismos:
    percentual_nucleotideos = {
        "A": organismo.sequencia.calcular_percentual(bases=["A"]),
        "T": organismo.sequencia.calcular_percentual(bases=["T"]),
        "G": organismo.sequencia.calcular_percentual(bases=["G"]),
        "C": organismo.sequencia.calcular_percentual(bases=["C"]),
    }

    print(f"Percentual de cada nucleotídeo da sequencia de ${organismo.get("nome", "")}:\n")
    for percentual_nucleotideo in percentual_nucleotideos:
        print(
            f"${percentual_nucleotideo}: ${percentual_nucleotideos[percentual_nucleotideo]}")
