import csv

import matplotlib.pyplot as plt
import numpy as np

# Definindo o caminho completo para o arquivo CSV
caminho_arquivo = './tabelas/teste.csv'
n_colunas = 3
n_sensor = 3
n_medidas = 2

def gerarGrafico(file):
    with open(f"./tabelas/{file}", newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        dados_csv = np.array([abs(float(x)) for x in list(leitor_csv)[0]], dtype=np.float64).reshape((n_colunas, n_medidas * n_sensor))  
        
    Z = 266.413 * np.power(dados_csv, -1)

    # Crie uma grade de coordenadas x e y
    x = np.linspace(0, n_medidas * n_sensor -1, n_medidas * n_sensor)
    y = np.linspace(0, n_colunas-1, n_colunas)
    X, Y = np.meshgrid(x, y)

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
    # plt.show()
    save = './graficos/'+file.split('.')[0]
    print(save)
    plt.savefig(save)
    # plt.close()