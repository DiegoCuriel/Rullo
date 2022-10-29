"""
Hecho por 
Diego Curiel    A01640372
Alexia Paz      A01635557
"""

from os import system, name
import random

#-------------------------------------------------------------------APARTADO VARIABLES GLOBALES
#gráficos en forma 
instrucciones = ['\033[1;37;40m{:^120}'.format("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"),
                 '{:^120}'.format("%      __o                               o__       %"),
                 '{:^120}'.format("%   _ \<_                                _>/ _     %"),
                 '{:^120}'.format("%  (_)/(_)         INSTRUCCIONES        (_)\(_)    %"),
                 '{:^120}'.format("% ^^^^^^^^^                            ^^^^^^^^^^  %"),
                 '{:^120}'.format("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"),
                 '{:^120}'.format('Para jugar a rullo deberás primero escoger el modo de juego, modo adición o multiplicación.'),
                 '{:^120}'.format('Después deberás seleccionar el tamaño del tablero, este tamaño varía de 5x5 hasta 8x8.'),
                 '{:^120}'.format('Rullo consiste en sumar o multiplicar los valores de manera horizontal o vertical unos con otros'),
                 '{:^120}'.format('para alcanzar el número que se te muestra a los extremos de cada fila o columna.\n'),
                 '{:^120}'.format('Tu tablero inicia con todas las casillas activadas y tienes que desactivar algunas'),
                 '{:^120}'.format('para poder alcanzar el número que se indica al final de cada fila o columna.'),
                 '{:^120}'.format('Las casillas activadas estarán indicadas con verde y las desactivadas con rojo.'),
                 '{:^120}'.format('Activas y desactivas casillas usando letras para las columnas (a-h) y números para las filas (1-8).'),
                 '{:^120}'.format('Un ejemplo de cómo se vería una fila es:\n'),
                 '\n\t\t\t\033[1;34;40m 10\t\t\033[1;32;40m|  6  |  2  |  3  |  6  |  5  |\033[1;34;40m\t\t10\n\n',
                 '\033[1;37;40m{:^120}'.format('En esta fila tienes que alcanzar una suma de 10, para lograrlo, tienes que desactivar ambos 6.'),
                 '{:^120}'.format('Para ello tendrías que insertar las coordenadas a1 y d1 que corresponden a la columna y fila en la que se encuentran.\n'),
                 '\n\t\t\t\033[1;34;40m 10\t\t\033[1;32;40m|  \033[1;31;40m6\033[1;32;40m  |  2  |  3  |  \033[1;31;40m6\033[1;32;40m  |  5  |\033[1;34;40m\t\t10\n\n',
                 '\033[1;37;40m{:^120}'.format('Ganas en Rullo cuando todas las filas y columnas suman/multiplican al número del exterior simultáneamente.'),
                 '{:^120}'.format('Pero también puedes hacer ragequit ingresando "salir" en cualquier momento del juego.'),
                 '\033[1;33;40m{:^120}'.format('Presione enter para regresar al menu principal.')
                
                ]
menu_1 =        ['\033[1;37;40m{:^120}'.format("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"),
                 '{:^120}'.format("%      __o                               o__       %"),
                 '{:^120}'.format("%   _ \<_                                _>/ _     %"),
                 '{:^120}'.format("%  (_)/(_)             RULLO            (_)\(_)    %"),
                 '{:^120}'.format("% ^^^^^^^^^                            ^^^^^^^^^^  %"),
                 '{:^120}'.format("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"),
                 '\033[1;36;40m{:^120}'.format("Seleccione alguna de las siguientes opciones"),
                 '{:^120}'.format("Escribiendo el número de la opción en la consola\n"),
                 '\033[1;32;40m{:^120}'.format('Seleccione el modo de juego:'),
                 '{:^120}'.format('1. Modo suma +'),
                 '{:^120}'.format('2. Modo multiplicación x'),
                 '{:^120}'.format('3. Instrucciones'),
                 '{:^120}'.format('Cualquier otro número. Salir')
                ]
menu_2_1 =      ['\033[1;37;40m{:^120}'.format("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"),
                 '{:^120}'.format("%      __o                               o__       %"),
                 '{:^120}'.format("%   _ \<_                                _>/ _     %"),
                 '{:^120}'.format("%  (_)/(_)             RULLO            (_)\(_)    %"),
                 '{:^120}'.format("% ^^^^^^^^^                            ^^^^^^^^^^  %"),
                 '{:^120}'.format("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"),
                 '\033[1;36;40m{:^120}'.format("Seleccione alguna de las siguientes opciones"),
                 '{:^120}'.format("Escribiendo el número de la opción en la consola\n")
                ]
menu_2_2 =      ['\033[1;32;40m{:^120}'.format('Seleccione el tamaño del tablero:'),
                 '{:^120}'.format('1. 5 X 5'),
                 '{:^120}'.format('2. 6 X 6'),
                 '{:^120}'.format('3. 7 X 7'),
                 '{:^120}'.format('4. 8 X 8'),
                 '{:^120}'.format('Cualquier otro número. Regresar')
                ]
win =           ['\033[1;37;40m{:^120}'.format("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"),
                 '{:^120}'.format("%      __o                               o__       %"),
                 '{:^120}'.format("%   _ \<_                                _>/ _     %"),
                 '{:^120}'.format("%  (_)/(_)            GANASTE           (_)\(_)    %"),
                 '{:^120}'.format("% ^^^^^^^^^                            ^^^^^^^^^^  %"),
                 '{:^120}'.format("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"),
                 '\033[1;33;40m{:^120}'.format('Presione enter para regresar al menu principal.')
                ]

#-------------------------------------------------------------------APARTADO FUNCIONES
#clear, funcion que limpia la consola 
def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

#Imprime tablero
#   mat_1 es la matriz completa, mat_2 es la de usuario, lin es los resultados de forma horizontal
#   col los resultados de forma vertical, size tamaño de tablero
def format_tablero(mat_1, mat_2, lin, col, size):
    #Imprime guía superior
    alf = ['a','b','c','d','e','f','g','h']
    print("\n\n")
    print("\033[1;33;40m\t\t", end = "")
    for i in range(size):
        print(f"     {alf[i]} ", end = "")
    print("\n\n")

    #Imprime guía izquierda, tablero y resultado a la derecha
    for y in range (size):
        print(f"\033[1;33;40m\t{y+1}\t", end = "")
        print(f"\033[1;32;40m|", end = "")
        for x in range (size):
            if(mat_1[y][x] == mat_2[y][x]):
                print(f"{mat_1[y][x]: 5d} |", end = "")
            else:
                print('\033[1;31;40m', end = '')
                print(f"{mat_1[y][x]: 5d} \033[1;32;40m|", end = "")
        print(f"\033[1;34;40m\t{lin[y]}")
        print("\n")

    #Imprime resultados inferior
    print("\t\t", end = "")
    for i in col:
        print(f" {i: 5d} ", end = "")
    print("\n")

#Función que toma los inputs del usuario y prende o apaga una casilla
def inputs(tab_1,tab_2,long_tablero):
    #   Transformamos el input del usuario en lista
    xcord = input("Ingresa la cordenada: ")
    cord = list(xcord)

    if xcord == "salir":
         #El usuario pierde
        return(0)

    #Comprobamos que las cordenadas sean validas
    while not (cord[0] in "abcdefgh" and cord[-1] in "12345678") or (len(cord) != 2):
        print("Cordenada no valida")
        xcord = input("Ingresa la cordenada: ")
        cord = list(xcord)

        if xcord == "salir":
            #1 = el usuario pierde
            return(0)

    #Cambiamos las cordenadas ingresadas por valores faciles de manejar
    cord2 = cord[-1]
    cord2 = int(cord2)-1

    cord1 = cord[0]
    if cord1 == "a":
        cord1 = 0
    if cord1 == "b":
        cord1 = 1
    if cord1 == "c":
        cord1 = 2
    if cord1 == "d":
        cord1 = 3
    if cord1 == "e":
        cord1 = 4
    if cord1 == "f":
        cord1 = 5
    if cord1 == "g":
        cord1 = 6
    if cord1 == "h":
        cord1 = 7

    cord = [cord2+1,cord1+1]
    if cord[-1] <= long_tablero and cord[0] <= long_tablero:
        pass
    else:
        print("Cordenada fuera de rango")
        return(1)

    #Revisar estado de la coordenada
    #   Activar casilla
    if tab_1[cord2][cord1] == 0:
        tab_1[cord2][cord1] = tab_2[cord2][cord1]

    #   Desactivar casilla
    else:
        tab_1[cord2][cord1] = 0

    return(1)

#Tablero escondido
#   Elimina ciertos valores del tablero y los reemplaza con 0
def tablero_sin_valores(matriz, size):
    for i in range (size):
        for n in range (random.randint(0,size-1)):
            matriz[i][random.randint(0,size-1)] = 0
    return(matriz)

#Suma de valores por fila
#   Utiliza matriz con valores eliminados
def suma_filas(matriz, size):
    temp = 0
    suma = []

    for y in range (size):
        for x in range (size):
            temp += matriz[y][x]
        suma.append(temp)
        temp = 0
  
    return suma

#Suma de valores por columna
#   Utiliza matriz con valores eliminados
def suma_columna(matriz, size):
    temp = 0
    suma = []

    for x in range (size):
        for y in range (size):
            temp += matriz[y][x]
        suma.append(temp)
        temp = 0
  
    return suma

#Producto de valores por fila
#   Utiliza matriz con valores eliminados
def multi_filas(matriz, size):
    temp = 1
    mult = []

    for y in range (size):
        for x in range (size):
            if matriz[y][x] != 0:
                temp = matriz[y][x] * temp
        mult.append(temp)
        temp = 1
  
    return mult

#Producto de valores por columna
#   Utiliza matriz con valores eliminados
def multi_columna(matriz, size):
    temp = 1
    mult = []

    for x in range (size):
        for y in range (size):
            if matriz[y][x] != 0:
                temp = matriz[y][x] * temp
        mult.append(temp)
        temp = 1
  
    return mult

#Juego principal
def rullo(tamano, modo):
    
    columna = []
    fila = []
    
    #Se generan 3 tableros:
    #   1 para que el usuario vea los números activados y desactivados
    #   2 para llevar los números desactivados
    #   3 para tener el tablero con números desactivados, o el objetivo
    
    #Genera el tablero que se le muestra al usuario sin cambios
    if modo == 1:
        tablero = [[random.randint(1,9) for x in range(tamano)] for y in range(tamano)] 
    elif modo == 2:
        tablero = [[random.randint(2,9) for x in range(tamano)] for y in range(tamano)] 

    #Tablero se le hacen cambios
    tablero_usu = [[tablero[y][x] for x in range(tamano)] for y in range(tamano)]

    #Tablero con valores escondidos
    tablero_esc = [[tablero[y][x] for x in range(tamano)] for y in range(tamano)]
    tablero_esc = tablero_sin_valores(tablero_esc, tamano)

    #La suma o multiplicación de datos se hace con el tablero escondido ya que es el resultado que debe alcanzar el usuario
    #   modo = 1 suma
    #   modo = 2 multiplicación
    if (modo == 1):
        columna = suma_columna(tablero_esc, tamano)
        fila = suma_filas(tablero_esc, tamano)
    else:
        columna = multi_columna(tablero_esc, tamano)
        fila = multi_filas(tablero_esc, tamano)

    while True:
        clear()
        format_tablero(tablero, tablero_usu, fila, columna, tamano)

        #llama función de input
        #cambia el tablero y regresa si sigue jugando o no
        inpt = inputs(tablero_usu, tablero, tamano)

        if (inpt == 0):
            clear()
            print('\033[1;33;40m{:^120}'.format("\n\nGracias por jugar"))
            exit()
        
        #Gana
        if tablero_usu == tablero_esc:
            clear()
            format_tablero(tablero, tablero_usu, fila, columna, tamano)
            for i in win:   print(i)
            p_ = input()
            break

#Mini menus
def menu_a():
    while True:
        #Imprime menú
        for i in menu_1: print(i)

        while True:
            try:
                select = int(input("Selección: "))
                break
            except ValueError:
                print('Error: Porfavor escriba un número')
        
        if select > 3 or select < 1:
            #Sale del programa
            print('{:^120}'.format('¡Hasta pronto!'))
            exit()
        else:
            clear()
            for i in menu_2_1: print(i)

            #Asigna tamaño de tablero a su variable correspondiente 1 = suma, 2 = multiplicación
            if select == 1:
                print('{:^120}'.format('Modo Suma'))
                return 1
            elif select == 2:
                print('{:^120}'.format('Modo Multiplicación'))
                return 2
            else:
                #Instrucciones
                clear()
                for i in instrucciones: print(i)
                p_ = input()
                clear()

def menu_b():
    for i in menu_2_2: print(i)

    #Asigna tamaño de tablero a su variable correspondiente 
    while True:
        try:
            select = int(input("Selección: "))
            break
        except ValueError:
            print('Error: Porfavor escriba un número')
    
    if select > 4 or select < 1:
        return 0
    #Cambia modo de tablero, para input == 1 no es necesario poner if ya que 5 es por defecto
    elif select == 2:
        return 6
    elif select == 3:
        return 7
    elif select == 4:
        return 8
    else:
        return 5

#Menu principal
def menu():
    #VARIABLES MENU

    #El tamaño default del tablero
    tam = 0
    #El modo de juego default es suma (1), multiplicacion (2)
    mod = 0

    #FUNCIONES
    clear()

    #Selecciona modo y tamaño
    while mod == 0 or tam == 0:
        tam = 0
        mod = 0
        mod = menu_a()
        tam = menu_b()
        clear()

    rullo(tam, mod)

#Main
def main():
    while True:
        menu()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
main()