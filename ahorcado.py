import mono
import random

def elegirPalabra(): #Waterman's "Reservoir Algorithm"
    file = open("palabras.txt")
    line = next(file)
    for num, aline in enumerate(file):
      if random.randrange(num + 2): continue
      line = line.strip("\n\r")
    return line

#Implementar esta función con strings
def removerAcentos(lista):
        for palabra2 in linea. split ():
            palabra3=[]
            for palabra2 in linea.split():
                palabra3.append(palabra2.strip("áéióúñ"))
            return " ".join(palabra3)

print ("""Vamos a jugar
ahorcado!!
Listo?
""")

input('Enter para comenzar!')


#palabra = elegirLinea()
palabra = elegirPalabra
intentos_lista = ['_']*len(palabra)
intentos_malos = 0
primer_juego = True
 
while True:
    s = ''
    for i in intentos_lista:
        s += i+','
    print (s[:-1]) #Imprimir la lista con la palabra del usuario
    print (mono.mono[intentos_malos])
    if primer_juego:
    #            print (lista_palabras[palabra])
                primer_juego = False
    intento = input('Intenta: ')    
    if intento == palabra:
        print ("Felicidades!! ganaste!!")
        print ('La palabra es', palabra)
        break
    elif intento in palabra and len(intento)==1:
        for i in range(len(palabra)): #Reemplazar las letras
            if palabra[i] == intento:
                intentos_lista[i] = intento
        #Comprobar que no haya ganado
        for i in intentos_lista:
            if i == '_':
                break
        else:
            print ("Felicidades!! ganaste!!")
            print ('La palabra es', palabra)
            break
           
    else:
        intentos_malos += 1
        if intentos_malos == 6:
            print ("PERDISTE!!")
            print ('La palabra es', palabra)
            print (mono.mono[6])
            break
        print ('Ups te quedan', 6-intentos_malos, 'intentos')

print ("FIN")


#HOLA (?) :V
#Funciona :^)
