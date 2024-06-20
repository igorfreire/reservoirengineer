import math
import numpy as np
import matplotlib.pyplot as plt


#Entrada de valores para calcular vazão e estocagem conforme equação Darcy

#Kr: permeabilidade relativa
#Kabs: permeabilidade absoluta
#h: espessura do reservatório
#uo: viscosidade do óleo
#Bo: fator volume-formação do óleo
#Pr: pressão no reservatório
#Pwf: pressão no fundo do poço
#S: fator de dano (skin)
#Rw: raio do poço
#Re: raio de drenagem do reservatório
kabs = float(input("Digite o kabs (mD): "))
h = float(input("Digite o h (ft): "))
Pr = float(input("Digite o Pr (psi): "))
Pwf = float(input("Digite o Pwf (psi): "))
uo = float(input("Digite o uo (cp): "))
Bo = float(input("Digite o Bo (bbl/bbl): "))
Re = float(input("Digite o Re (ft): "))
Rw = float(input("Digite o Rw (ft): "))
S = float(input("Digite o S : "))

#Calculando Denominador da equação de Darcy para fluxo radial em regime estacionário

DENO = Bo*uo*(math.log(Re/Rw)+ S)

#calcular Vazão qo

qo = (0.00708*kabs*h*(Pr-Pwf))/ (DENO)

#calcular o fator de estocagem S

esto = (Pr-Pwf)/qo

print("Valor de Q0 =", qo, "bbl/d")
print("Valor no fator de Estocagem = ", esto )

p10 = 0.1 * qo
p20 = 0.2 * qo
p30 = 0.3 * qo
p40 = 0.4 * qo
p50 = 0.5 * qo
p60 = 0.6 * qo
p70 = 0.7 * qo
p80 = 0.8 * qo
p90 = 0.9 * qo
p100 = qo

#serie de dados de vazão

vazao = np.array([p10, p20, p30, p40, p50, p60, p70, p80, p90, p100])
legenda = np.array([10,20,30,40,50,60,70,80,90,100])

#Plotar o grafico

plt.figure(figsize=(10,6))
plt.plot(vazao, legenda, marker='o', linestyle='-', color='b')

for i in range(len(vazao)):
    plt.text(legenda[i], vazao[i], f'{vazao[i]:.1f}', fontsize=9, ha='center', va='bottom')

plt.title('IP Forecast - Eq.Darcy')
plt.xlabel('Vazão')
plt.ylabel('%')
plt.grid(True)
plt.show()
