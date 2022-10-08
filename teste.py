# if elif else while
lista = [1,2,3,4,5]
for i in lista:
    print (i)

print ("\n")

for i in range(5,10,2):
    print (i)
print ("\n")

nome1 = "Pedro"
nome2 = "Noelita"
soma = nome1 + " " + nome2 + "\n"
print (len(soma))
print (nome1[0:3])
print (soma[4:9])
print (soma.upper())
print (soma.strip())
print (soma.split("o"))
print (soma.find("Noe"))
print (soma[soma.find("Noe"):])
soma = soma.replace("Noelita", "Victor")
print (soma)
def mult():
    x = int(input("Insira numero: "))
    y = int(input("Insira numero 2: "))
    return x*y
print (mult())