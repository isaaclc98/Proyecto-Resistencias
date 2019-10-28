
def insertaValor(mensaje):
    """ 
    Funcion que permite la entrada por teclado de solamente numeros(enteros,flotantes,negativos)

    """
    while True:
        entrada = input(mensaje)
        try:
            entrada = float(entrada)
            return entrada
        except ValueError:
            print("La entrada es incorrecta")
def cadenita(cadena,num,cad):
    """
    Concatena 3 cadenas y las devuelve como string

    """
    resultado = ""
    resultado = cadena + str(num) + cad
    return resultado
def potencia(lista):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.

    """
    if len(lista) == 0:
        return [[]]
    r = potencia(lista[:-1])
    return r + [s + [lista[-1]] for s in r]
def combinaciones(lista, n):
    """nCr Combinatoria
    """
    return [s for s in potencia(lista) if len(s) == n]
def serie(lista):
    """
    Suma los elementos de una lista o obtiene resistencia en serie (es lo mismo XD)

    """
    resultado = 0
    for i in range(0,len(lista)):
        resultado += lista[i]
    return resultado
def paralelo(lista):
    """
    Calcula la resistencia en paralelo de una lista de resistores

    """
    resultado = 0
    for i in range(0,len(lista)):
        resultado += (1/lista[i])
    return (1/resultado)
def dividendo(lista,n):
    """
    Esta funcion debe de entregar la multiplicacion de los elementos exepto de n
    
    """
    res = 1
    for i in range(len(lista)):
        if i == n:
            pass
        res = res * lista[i]
    return res
def divisor(listaR):
    """
    Obtiene las combinaciones posibles para el uso de la formula y los suma.
    ejemplo: xy+xz+yz

    """
    combinados = combinaciones(listaR,len(listaR)-1)
    suma = 0
    for i in range(len(combinados)):
        for j in range(len(combinados[i])):
            suma += combinados[i][j]
    return suma
def tolerancia(listaR,listaTol):
    """
    En teoria calcula la tolerancia
    SIGUE SIN SER PUESTO A PRUEBA

    """
    size = len(listaR)
    wRes=0
    if size == 1:
        w = listaTol[0]*listaR[0]
        w = w*w
        return w
    for i in range(len(listaR)):
        aux = dividendo(listaR,i)/divisor(listaR)
        aux = aux * aux
        w = aux * listaTol[i]
        w = w*w
        wRes += w

def main():
    print("Calculadora de incertidumbres")
    valor = int(insertaValor("Numero de mallas: "))
    resistencia = []
    toleranciaLista = []
    for i in range(0,valor):
        numResistores = 0
        toleranciaMalla = []
        resistoresMalla = []
        print("Malla: ",i+1)
        numResistores = int(insertaValor("Cuantos resistores hay en esta malla? "))
        for j in range(0,numResistores):
            resistoresMalla.append(insertaValor(cadenita("Resistencia ",j+1,": ")))
            toleranciaMalla.append(insertaValor(cadenita("Tolerncia [%] ",j+1,": "))/100)
        resistencia.append(paralelo(resistoresMalla))
        toleranciaLista.append(tolerancia(resistoresMalla,toleranciaMalla))
        resistoresMalla.clear
        toleranciaMalla.clear
    print("La resistencia es: ",serie(resistencia)," con una tolerancia de +-: ",(serie(toleranciaLista))**0.5)
        

if __name__ == "__main__":
    main()