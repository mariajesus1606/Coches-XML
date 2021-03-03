from lxml import etree
doc = etree.parse('coches.xml')

#Funcion: Listar información: Listar nombre y modelo de todos los coches.

def nombre_modelo(doc):
  nombre_coches = []
  modelo_coches = []
  nombres = doc.xpath('/coches/coche/marca/text()')
  nombre_coches = list(nombres)
  modelos = doc.xpath('/coches/coche/modelo/text()')
  modelo_coches = list(modelos)
  return zip(nombre_coches,modelo_coches)

#Funcion: Contar información: Contar cuantos coches se han vendido y listar esos coches vendidos.

def listar_coches_vendidos(doc):
  lista_marca = []
  lista_modelo = []
  lista_matricula = []
  coches_vendidos = doc.xpath('/coches/coche[vendido = True]')
  for coche_vendido in coches_vendidos:
    marca = coche_vendido.xpath("./marca/text()")
    lista_marca = list(marca)
    modelo = coche_vendido.xpath("./modelo/text()")
    lista_modelo = list(modelo)
    matricula = coche_vendido.xpath("./matricula/text()")
    lista_matricula = list(matricula)
  return zip(lista_marca,lista_modelo,lista_matricula)

def contar_coches_vendidos(doc):
  coches_vendidos_contar = doc.xpath("count(/coches/coche[vendido = 'True'])")
  return coches_vendidos_contar

#Funcion: Buscar o filtrar información: Pedir por teclado una matricula y mostrar información del coche.

def info_coche(doc,matricula):
  informacion = doc.xpath('/coches/coche[matricula = "%s"]'%matricula)
  print(informacion[0].xpath("./marca/text()"))
  print(informacion[0].xpath("./modelo/text()"))
  print(informacion[0].xpath("./combustible/text()"))
  print(informacion[0].xpath("./color/text()"))
  print(informacion[0].xpath("./num_puertas/text()"))
  print(informacion[0].xpath("./accesorio/nombre/text()"))
  return informacion

#Funcion: Buscar información relacionada: Pedir por teclado el nombre de un accesorio y mostrar la marca y el modelo.

def info_coche_relacionada(doc,nombre_accesorio):
  marca = []
  modelo = []
  marca_coche = doc.xpath('/coches/coche/accesorio[nombre = "%s"]//../../marca/text()'%nombre_accesorio)
  marca = list(marca_coche)
  modelo_coche = doc.xpath('/coches/coche/accesorio[nombre = "%s"]//../../modelo/text()'%nombre_accesorio)
  modelo = list(modelo_coche)
  return zip(marca,modelo) 

#Funcion: Ejercicio Libre: Pedir por teclado un modelo y mostrar sus accesorios.

def accesorios_coche(doc,nombre_modelo):
  accesorio_coche = doc.xpath('/coches/coche[modelo = "%s"]'%nombre_modelo)
  print(accesorio_coche[0].xpath("./accesorio/nombre/text()"))
  return accesorio_coche

  