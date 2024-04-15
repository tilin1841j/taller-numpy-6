import numpy as np 
#matplotlib tiene muhcos modulos. importar uno solo
import matplotlib.pyplot as plt 

#Crear un ndarray de 1 dimension, 100 elementos equiespaciados, de 0 a 2*PI
x= np.linspace(0, 2*np.pi, 100)
y= np.sin(x)

# usar matplotlib
plt.figure(figsize=(8,4))
plt.title("MI primer gráfico cientifico en progrmacion")
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("seno de x")
plt.grid(True)
plt.show()