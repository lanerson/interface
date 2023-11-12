import csv
from numpy import float64 as flt

# Definindo o caminho completo para o arquivo CSV
caminho_arquivo = ".\\tabelas\\teste2.csv"  # Substitua 'caminho_completo' pelo caminho real do arquivo
n_sensor = 2
n_medidas = 11
def gerarGrafico(file):
    dados_csv = []
    # Lendo o arquivo CSV e armazenando os dados em um DataFrame
    with open(caminho_arquivo, newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
    
        # Iterar sobre as linhas do arquivo CSV
        for linha in leitor_csv:
            linha_ = list(map(lambda x: abs(flt(x)), linha))
            dados_csv.append(linha_)
    

    n_sensor = len(dados_csv)
    n_medidas = len(dados_csv[0])

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    # Crie uma matriz 2x11 e declare os valores no corpo do código
    m1 = dados_csv
    print('só imaginação\n',m1)
    m2 = [[1 for _ in range(n_medidas)] for _ in range(n_sensor)]

        
    M = 266.413*np.array(m2)/np.array(m1)
    # Imprima a matriz
    print("Matriz 2x11:")
    for linha in m1:
        print('oi',linha)

    # Crie uma grade de coordenadas x e y
    x = np.linspace(0, n_medidas-1, n_medidas)
    y = np.linspace(0, n_sensor-1, n_sensor)
    X, Y = np.meshgrid(x, y)

    # Converta a matriz em uma matriz numpy para os valores de Z
    Z = np.array(M)

    # Crie uma figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    # Crie o gráfico de superfície
    surf = ax.plot_surface(X, Y, Z, cmap='viridis')

    # Adicione uma barra de cores para representar os valores de Z
    fig.colorbar(surf)

    # Defina os rótulos dos eixos
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    # Mostre o gráfico
    plt.show()
    # plt.savefig("teste.png")
    plt.close()

gerarGrafico(caminho_arquivo)
