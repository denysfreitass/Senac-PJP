# Leia kilobytes (int). Converta para megabytes inteiros com //= 1024.

print(f"Vamos transformar kilobytes em megabytes")
kbyt = int(input("Digite o vamos de kilobytes para transformar: "))
megabytes = kbyt
megabytes //= 1024
print(f"O valor de {kbyt} transformados em megabytes ficam {megabytes} megabytes")