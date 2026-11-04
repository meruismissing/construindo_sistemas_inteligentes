my_list = ["Mel", "valval", "Mocha", "Daniel"]

for item in my_list:
    print(item)

elemento = input("Digite qual item deseja remover da lista: ")

if elemento in my_list:
    my_list.remove(elemento)
    print("Removido com sucesso!")

else: 
    print("Esse elemento não existe na lista")

print(my_list)
