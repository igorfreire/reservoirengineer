def interpolar_rgo(dados_rgo, indices, novo_indice):
    if novo_indice < indices[0]:
        return dados_rgo[0]
    if novo_indice > indices[-1]:
        return dados_rgo[-1]

    for i in range(len(indices) - 1):
        if novo_indice >= indices[i] and novo_indice < indices[i + 1]:
            indice_poco_1 = indices[i]
            indice_poco_2 = indices[i + 1]
            rgo1 = dados_rgo[i]
            rgo2 = dados_rgo[i + 1]
            break
    
    rgo_interpolado = rgo1 + ((novo_indice - indice_poco_1) / (indice_poco_2 - indice_poco_1)) * (rgo2 - rgo1)
    
    return rgo_interpolado

# Dados de exemplo
dados_rgo = [1.014, 0.6615, 0.31538, 0.707]
indices = [0, 1, 2, 3]
novo_indice = 4

# Calcular o próximo valor de RGO usando interpolação linear
rgo_proximo = interpolar_rgo(dados_rgo, indices, novo_indice)
print("Próximo valor de RGO:", rgo_proximo)

