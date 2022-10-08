flag = 1
while flag!=0:
    palavra = input("Insira algo: ")
    num1 = int(input("Insira um numero: "))
    if num1>0:
        print ("o numero digitado é maior que 0")
    elif num1==0:
        print ("Igual a 0")
    else:
        print ("Menor que 0")
    while num1 > 0:
        print (num1)
        num1= num1-1
    print ("voce digitou:", palavra)
    flag = int(input("Insira 0 para encerrar o programa: "))