from io import open
archivo_texto=open("contadorPar.txt", "a")

n1 = int(input("Ingrese el numero de incio: "))
n2 = int(input("Ingrese el numero de fin: "))

print("Ingreso los numeros: " + str(n1) + " y " + str(n2) + "\nResultado: ")
archivo_texto.write("Ingreso los numeros: " + str(n1) + " y " + str(n2) + "\nResultado: ")
while n1<=n2:
    print(n1)
    archivo_texto.write(str(n1) + ", ")
    n1= n1 + 2
archivo_texto.write("\n" + "\n")

archivo_texto.close()

