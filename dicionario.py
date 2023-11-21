pessoa1 = {}
pessoa1['nome'] = "Renato"
pessoa1['email'] = 'renato@teste.com'
pessoa1['telefone'] = '2110-2020'

pessoa3 = {}

pessoa3['nome'] = input("Informe o nome: ")
pessoa3['email'] = input("Informe o e-mail: ")
pessoa3['telefone'] = input("Informe o telefone: ")




agenda = []
agenda.append(pessoa1)
for contato in agenda:
    print(contato['nome'])

agenda.append(pessoa3)