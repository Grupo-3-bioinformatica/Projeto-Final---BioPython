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

# Problema 2:
# Fazer o parse do arquivo multiFASTA
def ler_multifasta(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        sequencias = {}
        sequencia_atual = ''
        id_atual = None
        for linha in arquivo:
            # .strip utilizado para remover o \n do final (quebra de linha)
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

# Problema 3:
# Fazer o parse do arquivo multiFASTA contendo os genomas virais
# Função para verificar a mutação
def verificar_mutacao(sequencia, posicao, original, mutacao):
    if len(sequencia) > posicao and sequencia[posicao] == mutacao:
        return True
    return False
