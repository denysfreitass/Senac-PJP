#Leia a distância (km) e o tempo (h), calcule a velocidade média.

print("Olá, vamos calcular a sua velocidade média no treino de corrida!")
dist = float(input("Digite a distancia percorrida em KM: "))
tempo = float(input("Digite quanto tempo você levou em minutos: "))

tempo = tempo / 60
vel_media = dist / tempo 
print(f"Nesse treino, sua velocidade média foi {vel_media:.2f} km/h")