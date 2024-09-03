import os
os.system('cls')

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

def escolher_opcao():
    operacao = 1
    while operacao != 0:
        print("+ Adicao")
        print("- Subtracao")
        print("/ Divisao")
        print("* Multiplicacao")
        print("0 Sair")

        operacao = input("Digite a Operacao Desejada : ")
    
        if operacao == "0":
            os.system('cls')
            break

        if operacao != "+" and operacao != "-" and operacao != "/" and operacao != "*" and operacao!= "0":
            print("Opcao Invalida !!")
            input()
            os.system('cls')
        else:
            valor1 = float(input("Digite o Valor 1 : "))
            valor2 = float(input("Digite o Valor 2 : "))
        
            if operacao == "+":
                soma(valor1, valor2)
            elif operacao == "-":
                subtracao(valor1, valor2)
            elif operacao == "/":
                if valor2 != 0:
                    divisao(valor1, valor2)
                else:
                    resultado = 0
            else:
                multiplicacao(valor1, valor2)

            input()
            os.system('cls')            

def soma(valor1, valor2):
    resultado = valor1 + valor2
    mostrar = f"O resultado e : {resultado:.2f}"
    print(mostrar)
    return

def subtracao(valor1, valor2):
    resultado = valor1 - valor2
    mostrar = f"O resultado e : {resultado:.2f}"
    print(mostrar)
    return 

def divisao(valor1, valor2):
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        resultado = int(0)
    mostrar = f"O resultado e : {resultado:.2f}"
    print(mostrar)
    return 

def multiplicacao(valor1, valor2):
    resultado = valor1 * valor2
    mostrar = f"O resultado e : {resultado:.2f}"
    print(mostrar)
    return 

escolher_opcao()