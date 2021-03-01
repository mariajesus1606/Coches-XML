from lxml import etree

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
  