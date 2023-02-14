class   punto:

    def __init__(self,x,y):
        self.x: int = x
        self.y: int = y



class Rectangulo:

    def __init__(self, punto_1: punto,punto_2: punto,color_linea,color_fondo):
        self.punto_1: punto = punto_1
        self.punto_2: punto= punto_2
        self.color_linea = color_linea
        self.color_fondo = color_fondo

    def calcular_area(self) -> float:
        base = abs(self.Punto_2.x - self.Punto_1.x)
        altura = abs(self.Punto_2.y - self.Punto_1.y)
        return base * altura


    def calcular_perimetro(self)->float:
        base =abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)
        return (base + altura)*2

    def es_cuadrado(self) -> bool:
        base =abs(self.punto_2.x - self.punto_1.x)
        altura =abs(self.punto_2.y -self.punto_1.y)
        return base == alturax