print("Iniciando em python");

grafo = {"a":["ac", "ca"],
"b":["cb", "bc", "be", "eb"],
"c":["ce", "ec", "cd", "dc", "ca", "bc", "cb"],
"d":["cd", "dc"],
"e":["eb", "be", "ce", "ec"],
"f":[]}

grafo["j"] = ["ej", "dj"]

print(grafo)
print( )
del(grafo["e"])
print(grafo)