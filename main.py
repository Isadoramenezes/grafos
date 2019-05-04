#Inicializando o grafo 
teste = {"a":["ac", "ca"],
"b":["cb", "bc", "be", "eb"],
"c":["ce", "ec", "cd", "dc", "ca", "bc", "cb"],
"d":["cd", "dc"],
"e":["eb", "be", "ce", "ec"],
"f":[]}

class Grafo:
#Método que lista o grafo
    def listar(grafo):
        print("A listagem inicial do grafo")
        for x in teste:
            print(teste[x])
#Método para adicionar um nó e arestas
    def add(grafo, no, aresta):
        grafo[no] = [aresta]
        print("o grafo com vertice adicionado:")
        print(grafo)
#Método que deleta um nó    
    def delete(grafo, no):
        del(grafo[no])
        print("O grafo com no deletado: ")
        print(grafo)


#Chamada de Métodos
Grafo.listar(teste)
Grafo.add(teste, "a", "da")
Grafo.delete(teste, "d")

