distancia_km = 225000000
velocidad_kmh = 10000
tiempo_horas = 0
tiempo_dias = 0
for velocidad_kmh in range (10000, 50000+1, 10000):
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Para {velocidad_kmh} km/h -> Tiempo: {tiempo_dias} días")