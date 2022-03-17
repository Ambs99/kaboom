
tablero = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
    ]

def mostrar_tablero(z):
    for i in range(3):
        print("|{}|{}|{}|".format(z[i][0],z[i][1],z[i][2]))

def hacer_jugada(z,simbolo,jugador):
    posicion = ''
    while not posicion.isdigit() or int(posicion) not in range(1,10):
        posicion = input("{} ingresa una posicion: ".format(jugador[simbolo]))
    x = int(posicion)-1
    i = x // 3
    j = x % 3
    if z[i][j] in "123456789":
        z[i][j] =  simbolo
    else:
        print("Esa posicion ya esta ocupada, intenta de nuevo.")
        hacer_jugada(z,simbolo,jugador)

def verificacion(z):
    """ si hemos llegado a un final, devuelve True """
    # los nueve espacios estan ocupados
    #   contador que llegue 9
    #   cuando no hay espacio libre
    # cuando hay un ganador:
    # linea con valores iguales
    if (z[0][0]!='_' and z[0][0]==z[0][1] and z[0][1]==z[0][2]) or (z[1][0]!='_' and z[1][0]==z[1][1] and z[1][1]==z[1][2]) or (z[2][0]!='_' and z[2][0]==z[2][1] and z[2][1]==z[2][2]) or (z[0][0]!='_' and z[0][0]==z[1][0] and z[1][0]==z[2][0]) or (z[0][1]!='_' and z[0][1]==z[1][1] and z[1][1]==z[2][1]) or (z[0][2]!='_' and z[0][2]==z[1][2] and z[1][2]==z[2][2]) or (z[0][0]!='_' and z[0][0]==z[1][1] and z[1][1]==z[2][2]) or (z[0][2]!='_' and z[0][2]==z[1][1] and z[1][1]==z[2][0]):
        return True
    return False




# ---main--- 
j = dict()
j['X'] = input("Nombre jugador X: ")
j['O'] = input("Nombre jugador O: ")
simbolo = 'X'
paramos = False
while not paramos:
    mostrar_tablero(tablero)
    hacer_jugada(tablero,simbolo,j)
    if simbolo=='X':
        simbolo='O'
    else:
        simbolo='X'
    paramos = verificacion(tablero)
mostrar_tablero(tablero)
if simbolo=='X':
    print("Ganó", j['O'])
else:
    print("Ganó", j['X'])

#[x] validar todas las lineas y columnas, no solo la primera columna
#[x] poner el nombre del jugador cuando sea su turno
#[ ] verificar que todo esté lleno para ver si ya terminamos
#[x] imprimir mensaje del ganador{}
#[x] verificar que la posicion solo sea del 1-9, else print message
#[ ] after a match, ask if same players are gonna play