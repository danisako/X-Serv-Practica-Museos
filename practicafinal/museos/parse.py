from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string

class ContentHandler(ContentHandler):
	def __init__(self):

		self.dataType = 'contenido'
		

		self.inContent = True
		self.theContent = ""

		self.inSection = False
		self.atrSection = ''

		self.Lista_Museos = {}
		self.Museos = []
		
	def startElement(self,tag,attrs):

		if tag == "atributo" and attrs["nombre"] in ['PK','NOMBRE', 'DESCRIPCION-ENTIDAD','HORARIO','EQUIPAMIENTO','TRANSPORTE','DESCRIPCION', 'ACCESIBILIDAD','CONTENT-URL', 'NOMBRE-VIA', 'CLASE-VIAL', 'TIPO-NUM','NUM','PLANTA','ORIENTACION','LOCALIDAD','PROVINCIA','CODIGO-POSTAL','BARRIO', 'DISTRITO','COORDENADA-X','COORDENADA-Y','LATITUD','LONGITUD','TELEFONO']:
			self.atrSection = attrs['nombre']
			self.inSection = 1

	def endElement(self, tag):
		if tag == 'atributo' and self.atrSection in ['PK','NOMBRE', 'DESCRIPCION-ENTIDAD','HORARIO','EQUIPAMIENTO','TRANSPORTE','DESCRIPCION', 'ACCESIBILIDAD','CONTENT-URL', 'NOMBRE-VIA', 'CLASE-VIAL', 'TIPO-NUM','NUM','PLANTA','ORIENTACION','LOCALIDAD','PROVINCIA','CODIGO-POSTAL','BARRIO', 'DISTRITO','COORDENADA-X','COORDENADA-Y','LATITUD','LONGITUD','TELEFONO']:
			self.Lista_Museos[self.atrSection] = self.theContent
			self.atrSection = ""
		if tag == "atributo" and self.atrSection == 'LOCALIZACION' and self.atrSection in ['PK','NOMBRE', 'DESCRIPCION-ENTIDAD','HORARIO','EQUIPAMIENTO','TRANSPORTE','DESCRIPCION', 'ACCESIBILIDAD','CONTENT-URL', 'NOMBRE-VIA', 'CLASE-VIAL', 'TIPO-NUM','NUM','PLANTA','ORIENTACION','LOCALIDAD','PROVINCIA','CODIGO-POSTAL','BARRIO', 'DISTRITO','COORDENADA-X','COORDENADA-Y','LATITUD','LONGITUD','TELEFONO']:
			self.Lista_Museos[self.atrSection] = self.theContent
		if tag == self.dataType:
			self.Museos.append(self.Lista_Museos)
			self.Lista_Museos = {}
		if self.inSection:
			self.inSection = 0
			self.AtrSection = ""
			self.theContent = ""

	def characters(self, chars):
		if self.inSection:
			self.theContent = self.theContent + chars

	def terminar (self):
		return (self.museos)

def ParsearMuseos():

	theParser = make_parser()
	theHandler = ContentHandler()
	theParser.setContentHandler(theHandler)

	theParser.parse("https://datos.madrid.es/egob/catalogo/201132-0-museos.xml")
	Museos = theHandler.Museos
	return Museos
