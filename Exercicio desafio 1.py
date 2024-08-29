
import os

operacao = 1
while operacao != 0:
    print("+ Adicao")
    print("- Subtracao")
    print("/ Divisao")
    print("* Multiplicacao")
    print("0 Sair")

    operacao = input("Digite a Operacao Desejada : ")
    
    if operacao == "0":
        break

    if operacao != "+" and operacao != "-" and operacao != "/" and operacao != "*" and operacao!= "0":
        print("Opcao Invalida !!")
        input()
        os.system('cls')
    else:
        
        valor1 = float(input("Digite o Valor 1 : "))
        valor2 = float(input("Digite o Valor 2 : "))

        if operacao == "+":
            resultado = valor1 + valor2
        elif operacao == "-":
            resultado = valor1 - valor2
        elif operacao == "/":
            if valor2 != 0:
                resultado = valor1 / valor2
            else:
                resultado = 0
        else:
            resultado = valor1 * valor2

        mensagem = f"O resultado e : {resultado:.2f}"
    
        print(resultado)
        input()
        os.system('cls')
        