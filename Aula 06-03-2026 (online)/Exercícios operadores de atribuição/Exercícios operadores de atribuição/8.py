# Leia base de pontos (int) e combos (int). Aplique *=.

print("Vamos descobrir quantos pontos você fez somando os bases e os pontos de combos que dão 3 pontos cada combo?")

base = int(input("Digite quantos pontos base você fez: "))
combo = int(input("Digite quantos combos você realizou: "))

pontos_combo = 3
combo *= pontos_combo
print(f"Seu numero de pontos total foi", combo + base)
