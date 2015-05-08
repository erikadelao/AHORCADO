lista= []
    for palabra2 in linea. split ():
        palabra3=[]
        for palabra2 in linea.split():
            palabra3.append(palabra2.strip("áéióúñ"))
        print(" ".join(palabra3))
