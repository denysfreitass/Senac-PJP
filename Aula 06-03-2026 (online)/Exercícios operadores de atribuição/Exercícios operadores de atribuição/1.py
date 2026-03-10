# Leia saldo (float) e depósito (float). Use saldo += deposito e mostre o novo saldo.

saldo = float(input("Digite seu saldo atual: "))
deposito = float(input("Digite o valor do depósito: "))
saldo += deposito  
print(f"Seu novo saldo é {saldo}")