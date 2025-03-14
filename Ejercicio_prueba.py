import sys
def division_entre_cero():
    N1 = int(input("introduzca el primer numero a dividir: "))
    N2 = int(input("Introduzca el segundo numero a dividir: "))
    try:
        Div = N1/N2
    except ZeroDivisionError:
        return "El numero se ha dividido entre 0, vuelve a intentarlo"
        sys.exit()
    finally:
        return Div
print(division_entre_cero())
    
def indice_fuera_de_rango():
    
    