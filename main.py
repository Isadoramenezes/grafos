from grafo import Grafao


#Inicializando o grafo 
teste = {"a":["ac", "ca"],
"b":["cb", "bc", "be", "eb"],
"c":["ce", "ec", "cd", "dc", "ca", "bc", "cb"],
"d":["cd", "dc"],
"e":["eb", "be", "ce", "ec"],
"f":[]}

#Adicionando um vértice
teste["j"] = ["ej", "dj"]
print(teste)

print( )

#Deletando um nó
del(teste["e"])
print(teste)


