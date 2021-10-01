
def diagonalprincipal(lista):
    diagonal=[]
    for i in range (len(lista)): 
        diagonal.append(lista[i][i])
    return(diagonal)

def main():
    lista=[]
    #cantidad de filas
    fila=int(input(''))
    #cantidad de columnas
    columna=int(input(''))

    if fila == columna : 
        for i in range (fila): 
            lista.append([])
            for j in range (columna):
                x=int(input())
                lista[i].append(x)
        resultado=diagonalprincipal(lista)
        print(resultado)
    else:
        print('La matriz no es cuadrada')

   

if __name__=='__main__':
    main()
