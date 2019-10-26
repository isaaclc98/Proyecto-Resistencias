
def insertaValor(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            entrada = float(entrada)
            return entrada
        except ValueError:
            print("La entrada es incorrecta")
def cadenita(cadena,num,cad):
    resultado = ""
    resultado = cadena + str(num) + cad
    return resultado

def serie(lista):
    resultado = 0
    for i in range(0,len(lista)):
        resultado += lista[i]
    return resultado
def paralelo(lista):
    resultado = 0
    for i in range(0,len(lista)):
        resultado += (1/lista[i])
    return (1/resultado)
#prueba =[1,2,3]
#print(serie(prueba))
#print(paralelo(prueba))

def main():
    print("Calculadora de incertidumbres")
    valor = int(insertaValor("Numero de mallas: "))
    resistencia = []
    for i in range(0,valor):
        numResistores = 0
        resistoresMalla = []
        print("Malla: ",i+1)
        numResistores = int(insertaValor("Cuantos resistores hay en esta malla? "))
        for j in range(0,numResistores):
            resistoresMalla.append(insertaValor(cadenita("Resistencia ",j+1,": ")))
        resistencia.append(paralelo(resistoresMalla))
        resistoresMalla.clear
    print("La resistencia es: ",serie(resistencia))
        

if __name__ == "__main__":
    main()
