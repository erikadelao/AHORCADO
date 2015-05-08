#Okol & Developingo
import mono
import random
'''
lista_palabras = {
    'cpu': 'Unidad central de procesamiento',
    'sqli':'Es un error que te permite ejecutar consultas a la base de datos',
    'php':'lenguaje de programacion para crear webs dinamicas',
    'ruby on rails':'framework web de ruby',
    'perl':'papa de PHP',
    'django':'framework web de python',
    'print':'funcion para imprimir en pantalla en casi cualquier lenguaje de scripting'
    
}
'''

def elegirLinea():
    afile = open("palabras.txt")
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline.strip("\n")
    return line

print ("""Vamos a jugar
ahorcado!!
Listo?
""")

input('Enter para comenzar!')


palabra = elegirLinea()
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

