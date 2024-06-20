# Dados de exemplo (RGO)
dados_rgo = [
    1.014,
    0.6615,
    0.31538,
    0.707
]

def interpolar_rgo(dados_rgo, indice_poco):
    rgo_interpolado = None
    if 0 <= indice_poco < len(dados_rgo):
        if indice_poco == len(dados_rgo) - 1:  # Caso especial para o último ponto
            rgo_interpolado = dados_rgo[-1]
        else:
            rgo1 = dados_rgo[indice_poco]
            rgo2 = dados_rgo[indice_poco + 1]
            # Fórmula da interpolação linear
            rgo_interpolado = rgo1 + (indice_poco / (len(dados_rgo) - 1)) * (rgo2 - rgo1)
    return rgo_interpolado

# Exemplo de uso
indice_poco_novo = 3  # Índice do novo poço
rgo_estimado = interpolar_rgo(dados_rgo, indice_poco_novo)
print("RGO estimado para o Campo de São João:", rgo_estimado)

