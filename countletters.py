
def contarpalabras(palabras):
    diccionario_palabras = {}
    palabras = palabras.split()
    for palab in palabras:
        if palab in diccionario_palabras:
            diccionario_palabras[palab]=diccionario_palabras[palab]+1
        else:
            diccionario_palabras[palab]=1
    return diccionario_palabras

