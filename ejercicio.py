#Identificar los errores en los siguiente bloques de código y evaluarlos con excepciones especificas para evitar errores 
# no controlados en nuestros programas. Añadem mensajes explicativos para el usuario.
#Nota: Se tienen que evaluar excepciones concretas, no hacer referencia a Exception sin más.

#1) Código a evaluar:
#numero = 7/0
#2) Código a evaluar:

#lista = [4, 7, 30, 23, 5]
#lista[10]
#3) Código a evaluar:

#paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
#paises["alemania"]
#4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además 
# explica en un mensaje al usuario la causa y/o solución:

#resultado = "2" + 10

#Codigo 1) a evaluar:
#En este primer codigo el error es que no se puede dividir por zero, intentaremos que no de error mediante el uso de excepciones.
import sys
division_por_cero = 7/0
def codigo_1():
    try:
        division_por_cero
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    finally:
        return "7/0 = 0"
        sys.exit()
print(codigo_1())


#codigo 2) a evaluar:
#en este segundo codigo el error es que el elemento 10 de dicha lista se encuentra logicamente fuera de rango.
lista = [4, 7, 30, 23, 5]
def codigo_2():
    try:
        lista[10]
    except IndexError:
        print("El elemento numero 10 de la lista esta fuera de rango")
    finally:
        return "No se encuentra el elemento"
        sys.exit()
print(codigo_2())


#codigo 3) a evaluar:
#En dicho codigo no se encuentra alemania en el diccionario de paises
paises = {"España":"Español", "EEUU":"Ingles", "Italia":"Italiano"}
def codigo_3():
    try:
        paises["alemania"]
    except KeyError:
        print("Alemania no se encuentra en el diccionario")
    finally:
        return "Busqueda finalizada"
    sys.exit()
print(codigo_3())


#codigo 4) a evaluar:



    