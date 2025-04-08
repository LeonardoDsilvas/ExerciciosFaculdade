## OBTER A SOMA  DE TRÊS VARIÁVEIS
def soma():
    variavel1= int(input("Digite o primeiro numero da soma: "))
    variavel2= int(input("Digite o segundo numero da soma: "))
    variavel3= int(input("Digite o terceiro numero da soma: "))

    print("Resultado:",variavel1 + variavel2 + variavel3,"\n")
soma()

print("Multiplicação de duas variáveis\n")
def multiplicação():
    var1 = int(input("Digite o primeiro valor: "))
    var2 = int(input("Digite o segundo valor: "))
    print ("\nTotal do valor multiplicado:",var1 * var2)
multiplicação()

print ("\nMostrar resultado da divisão de dois numeros")

def divisão():
    var1 = int(input("Digite o primeiro valor: "))
    var2 = int(input("Digite o segundo valor: "))
    print ("\nTotal do valor dividido:", var1 / var2 )
divisão()

print("\nCalcular média de um aluno, verificar a situação, aprovado S/N")

def CalcularMedia():
    nota1 = int(input("Digite o primeiro valor: "))
    nota2 = int(input("Digite o segundo valor: "))
    nota3 = int(input("Digite o terceiro valor: "))
    resultadosoma = (nota1 + nota2 + nota3)
    resultadodiv = (resultadosoma / 3)
    if resultadodiv < 6.5:
        print(resultadodiv, 'reprovado')
    else:
        print(resultadodiv, 'aprovado')
CalcularMedia()    