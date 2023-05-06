import random 
import numpy as np
from Simulacion import MonteCarlo


#Objeto tipo Simulacion con constructor
Objmonte = MonteCarlo(50, 50, 0, 1000)

#Usar clases 
Objmonte.movimiento()
Objmonte.graficar()