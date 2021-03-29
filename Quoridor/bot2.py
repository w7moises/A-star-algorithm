import a_star

data1 = []
data2 = []
class algoritmo():
    def __init__(self,grid,inicio,final,jugador):
        self.grid = grid
        self.inicio = inicio
        self.final = final
        self.jugador = jugador
    def a_star(self):
        data1[:] = []
        data2[:] = []
        path = a_star.astar(self.grid,self.inicio,self.final,self.jugador)
        for elemento in path:
            data1.append(elemento[0])
            data2.append(elemento[1])
        return data1,data2

class movimientoBot():
    def __init__(self,grid,data1,data2,x,color):
        self.grid = grid
        self.data1 = data1
        self.data2 = data2
        self.x = x
        self.color = color
    def movimiento(self):
        self.grid[self.data1[self.x+2]][self.data2[self.x+2]] = self.color
        self.grid[self.data1[self.x]][self.data2[self.x]] = 0
        return (self.data1[self.x+2],self.data2[self.x+2])

