class Rotor:
    def __init__(self, desordem):
        self.letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.letras_posicao = self.letras[:]
        self.rotor1 = desordem
        self.rotor_posicao = self.rotor1[:]
        self.rotacao_rotor = 0

    def posicao(self):
        self.letras_posicao = self.letras_posicao[-1] + self.letras_posicao[:-1]
        self.rotor_posicao = self.rotor_posicao[-1] + self.rotor_posicao[:-1]
        self.rotacao_rotor += 1
        

    def criptografa(self, index, volta=False):
        if volta == False:
            letra_rotor = self.rotor_posicao[index]
            saida_index = self.letras_posicao.index(letra_rotor)
            return saida_index

        else:
            letra_normal = self.letras_posicao[index]
            saida_index = self.rotor_posicao.index(letra_normal)
            return saida_index

class Refletor:

    def reflete(self, index):
        refletor = list("ABCDEFGDIJKGMKMIEBFTCVVJAT")
        letra = refletor[index]
        refletor[index] = 0
        return refletor.index(letra)

            
