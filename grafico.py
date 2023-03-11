import matplotlib.pyplot as plt
import numpy as np
import librosa
from pydub import AudioSegment
#--Input
frequenza=int(input("Inserisci una frequenza:"))
frequenza2=int(input("Inserisci un'altra frequenza:"))
# Crea una funzione d'onda sinusoidale
def onda(ampiezza, frequenza, puntiX):
    return ampiezza * np.sin(2 * np.pi * frequenza * puntiX )
#----Y(x) = A sin( 2pi f x +fase(è = 0))------

#frequenza= 440
puntiX1 = np.linspace(0, 1/frequenza, 1000)
puntiX2 = np.linspace(0, 1/frequenza2, 1000)

#numpy.linspace restituisce valori equidistanti nel tempo.     

ampiezza = 10 #db

# Creare la funzione d'onda
puntiY1 = onda(ampiezza, frequenza, puntiX1)
puntiY2 = onda(ampiezza, frequenza2, puntiX2)
fig, axs = plt.subplots(2)


# Visualizzare il grafico della funzione d'onda

axs[0].plot(puntiX1, puntiY1)
axs[1].plot(puntiX2, puntiY2)

axs[0].set_xlabel('Tempo (s)')
axs[0].set_ylabel('Ampiezza (m)')
axs[1].set_xlabel('Tempo (s)')
axs[1].set_ylabel('Ampiezza (m)')
axs[0].set_title("Grafico del periodo dell'onda sonora a "+ str(frequenza) + " Hz")
axs[1].set_title("Grafico del periodo dell'onda sonora a "+ str(frequenza2) + " Hz")

fig.tight_layout()
axs[0].grid()
axs[1].grid()
plt.show()