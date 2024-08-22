print("+ Adicao")
print("- Subtracao")
print("/ Divisao")
print("* Multiplicacao")

operacao = input("Digite a Operacao Desejada : ")

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
    
print(resultado)
