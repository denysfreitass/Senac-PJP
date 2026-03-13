#Leia o raio de um círculo (float) e calcule a área, utilize π = 3.14.
#formula para calcular área (  Area = pi x raio² )

print("Vamos calcular o valor da área de um circulo")
raio = float(input("Digite o valor do raio: "))
area = 3.14 * (raio ** 2)
print(f"A area do circulo informado é {area:.2f}")