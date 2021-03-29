
class movimientoJugador():
    def __init__(self,grid,posicionJugador):
        self.grid = grid
        self.posicionJugador = posicionJugador
    def movimientoArriba(self):
        if (self.posicionJugador[0] > 0):
            if (self.grid[self.posicionJugador[0] - 1][self.posicionJugador[1]] != 1 and self.grid[self.posicionJugador[0] - 2][self.posicionJugador[1]] != 4 ):
                self.grid[self.posicionJugador[0] - 2][self.posicionJugador[1]] = 3
                self.grid[self.posicionJugador[0]][self.posicionJugador[1]] = 0
                self.posicionJugador = (self.posicionJugador[0] - 2, self.posicionJugador[1])
                return self.posicionJugador
        if(self.posicionJugador == None):
            return self.posicionJugador
        else:
            return self.posicionJugador

    def movimientoAbajo(self):
        if (self.posicionJugador[0] < 12):
            if (self.grid[self.posicionJugador[0] + 1][self.posicionJugador[1]] != 1 and self.grid[self.posicionJugador[0] + 1][self.posicionJugador[1]] != 4):
                self.grid[self.posicionJugador[0] + 2][self.posicionJugador[1]] = 3
                self.grid[self.posicionJugador[0]][self.posicionJugador[1]] = 0
                self.posicionJugador = (self.posicionJugador[0] + 2, self.posicionJugador[1])
                return self.posicionJugador
        if (self.posicionJugador == None):
            return self.posicionJugador
        else:
            return self.posicionJugador
    def movimientoDerecha(self):
        if (self.posicionJugador[1] < 12):
            if (self.grid[self.posicionJugador[0]][self.posicionJugador[1] + 1] != 1 and self.grid[self.posicionJugador[0]][self.posicionJugador[1] + 2] != 4):
                self.grid[self.posicionJugador[0]][self.posicionJugador[1] + 2] = 3
                self.grid[self.posicionJugador[0]][self.posicionJugador[1]] = 0
                self.posicionJugador = (self.posicionJugador[0], self.posicionJugador[1] + 2)
                return self.posicionJugador
        if (self.posicionJugador == None):
            return self.posicionJugador
        else:
            return self.posicionJugador
    def movimientoIzquierda(self):
        if (self.posicionJugador[1] > 0):
            if (self.grid[self.posicionJugador[0]][self.posicionJugador[1] - 1] != 1 and self.grid[self.posicionJugador[0]][self.posicionJugador[1] - 2] != 4):
                self.grid[self.posicionJugador[0]][self.posicionJugador[1] - 2] = 3
                self.grid[self.posicionJugador[0]][self.posicionJugador[1]] = 0
                self.posicionJugador = (self.posicionJugador[0], self.posicionJugador[1] - 2)
                return self.posicionJugador
        if (self.posicionJugador == None):
            return self.posicionJugador
        else:
            return self.posicionJugador