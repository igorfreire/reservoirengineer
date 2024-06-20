import math

k = float(input("Digite o kr (fr): "))
h = float(input("Digite o h (): "))
Pr = float(input("Digite o Pr (psi): "))
Pwf = float(input("Digite o Pwf (psi): "))
uo = float(input("Digite o uo (cp): "))
Bo = float(input("Digite o Bo (bbl/bbl): "))
Re = float(input("Digite o Re (ft): "))
Rw = float(input("Digite o Rw (ft): "))
S = float(input("Digite o S : "))

P = (Pr-Pwf)
mi = 141.2*uo*Bo
R = math.log(Re/Rw)

#calcular Vazão qo
qo = (k*h*P)/(mi*(R-0.75+S))

print("Valor de Q0=", qo)