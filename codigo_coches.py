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

def contar_coches_vendidos(doc):
  coches_vendidos = doc.xpath('/coches/coche/matricula/text()')
  cont = 0
  lista_coches_vendidos = []
  if coches_vendidos != (" "):
    cont = cont + 1
    lista_coches_vendidos = list (coches_vendidos)
   return (cont,lista_coches_vendidos)

#Funcion: Buscar o filtrar información: Pedir por teclado una matricula y mostrar información del coche.

def info_coche(doc,buscar_matricula):
  informacion = doc.xpath('/coches/coche[buscar_matricula = "%s"]'%buscar_matricula)
  return informacion 

#Funcion: Buscar información relacionada: Pedir por teclado el nombre de un accesorio y mostrar la marca y el modelo.

def info_coche_relacionada(doc,nombre_accesorio):
  marca_coche = doc.xpath('/coches/coche/accesorio[nombre = nombre_accesorio]//../../marca/text()')
  modelo_coche = doc.xpath('/coches/coche/accesorio[nombre = nombre_accesorio]//../../modelo/text()')
  return zip(marca_coche,modelo_coche) 

#Funcion: Ejercicio Libre: Pedir por teclado un modelo y mostrar sus accesorios.

def accesorios_coche(doc,nombre_modelo):
  accesorios_coche = doc.xpath('/coches/coche[modelo = nombre_modelo]/accesorio/nombre/text()')
  return accesorios_coche
  