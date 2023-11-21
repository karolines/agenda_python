
soma = 0
media = 0
for contador in range(10):
   numero = (input("Informe número: "))
   soma = soma + numero
   media = soma / 10

   print(f"A soma é {soma}\n a média é {media:.2f}")