from Scripts.rotores import Rotor, Refletor
import random

embaralha = ["JGDQOXUSCAMIFRVTPNEWKBLZYH", "NTZPSFBOKMWRCJDIVLAEYUXHGQ", "JVIUBHTCDYAKEQZPOSGXNRMWFL"]



def enigma(pos_rotor, mensa):
    

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    posicao_rotor = pos_rotor

    mensagem = mensa

    posicao_rotor = [int(x) for x in posicao_rotor.split(",")]
            
    cripto = ""

    rotor1 = Rotor(embaralha[0])
    rotor2 = Rotor(embaralha[1])
    rotor3 = Rotor(embaralha[2])
    refletor = Refletor()

    if posicao_rotor[0] >= 0 and posicao_rotor[0] <= 25:
        for i in range(posicao_rotor[0]):
            rotor1.posicao()


    else: 
        print("Digite um valor válido para a posição do rotor")
        exit()

    if posicao_rotor[1] >= 0 and posicao_rotor[1] <= 25:
        for i in range(posicao_rotor[1]):
            rotor2.posicao()


    else: 
        print("Digite um valor válido para a posição do rotor")
        exit()

    if posicao_rotor[2] >= 0 and posicao_rotor[2] <= 25:
        for i in range(posicao_rotor[2]):
            rotor3.posicao()


    else: 
        print("Digite um valor válido para a posição do rotor")
        exit()


    for i in mensagem:
        if i != " " and i != "." and i != ";" and i != "!" and i != "?" and i != ",":
            rotor1.posicao()

            if rotor1.rotacao_rotor > 25:
                rotor1.rotacao_rotor = 0
                rotor2.posicao()

            if rotor2.rotacao_rotor > 25:
                rotor2.rotacao_rotor = 0
                rotor3.posicao()
            
            if rotor3.rotacao_rotor > 25:
                rotor3.rotacao_rotor = 0


            randint = random.randint(0, 1)

            index = letras.index(i.upper())
            saida1=rotor1.criptografa(index)
            saida2=rotor2.criptografa(saida1)
            saida3=rotor3.criptografa(saida2)
            refletido = refletor.reflete(saida3)
            entrada1 = rotor3.criptografa(refletido, volta=True)
            entrada2 = rotor2.criptografa(entrada1, volta=True)
            entrada3 = rotor1.criptografa(entrada2, volta=True)
            letra = letras[entrada3]

            if randint == 0:
                cripto += letra.upper()
            else:
                cripto += letra.lower()

        else:
            cripto += i

                        

    return cripto

