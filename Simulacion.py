import random
import matplotlib.pyplot as plt

class MonteCarlo: 
    def __init__(self, x, y, z, pasos):
        self.x = x
        self.y = y 
        self.z = z 
        
        self.pasos = pasos 
        
        self.arrX = []
        self.arrY = []
        self.arrZ = []

    def movimiento(self):
        while self.pasos > 0:
            movX = random.choice(['izquierda', 'derecha'])
            movY = random.choice(['abajo', 'arriba'])
            movZ = random.choice(['adelante','atras'])
            
            match movX:
                case 'izquierda':
                    self.x -= 1
                case 'derecha':
                    self.x += 1
                    
            match movY:
                case 'arriba':
                    self.y += 1
                case 'abajo':
                    self.y -= 1
            
            match movZ:
                case 'adelante':
                    self.z+=1
                case 'atras':
                    self.z-=1
                
                
            self.arrX.append(self.x)
            self.arrY.append(self.y)
            self.arrZ.append(self.y)
            
            self.pasos -= 1
            
    def graficar(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.arrX, self.arrY, self.arrZ, 'b-', linewidth=0.5,label='Recorrido')
        ax.scatter(self.arrX[0], self.arrY[0], self.arrZ[0], c='r', marker='o',label='Inicio')
        ax.scatter(self.arrX[-1], self.arrY[-1], self.arrZ[-1], c='g', marker='o',label='Final')
        ax.set_title('Simulación de MonteCarlo')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.legend()
        plt.show()

