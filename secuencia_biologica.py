import numpy as np

# Se hace una lista con los caracteres que van a tener nuestras secuencias
cadenaBiologica = ['A', 'C', 'T', 'G']

# Usandonumpy se hace una cadena
sec1 = np.random.choice(cadenaBiologica, 150)
sec2 = np.random.choice(cadenaBiologica, 30)
puntos = np.zeros(150)


def puntaje(sec_aux1, sec_aux2):
    puntuacion = 0
    j = len(sec_aux2) - 1
    print(sec_aux1)
    print(sec_aux2)
    for i in range(len(sec_aux2)):
        # print('\n' + sec_aux1[i] + ' comparado con '+ sec_aux2[j])
        if (sec_aux1[i] == sec_aux2[j]):
            puntuacion += 1
        j -= 1
    return puntuacion

def coincidencia():
    pos = 0
    for k in range(149):
        if (max(puntos) == puntos[k]):
            print('posicion: ' + str(k))
            pos = k
            break
    print('coincidencias: ' + str(max(puntos)))
    return pos

def imprimir(posicion):
    print(sec1)
    sec_aux = np.random.choice(cadenaBiologica, 150)
    i = 0
    for x in range (150):
        if (x >= posicion and x <= (posicion+30)):
            sec_aux[x] = sec2[i]
            i += 1
        else:
            sec_aux[x] = '*'
    print(sec_aux)

for i in range(30):
    print('iteracion' + str(i))
    puntos[i] = puntaje(sec1[0:i], sec2[30 - i:30])

for j in range(120):
    print('iteracion' + str(j+30))
    puntos[j + 30] = puntaje(sec1[j:j+30], sec2[0:30])

print(sec1)
print(sec2)
print(puntos)
coincidencia()
imprimir(coincidencia())