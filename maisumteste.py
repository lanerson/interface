import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import random

plt.style.use('seaborn-darkgrid')

x_vals = list(range(1, 21)) * 20  # Coordenadas x fixas de 1 a 20, repetidas 20 vezes
y_vals = [i for _ in range(20) for i in range(1, 21)]  # Coordenadas y de 1 a 20, repetidas 20 vezes
z_vals = []

index = list(range(20))

def gerar_dado():
    return random.uniform(0, 10)

def animate(i):
    for _ in range(20):
        z_vals.extend([gerar_dado() for _ in range(20)])

    if len(z_vals) > 400:
        z_vals[:20] = []

    ax.clear()  # Limpa o eixo 3D para evitar sobreposição
    ax.plot_trisurf(x_vals, y_vals, z_vals, cmap='viridis', edgecolor='none', linewidth=0.2, antialiased=True)
    ax.set_xlabel('Tempo (X)')
    ax.set_ylabel('Tempo (Y)')
    ax.set_zlabel('Valor (Z)')
    ax.set_title('Curva de Nível em Tempo Real')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ani = FuncAnimation(fig, animate, interval=500)

plt.tight_layout()
plt.show()
