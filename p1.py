#Empieza la p1#

#Se plotea el espectro solar#
datos=np.loadtxt('sun_AM0.dat') #se cargan los datos#

longitudesdeonda=datos[:,0] #se extraen las columnas de datos por separado#
espectro=datos[:,1]

longitudesdeondanorm=[x * 0.001 for x in longitudesdeonda] #se normalizan los vectores a unidades astronómicas#
espectronorm=[x * (10**10) for x in espectro]

plt.plot(longitudesdeondanorm, espectronorm, '.r') #se hace el gráfico del espectro solar#

plt.xlim(0,5) #se acorta el rango de graficación para mejor entendimiento del gráfico#

plt.xlabel('Longitud de onda $[\mu m]$')
plt.ylabel('Espectro $[g/ (cm s{^3})]$')
plt.title('Espectro del sol v/s longitud de onda')

plt.grid(True)
plt.savefig("graficop1.png")
plt.show()

#aquí termina la p1#
