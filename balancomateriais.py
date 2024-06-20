import pandas as pd
import matplotlib.pyplot as plt

# Definindo os dados de entrada
dados = {
    'Tempo (dias)': [0, 30, 60],
    'Pressão (psi)': [3000, 2950, 2900],
    'Produção acumulada de óleo (STB)': [0, 5000, 10000],
    'Produção acumulada de gás (SCF)': [0, 20000, 40000],
    'Produção acumulada de água (STB)': [0, 1000, 2000],
    'Volume de água injetada (STB)': [0, 500, 1000],
    'Bo (rb/STB)': [1.2, 1.21, 1.22],
    'Bg (rb/SCF)': [0.005, 0.0051, 0.0052],
    'Bw (rb/STB)': [1.0, 1.001, 1.002]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Definindo parâmetros estáticos
OOIP = 500000  # Volume de óleo original no lugar
Rs = 0         # Razão gás-óleo dissolvido inicial (simplificação)

# Função para calcular N usando balanço de materiais
def calcular_N(row, OOIP, Rs):
    Np = row['Produção acumulada de óleo (STB)']
    Gp = row['Produção acumulada de gás (SCF)']
    Wp = row['Produção acumulada de água (STB)']
    Wi = row['Volume de água injetada (STB)']
    Bo = row['Bo (rb/STB)']
    Bg = row['Bg (rb/SCF)']
    Bw = row['Bw (rb/STB)']
    
    if Np == 0:  # Evita divisão por zero
        return OOIP

    Rp = Gp / Np if Np != 0 else 0  # Razão gás-óleo produzido
    
    numerador = Np * Bo + (Gp - Np * Rs) * Bg + (Wi - Wp) * Bw
    denominador = Bo + (Rp - Rs) * Bg
    
    if denominador == 0:
        return float('nan')  # Evita divisão por zero

    N = numerador / denominador
    return N

# Calculando N para cada linha do DataFrame
df['N (STB)'] = df.apply(lambda row: calcular_N(row, OOIP, Rs), axis=1)

# Imprimindo o DataFrame com os resultados
print(df)

# Plotando os gráficos
plt.figure(figsize=(10, 5))

# Gráfico de Produção Acumulada de Óleo vs. Tempo
plt.subplot(1, 2, 1)
plt.plot(df['Tempo (dias)'], df['Produção acumulada de óleo (STB)'], marker='o')
plt.title('Produção Acumulada de Óleo vs. Tempo')
plt.xlabel('Tempo (dias)')
plt.ylabel('Produção Acumulada de Óleo (STB)')

# Gráfico de Pressão do Reservatório vs. Tempo
plt.subplot(1, 2, 2)
plt.plot(df['Tempo (dias)'], df['Pressão (psi)'], marker='o', color='r')
plt.title('Pressão do Reservatório vs. Tempo')
plt.xlabel('Tempo (dias)')
plt.ylabel('Pressão (psi)')

plt.tight_layout()
plt.show()

