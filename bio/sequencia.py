from bio.constantes import DNA_PARA_AMINOACIDO, DNA_STOP_CODONS


class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return self.sequencia

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia.__getitem__(index)

    def conversor_sequencial(self, base):
        # Objeto = {'key': 'valor'}
        # conversor[base] = pegue o valor na posição 'base'
        conversor = {
            "A": "T",
            "T": "A",
            "G": "C",
            "C": "G"
        }
        return conversor[base]

    def complement(self):
        sequencia_complementar = ""
        # Chama individualmente todos os items da lista self.sequencia
        for base in self.sequencia:
            # Converte a base e soma na sequencia complementar
            sequencia_complementar += self.conversor_sequencial(base)
        return sequencia_complementar

    def reverso_complemento(self):
        # Cria a sequencia com base na função anterior
        sequencia_complementar = self.complement()
        # sequencia_complementar[::-1] pega os valores começando do index mais alto para o menor index (tras pra frente)
        sequencia_reversa = sequencia_complementar[::-1]
        return sequencia_reversa

    #Transformar DNA em RNA
    def transcrever(self):
        sequencia_transcrita = ""
        for base in self.sequencia:
            if base == 'T':
                sequencia_transcrita += 'U'
            else:
                sequencia_transcrita += base
        return sequencia_transcrita
    
    #Transformar RNA em DNA
    def transcrever_rna_para_dna(self, sequencia):
        sequencia_transcrita = ""
        for base in sequencia:
            if base == 'U':
                sequencia_transcrita += 'T'
            else:
                sequencia_transcrita += base
        return sequencia_transcrita

    def traduzir(self, parar=False):
        sequencia_traduzida = ""
        ponto_inicio = "ATG"
        proteina = ""
        # Procura um U na lista de sequencia, se houver retorna True 
        eh_rna = str(self.sequencia).find("U") != -1
        index_inicio = 0
        index_inicio = str(self.transcrever_rna_para_dna(
            self.sequencia) if eh_rna else self.sequencia).find(ponto_inicio)

        if index_inicio != -1:
            proteina = self.transcrever_rna_para_dna(
                self.sequencia[index_inicio:]) if eh_rna else self.sequencia[index_inicio:]
            #Lê os codons (de 3 em 3)
            for i in range(0, len(proteina), 3):
                codon = proteina[i:i+3]
                # Encontra o stop codon
                if str(DNA_STOP_CODONS).find(codon) != -1:
                    # Para no stop codon
                    if parar:
                        break
                    else:
                        sequencia_traduzida += "*"
                else:
                    # Pega o valor da proteina com base no codon {'codon': 'proteina'}
                    # Caso não exista, retorna 'X' por conta do .get
                    sequencia_traduzida += DNA_PARA_AMINOACIDO.get(
                        codon, "X")

        return sequencia_traduzida

    def calcular_percentual(self, bases):
        quantidade_bases = {
            "A": 0,
            "T": 0,
            "G": 0,
            "C": 0
        }
        soma = 0
        for base in bases:
            #Conto quantas vezes aparece a base dentro de self.sequencia e adiciono em sua chave
            #quantidade_base[A] = AATGCCCCC.count(A) => 2 
            quantidade_bases[base] = str(self.sequencia).count(base)
        for base in quantidade_bases:
            soma += quantidade_bases.get(base, 0)
        percentual = soma / len(self.sequencia)
        # Round para arredondar o valor em 2 casas decimais
        return round(percentual, 2)

#    # Problema_2: Traduzir cada sequência de nucleotídeos para sua sequência de proteína correspondente.
#    # Utilizado em conjunto com a funcao ler_multifasta
#    def traduzir_sequencias(self):
#        sequencias_proteinas = {}
#        for id, seq in self.items():
#            sequencia_obj = Sequencia(seq)
#            sequencia_proteina = sequencia_obj.traduzir()
#            sequencias_proteinas[id] = sequencia_proteina
#        return sequencias_proteinas
