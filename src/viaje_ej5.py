respuesta = "s"
while respuesta == "s":
    distancia_km = int(input("Introduce la distancia en km:"))
    velocidad_kmh = int(input("Introduce la velocidad en km/h:"))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    respuesta = str(input("¿Quieres hacer otra simulación? (s/n): "))