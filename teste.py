import csv
import random
import numpy as np
def gerarTabelas(caminho_arquivo):
    a = np.array([random.uniform(1,100) for i in range(18)]).reshape(3,6)
    with open(caminho_arquivo, 'a') as arquivo_csv: 
        for coluna in a:
            for num in coluna:
                arquivo_csv.write(str(num))
                arquivo_csv.write(',')
            arquivo_csv.write('\n')
        arquivo_csv.close()
        
            
            
gerarTabelas('./teste1.csv')