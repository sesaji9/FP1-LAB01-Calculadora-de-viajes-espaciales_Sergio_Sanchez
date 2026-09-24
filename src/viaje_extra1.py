dist = int(input("Introduce la distancia total en km: "))
num_paradas = 0
for dist in range(150000,dist+1,150000):
    print(f"Parada en el km {dist}")
    num_paradas +=1
print(f"Total de paradas para repostar: {num_paradas}")