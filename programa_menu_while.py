import time
print("{:=^40}" .format("Programa com Menu"))
print("{:-^30}" .format("-"))
numero_um = int(input("Digite o numero: "))
numero_dois = int(input("Digite outro numero: "))
print("{:-^30}" .format("-"))
while True:
    print("{:=^40}" .format(" Menu "))
    print("[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa")
    menu = int(input("Qual opçao numero: "))
    print("{:=^40}" .format(""))
    if menu == 1:
        print("Calculando...")
        time.sleep(2)
        somar = numero_um + numero_dois
        print("a soma entre {} + {} = {}" .format(numero_um, numero_dois, somar))
    elif menu == 2:
        print("Calculando...")
        time.sleep(2)
        multip = numero_um * numero_dois
        print("a multiplicacao entre {} X {} = {}" .format(numero_um, numero_dois,multip))
    elif menu == 3:
        if numero_um >= numero_dois:
            maior = numero_um
        else:
            maior = numero_dois
            print("Calculando...")
            time.sleep(2)
        print("o numero entre {} e {}, esse e maior -> {}" .format(numero_um, numero_dois, maior))
    elif menu == 4:
        numero_um = int(input("Digite o numero: "))
        numero_dois = int(input("Digite outro numero: "))
        print("{:-^30}" .format("-"))
    elif menu == 5:
        print("Encerrando...")
        time.sleep(2)
        break#encerrar o programa
    else:
        print("tente novamente")
print("fim do programa")
        
