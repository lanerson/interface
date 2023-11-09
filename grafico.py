import pandas as pd
#teste

# Definindo o caminho completo para o arquivo CSV
# path = "C:/Users/catul/OneDrive/Área de Trabalho/calculo numerico/lista_1/arquivo_ipe.csv"  # Substitua 'caminho_completo' pelo caminho real do arquivo

def gerarGrafico(nome,path):
    
    # Lendo o arquivo CSV e armazenando os dados em um DataFrame
    df = pd.read_csv(path)

    # Convertendo o DataFrame em uma matriz
    M = df.values.tolist()

    # Exibindo a matriz M
    print(M)

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np

    # Crie uma matriz 2x11 e declare os valores no corpo do código
    m1 = M

    m2 = [[1 for _ in range(11)] for _ in range(2)]


    M = 266.413 * np.array(m2) / np.array(m1)

    # Imprima a matriz
    print("Matriz 2x11:")
    for linha in m1:
        print(linha)
    print(m1[0][0])
    print(M[0][0])

    # Crie uma grade de coordenadas x e y
    x = np.linspace(0, 10, 11)
    y = np.linspace(0, 1, 2)
    X, Y = np.meshgrid(x, y)

    # Converta a matriz em uma matriz numpy para os valores de Z
    Z = np.array(M)

    # Crie uma figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Crie o gráfico de superfície
    surf = ax.plot_surface(X, Y, Z, cmap="viridis")

    # Adicione uma barra de cores para representar os valores de Z
    fig.colorbar(surf)

    # Defina os rótulos dos eixos
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_zlabel("Eixo Z")

    # Mostre o gráfico
    # plt.show()
    plt.savefig(nome)
    plt.close()
