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

class Grafo:
    def listar(self, ngf):
        for x in ngf:
            print(ngf[x])

Grafo.listar(teste, ngf)