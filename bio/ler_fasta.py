from bio.organismo_fasta import OrganismoFasta

def ler_fasta(caminho_do_arquivo):
    organismos = []

    with open(caminho_do_arquivo) as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == ">":
                id_organismo, nome = line[1:].rstrip().split("|")
                organismos.append({
                    "id": id_organismo.strip(),
                    "nome": nome.strip(),
                    "sequencia": ""
                })
            else:
                organismos[-1]["sequencia"] += line.rstrip()

    return [OrganismoFasta(
        id=organismo["id"],
        nome=organismo["nome"],
        sequencia=organismo["sequencia"],
    ) for organismo in organismos]

# # Problema 2:
# # Fazer o parse do arquivo multiFASTA
# def ler_multifasta(nome_arquivo):
#     with open(nome_arquivo, 'r') as arquivo:
#         sequencias = {}
#         sequencia_atual = ''
#         id_atual = None
#         for linha in arquivo:
#             # .strip utilizado para remover o \n do final (quebra de linha)
#             linha = linha.strip()
#             # Valida o comeco da linha
#             if linha.startswith('>'):
#                 # Se id_atual não for None, armazena a sequência atual
#                 if id_atual is not None:
#                     sequencias[id_atual] = sequencia_atual
#                 # Atualiza id_atual com a nova linha, removendo o primeiro caractere (>)
#                 id_atual = linha[1:]
#                 sequencia_atual = ''
#             # A linha é adicionada a sequencia_atual caso não comece com '>'
#             else:
#                 sequencia_atual += linha
#         # Se o id_atual ainda estiver definido, armazena a última sequência lida
#         if id_atual is not None:
#             sequencias[id_atual] = sequencia_atual
#     return sequencias
