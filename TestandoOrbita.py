import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definição da função para calcular a posição orbital futura
def calculate_future_position(a, e, n, t0, x):
    return a * (1 - e * np.cos(n * (t0 + x)))

# Parâmetros orbitais
a = 0.728      # Semi-eixo maior em AU
e = 0.068      # Excentricidade
n = 0.04501    # Movimento angular médio em radianos por dia
t0 = 4386      # Tempo de referência inicial em dias

# Número de dias futuros a partir do dia atual
x = np.linspace(0, 600, 1000)  # Array de 0 a 600 dias com 1000 pontos

# Calcular a posição orbital futura
y = calculate_future_position(a, e, n, t0, x)

# Plotar o gráfico
plt.plot(x, y, label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de y em função de x para $0.728*(1-(0.068*cos(0.04501*(4386+x))))$')
plt.legend()
plt.grid(True)
plt.show()

# Salvar os dados em um CSV
data = {
    'Dias Futuros (x)': x,
    'Posição Orbital (y)': y
}

df = pd.DataFrame(data)
df.to_csv('orbita_venus.csv', index=False)
