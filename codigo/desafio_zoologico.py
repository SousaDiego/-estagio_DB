animais = {
    "LEAO": {"tamanho": 3, "bioma": ["savana"], "carnivoro": True},
    "LEOPARDO": {"tamanho": 2, "bioma": ["savana"], "carnivoro": True},
    "CROCODILO": {"tamanho": 3, "bioma": ["rio"], "carnivoro": True},
    "MACACO": {"tamanho": 1, "bioma": ["savana", "floresta"], "carnivoro": False},
    "GAZELA": {"tamanho": 2, "bioma": ["savana"], "carnivoro": False},
    "HIPOPOTAMO": {"tamanho": 4, "bioma": ["savana", "rio"], "carnivoro": False},
}


recintos = [
    {"numero": 1, "bioma": ["savana"], "tamanho_total": 10, "animais": [("MACACO", 3)]},
    {"numero": 2, "bioma": ["floresta"], "tamanho_total": 5, "animais": []},
    {"numero": 3, "bioma": ["savana", "rio"], "tamanho_total": 7, "animais": [("GAZELA", 1)]},
    {"numero": 4, "bioma": ["rio"], "tamanho_total": 8, "animais": []},
    {"numero": 5, "bioma": ["savana"], "tamanho_total": 9, "animais": [("LEAO", 1)]},
]

def encontrar_recintos(animal, quantidade):

    if animal not in animais:
        return {"erro": "Animal inválido"}

    if quantidade <= 0:
        return {"erro": "Quantidade inválida"}

    recintos_viaveis = []

    for recinto in recintos:
        espaco_ocupado = 0

        for animal_no_recinto, qtd in recinto["animais"]:
            espaco_ocupado += animais[animal_no_recinto]["tamanho"] * qtd

        if len(recinto["animais"]) > 1:
            espaco_ocupado += 1

        espaco_necessario = animais[animal]["tamanho"] * quantidade
        if len(recinto["animais"]) > 0:
            espaco_necessario += 1  

        bioma_compativel = any(b in recinto["bioma"] for b in animais[animal]["bioma"])
        if not bioma_compativel:
            continue

        espaco_livre = recinto["tamanho_total"] - espaco_ocupado
        if espaco_livre < espaco_necessario:
            continue

        if animais[animal]["carnivoro"] and len(recinto["animais"]) > 0:
            continue

        espaco_restante = recinto["tamanho_total"] - (espaco_ocupado + espaco_necessario)
        recintos_viaveis.append(f"Recinto {recinto['numero']} (espaço livre: {espaco_restante} total: {recinto['tamanho_total']})")

    if not recintos_viaveis:
        return {"erro": "Não há recinto viável"}

    return {"recintosViaveis": sorted(recintos_viaveis)}

animal = input("Informe o tipo de animal: ").upper()
quantidade = int(input("Informe a quantidade: "))

resultado = encontrar_recintos(animal, quantidade)

print(resultado)
