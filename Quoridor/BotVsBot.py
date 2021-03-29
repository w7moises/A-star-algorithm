import pygame, random
import bot
import bot2
import bot3
import bot4
import jugador
import time

NARANJA = (255, 128, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AZUL = (14, 45, 99)
MORADO = (87,35,100)
PLIM = (241, 148, 138)
LARGO = 50
ALTO = 50
MARGEN = 5
x = 0


grid = [[0 for i in range(17)] for j in range(17)]
inicio = (8, 0)
finalBot = (8, 0)
final = (8, 16)
inicioBot = (8, 16)

inicioBot2 = (0,8)
finalBot2 = (16,8)

inicioBot3 = (16,8)
finalBot3 = (0,8)
turno = 0
pygame.init()
DIMENSION_VENTANA = [800, 800]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Quoridor")
hecho = False
reloj = pygame.time.Clock()

def ValidMove(G, i, j, move):
    if move == 'right':
        return G[i][j - 1] == 0
    elif move == 'top':
        return G[i + 1][j] == 0
    elif move == 'bot':
        return G[i - 1][j] == 0
    elif move == 'left':
        return G[i][j + 1] == 0
    else:
        return True

directionsRight = [(0, 2, 'right'), (-2, 0, 'top'), (2, 0, 'bot'), (0, -2, 'left')]
directionsLeft = [(0, -2, 'left'),(2, 0, 'bot'), (-2, 0, 'top'), (0, 2, 'right')]
directionsTop = [(-2, 0, 'top'), (0, 2, 'right'), (0, -2, 'left'),(2, 0, 'bot')]
directionsBot =  [(2, 0, 'bot'), (0, -2, 'left'), (0, 2, 'right'),(-2, 0, 'top')]


def findPath(G, start, end, directions):
    n = len(G)
    visited = [[False for x in range(17)] for y in range(17)]

    def dfs(i, j, move):
        if not ValidMove(G, i, j, move):
            return None
        if (i, j) == end:
            return [end]

        visited[i][j] = True

        for m, k, movement in directions:

            if i + m < 0 or i + m >= len(G):
                continue
            if j + k < 0 or j + k >= len(G):
                continue

            if not visited[i + m][j + k]:
                newPath = dfs(i + m, j + k, movement)
                if newPath:
                    return [(i, j)] + newPath

        visited[i][j] = False
        return None

    return dfs(start[0], start[1], '')


while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 3:
                pos = pygame.mouse.get_pos()
                if pos[0] < 300:
                    columna = pos[0] // (50)
                else:
                    columna = pos[0] // (45)

                if pos[1] < 300:
                    fila = pos[1] // (50)
                else:
                    fila = pos[1] // (45)
                print(pos[0], pos[1])

                if (grid[fila][columna] == 0 and columna % 2 != 0 or fila % 2 != 0):
                    if columna % 2 != 0 and fila % 2 != 0: continue
                    grid[fila][columna] = 1


        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                turno = 1
            if evento.key == pygame.K_2:
                turno = 2
            if evento.key == pygame.K_3:
                turno = 3
            if evento.key == pygame.K_4:
                turno = 4

    n = len(grid)
    for fila in range(n):
        for columna in range(n):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = AZUL
            if grid[fila][columna] == 2:
                color = VERDE
            if grid[fila][columna] == 3:
                color = ROJO
            if grid[fila][columna] == 4:
                color = NARANJA
            if grid[fila][columna] == 6:
                color = MORADO
            if grid[fila][columna] == 7:
                color = PLIM
            if columna % 2 != 0 and fila % 2 != 0:
                grid[fila][columna] = 5
                color = NEGRO
            if columna % 2 == 0:
                if columna == 0:
                    if fila % 2 != 0:
                        if fila == 1:
                            pygame.draw.rect(pantalla, color, [(MARGEN + LARGO) * (columna) + MARGEN,
                                                               (MARGEN + ALTO) * fila + MARGEN + 5, LARGO, 20])
                        else:
                            pygame.draw.rect(pantalla, color,
                                             [(MARGEN + LARGO) * (columna) + MARGEN, (MARGEN + 40) * fila + MARGEN + 15,
                                              LARGO, 20])
                        ##primera fila de bloques
                    else:
                        if fila == 0:
                            pygame.draw.rect(pantalla, color,
                                             [(MARGEN + LARGO) * (columna) + MARGEN, (MARGEN + 40) * fila + MARGEN,
                                              LARGO,
                                              ALTO])
                        else:
                            pygame.draw.rect(pantalla, color,
                                             [(MARGEN + LARGO) * (columna) + MARGEN, (MARGEN + 40) * fila + MARGEN,
                                              LARGO,
                                              ALTO])
                        ##primera columna
                elif columna < 17:  ##columnas pares que no sea 0
                    if fila % 2 != 0:
                        pygame.draw.rect(pantalla, color,
                                     [(MARGEN + 40) * (columna) + MARGEN, (MARGEN + 40) * fila + MARGEN + 15, LARGO,
                                          20])

                    else:
                        pygame.draw.rect(pantalla, color,
                                         [(MARGEN + 40) * (columna) + MARGEN, (MARGEN + 40) * fila + MARGEN,
                                          LARGO,
                                          ALTO])
            else:  ##columnas impares
                if columna == 1:
                    if fila % 2 != 0:
                        pygame.draw.rect(pantalla, color,
                                         [(MARGEN + LARGO) * (columna) + MARGEN + 5, (MARGEN + 40) * fila + MARGEN + 15,
                                          20, 20])
                    else:
                        pygame.draw.rect(pantalla, color,
                                         [(MARGEN + LARGO) * (columna) + MARGEN + 5, (MARGEN + 40) * fila + MARGEN, 20,
                                          ALTO])
                elif columna < 17:
                    if fila % 2 != 0:
                        pygame.draw.rect(pantalla, color,
                                         [(MARGEN + 40) * (columna) + MARGEN + 15, (MARGEN + 40) * fila + MARGEN + 15,
                                          20, 20])
                    else:
                        pygame.draw.rect(pantalla, color,
                                         [(MARGEN + 40) * (columna) + MARGEN + 15, (MARGEN + 40) * fila + MARGEN,
                                          20,
                                          ALTO])

    Recorrido = bot.algoritmo(grid, inicio, final, 2)
    path = Recorrido.a_star()
    data1 = path[0]
    data2 = path[1]

    Recorrido2 = bot2.algoritmo(grid, inicioBot, finalBot, 3)
    path2 = Recorrido2.a_star()
    data3 = path2[0]
    data4 = path2[1]

    Recorrido3 = bot3.algoritmo(grid, inicioBot2, finalBot2,6)
    path3 = Recorrido3.a_star()
    data5 = path3[0]
    data6 = path3[1]

    Recorrido4 = bot4.algoritmo(grid, inicioBot3, finalBot3,7)
    path4 = Recorrido4.a_star()
    data7 = path4[0]
    data8 = path4[1]



    if turno == 1:
        time.sleep(0.2)
        opcionBot = random.randint(1, 2)
        if (opcionBot == 1):
            Movimiento = bot.movimientoBot(grid, data1, data2, x, 4)
            Movimiento.movimiento()
            inicio = Movimiento.movimiento()
        elif (opcionBot == 2):
            path = findPath(grid, inicioBot, finalBot, directionsRight)
            orig = path[0]
            move = path[1]
            # top
            if orig[0] - move[0] == 2:
                grid[orig[0] + 1][orig[1]] = 1
            # bot
            if orig[0] - move[0] == -2:
                grid[orig[0] - 1][orig[1]] = 1
            # right
            if orig[1] - move[1] == -2:
                grid[orig[0]][orig[1] + 1] = 1
        turno = 2

    if turno == 2:
        opcionBot = random.randint(1, 2)
        if (opcionBot == 1):
            Movimiento2 = bot2.movimientoBot(grid, data3, data4, x, 3)
            Movimiento2.movimiento()
            inicioBot = Movimiento2.movimiento()

        elif (opcionBot == 2):
            path = findPath(grid, inicio, final, directionsLeft)
            orig = path[0]
            move = path[1]
            # top
            if orig[0] - move[0] == 2:
                grid[orig[0] + 1][orig[1]] = 1
            # bot
            if orig[0] - move[0] == -2:
                grid[orig[0] - 1][orig[1]] = 1
            # right
            if orig[1] - move[1] == -2:
                grid[orig[0]][orig[1] + 1] = 1

        turno = 3

    if turno == 3:
        opcionBot = random.randint(1, 2)
        if (opcionBot == 1):
            Movimiento3 = bot3.movimientoBot(grid, data5, data6, x, 6)
            Movimiento3.movimiento()
            inicioBot2 = Movimiento3.movimiento()

        elif (opcionBot == 2):
            path = findPath(grid, inicioBot3, finalBot3, directionsBot)
            orig = path[0]
            move = path[1]
            # top
            if orig[0] - move[0] == 2:
                grid[orig[0] + 1][orig[1]] = 1
            # bot
            if orig[0] - move[0] == -2:
                grid[orig[0] - 1][orig[1]] = 1
            # right
            if orig[1] - move[1] == -2:
                grid[orig[0]][orig[1] + 1] = 1

        turno = 4

    if turno == 4:
        opcionBot = random.randint(1, 2)
        if (opcionBot == 1):
            Movimiento4 = bot4.movimientoBot(grid, data7, data8, x, 7)
            Movimiento4.movimiento()
            inicioBot3 = Movimiento4.movimiento()

        elif (opcionBot == 2):
            path = findPath(grid, inicioBot2, finalBot2, directionsTop)
            orig = path[0]
            move = path[1]
            # top
            if orig[0] - move[0] == 2:
                grid[orig[0] + 1][orig[1]] = 1
            # bot
            if orig[0] - move[0] == -2:
                grid[orig[0] - 1][orig[1]] = 1
            # right
            if orig[1] - move[1] == -2:
                grid[orig[0]][orig[1] + 1] = 1

        turno = 1



    if (inicio == final or inicioBot == finalBot) :
       pygame.quit()

    reloj.tick(60)
    pygame.display.flip()
pygame.quit()
