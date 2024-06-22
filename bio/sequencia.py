from constantes import DNA_PARA_AMINOACIDO, DNA_STOP_CODONS

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
        conversor = {
            "A": "T",
            "T": "A",
            "G": "C",
            "C": "G"
        }
        return conversor[base]

    def complement(self):
        sequencia_complementar = ""
        for base in self.sequencia:
            sequencia_complementar += self.conversor_sequencial(base)
        return sequencia_complementar
    
    def reverso_complemento(self):
        sequencia_complementar=self.complement()
        sequencia_reversa=sequencia_complementar[::-1]
        return sequencia_reversa
    
    def transcrever(self):
       sequencia_transcrita = ""
       for base in self.sequencia:
            if base=='T':
                sequencia_transcrita += 'U'
            else: 
                sequencia_transcrita += base
       return sequencia_transcrita
    
    def traduzir(self):
        sequencia_traduzida = ""
        ponto_inicio = "ATG"
        proteina = ""
        index_inicio = self.sequencia.find(ponto_inicio)

        if index_inicio != -1:
            proteina = self.sequencia[index_inicio:]
            for i in range(0, len(proteina), 3):
                codon = proteina[i:i+3]
                sequencia_traduzida += DNA_PARA_AMINOACIDO[codon]
                if DNA_STOP_CODONS.find(codon):
                    break
                