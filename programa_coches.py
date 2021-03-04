#PROGRAMA PRINCIPAL

from codigo_coches import *

print("--------")
print("- MENU -")
print("--------")
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
        for marca,modelo,matricula in zip(listar_coches_vendidos(doc)[0],listar_coches_vendidos(doc)[1],listar_coches_vendidos(doc)[2]):
            print(marca," ",modelo," ",matricula)
    #Buscar o filtrar información: Pedir por teclado una matricula y mostrar información del coche.
    elif opcion == 3:
        #Mostrar todas las matriculas:
        lista_matriculas = ['0754GHE','0401ASD','0401JDW','0252JDW','4580DMX','7568LCD']
        print("MATRICULAS: ")
        for elem in lista_matriculas:
            print(elem)
        print("INFORMACIÓN DEL COCHE SEGUN SU MATRICULA: ")
        print("------------------------------------------")
        matricula = input("Matricula: ")
        for info in info_coche(doc,matricula):
            print(info)
    #Buscar información relacionada: Pedir por teclado el nombre de un accesorio y mostrar la marca y el modelo.
    elif opcion == 4:
        #Mostrar nombre de todos los accesorios:
        lista_accesorios = ['Radio','Climatizador','Bluetooth','Ventana Techo','Camara Trasera']
        print("ACCESORIOS: ")
        for elem in lista_accesorios:
            print(elem)
        print("MARCA Y MODELO SEGUN NOMBRE DE UN ACCESORIO: ")
        print("---------------------------------------------")
        nombre_accesorio = input("Nombre Accesorio: ")
        for marca,modelo in info_coche_relacionada(doc,nombre_accesorio):
            print(marca,"--",modelo)
    #Ejercicio Libre: Pedir por teclado un modelo y mostrar sus accesorios.
    elif opcion == 5:
        #Mostrar Modelos de los coches:
        lista_modelos = ['Fiesta','Tucson','Leon','208','Clio','Kona','325d Berlina','Clase C','xc60']
        print("MODELOS: ")
        for elem in lista_modelos:
            print(elem)
        print("ACCESORIOS SEGUN MODELO DE COCHE: ")
        print("----------------------------------")
        nombre_modelo = input("Modelo Coche: ")
        for accesorio in accesorios_coche(doc,nombre_modelo):
            print(accesorio)
    print("--------")
    print("- MENU -")
    print("--------")
    print(menu)
    opcion = int(input("Opción: "))
    while opcion <1 or opcion >6:
        print("Opcion Incorrecta")
        opcion = int(input("Opción: "))
