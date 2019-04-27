import math

def quitarSignos(text):
	signos = ("?", "¿", "¡", "!", ",", ".", ";", ":", "–", "“", "”", ".\n", "\n")
	texto = text.lower()
	cadena = "" 
	for palabra in texto:
		if not palabra in signos:
			cadena += palabra
	return cadena

def count(w, d):
	contador = 0
	lineas = d.readlines()
	tam = 0
	for linea in lineas:
		palabra = linea.split(' ')
		for p in palabra:	
			p = quitarSignos(p)
			if p != '':
				tam = tam + 1 
			
			if w == p:
				contador = contador + 1
	
	#print("El contador es:",contador)
	return (contador, tam)

"""	Se obtiene k y m
	k =|{d|d E {d1,...,dm}, w E d}|
	La cantidad de veces que aparece
	w en todos los documentos
	m = numero de documwentos analizados
"""


def obtenerK(w, *doc):
	documentos = []
	i = 0
	contador = 0
	for di in doc:
		documentos.append(open(di, "r"))
		cont, tam = count(w, documentos[i])
		contador = contador + cont 
		documentos[i].close()
		i = i + 1

	return (contador, len(doc))


"""	
	Se obtiene tf 
	tf = count(w, d)
		 -----------
			|d| 
"""
def tfFun(w, d, k):
	doc = open(d, "r")
	x, tam = count(w,doc)
	return x/tam


"""
	IDF = log( M / K + 1)
	donde M = |{d1, ..., dM}|
y k =|{d|d E {d1,...,dm}, w E d}|
"""
def idfFun(m, k):
	return math.log10( (m / (k + 1)) + 1 ) #Se agrega un 1 como factor correctivo

def tfidfFun():
	w = input("Ingrese la palabra a buscar = ")
	(k, m) = obtenerK(w, "d1.txt", "d2.txt", "d3.txt")
	tf = tfFun(w, "d1.txt", k)
	#print(k, m)
	idf = idfFun(m, k)
	tfidf = tf * idf 
	print("tf =", tf, "\nidf =", idf, "\ntfidf =", tfidf)
	return tfidf

tfidfFun()


