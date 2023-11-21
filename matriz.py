matriz = []

matriz.append('Caroline', 'karolines@hotmail.com', '1020-2020' )
matriz.append(['Fernanda', 'fernanda@teste.com', '2123-2020'])

for elemento in matriz:
    for elem in elemento:
     print(elem)

for elemento in matriz:
   saida=''
   saida = saida + elem + "\t"
   print(saida)