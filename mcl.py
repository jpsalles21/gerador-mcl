import pandas as pd
import matplotlib.pyplot as plt
import os

# ==== Parâmetros do Método Congruente Linear ====
X0 = 987654321         # Semente
a = 1664525     # Multiplicador
c = 1013904223          # Incremento
M = 2**32         # Módulo
n = 1000           # Quantidade de números

# ==== Função do MCL ====
def lcg(seed, a, c, m, n):
    X = seed
    numeros = []
    for _ in range(n):
        X = (a * X + c) % m
        numeros.append(X / m)  
    return numeros

# ==== Gerar números ====
numeros = lcg(X0, a, c, M, n)


plt.scatter(range(n), numeros, s=10, alpha=0.7)
plt.title("Gráfico de Dispersão - Método Congruente Linear")
plt.xlabel("Índice")
plt.ylabel("Número Pseudoaleatório")
plt.grid(True)
plt.show()


caminho_csv = os.path.join(os.path.dirname(__file__), "numeros.csv")
pd.DataFrame(numeros, columns=["Número"]).to_csv(caminho_csv, index=False)
