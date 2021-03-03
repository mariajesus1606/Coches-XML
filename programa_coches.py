#PROGRAMA PRINCIPAL

from codigo_coches import *

menu = '''1. Listar información
2. Contar información
3. Buscar o filtrar información
4. Buscar información relacionada
5. Ejercicio libre
6. Salir'''

print(menu)

opcion = int(input("Opción: "))
while opcion <1 or opcion >6:
    print("Opcion Incorrecta")
    opcion = int(input("Opción: "))

while opcion != 6:
    #Listar información: Listar nombre y modelo de todos los coches.
    if opcion == 1:
        print("NOMBRE Y MODELO DE TODOS LOS COCHES: ")
        print("-------------------------------------")
        for marca,modelo in nombre_modelo(doc):
            print(marca," ",modelo)
    #Contar información: Contar cuantos coches se han vendido y listar esos coches vendidos.
    elif opcion == 2:
        print("NUMERO DE COCHES VENDIDOS: ")
        print("---------------------------")
        print("El numero de coches vendidos es de: ",contar_coches_vendidos(doc)," coches")
        #for coches in listar_coches_vendidos(doc):
        #    print(coches)
        print("LISTA COCHES VENDIDOS: ")
        print("-----------------------")
    #Buscar o filtrar información: Pedir por teclado una matricula y mostrar información del coche.
    elif opcion == 3:
        matricula = input("Matricula: ")
        for info in info_coche(doc,matricula):
            print(info)
    #Buscar información relacionada: Pedir por teclado el nombre de un accesorio y mostrar la marca y el modelo.
    elif opcion == 4:
        nombre_accesorio = input("Nombre Accesorio: ")
        for marca,modelo in info_coche_relacionada(doc,nombre_accesorio):
            print(marca,"--",modelo)
    #Ejercicio Libre: Pedir por teclado un modelo y mostrar sus accesorios.
    #elif opcion == 5:
    #    nombre_modelo = input("Modelo Coche: ")
    #    lista_accesorios = accesorios_coche(nombre_modelo)
    #    if nombre_modelo in lista_accesorios:
    #        for lista in lista_accesorios:
    #            for accesorio in lista:
    #                print(accesorio) 
    print("--------")
    print("- MENU -")
    print("--------")
    print(menu)
    opcion = int(input("Opción: "))
    while opcion <1 or opcion >6:
        print("Opcion Incorrecta")
        opcion = int(input("Opción: "))
