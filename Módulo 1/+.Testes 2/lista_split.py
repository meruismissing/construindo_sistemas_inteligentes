my_list = ["Mel", "valval", "Mocha", "Daniel"]

for item in my_list:
    print(item)

elemento = input("\nDigite qual item deseja remover da lista: ")

elementos = elemento.split(',')

for e in elementos:
    if e.strip() in my_list:
     my_list.remove(e.strip())
     print(f"{e} Removido com sucesso!") 
    else: 
     print("Esse elemento não existe na lista\n")

print(my_list)

