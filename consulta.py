import json

def carregar_refeicoes():
    with open("refeicoes.json", "r", encoding="utf-8") as f:
        return json.load(f)

def buscar_refeicoes(tags_desejadas=None, max_preco=None, ingredientes_desejados=None):
    refeicoes = carregar_refeicoes()
    resultados = []

    for item in refeicoes:
        if tags_desejadas:
            if not all(tag in item.get("tags", []) for tag in tags_desejadas):
                continue

        if ingredientes_desejados:
            descricao = (item.get("descricao") or "").lower()
            if not all(ing.lower() in descricao for ing in ingredientes_desejados):
                continue

        if max_preco is not None and item["preco"] > max_preco:
            continue

        resultados.append(item)

    return sorted(resultados, key=lambda r: r["preco"])
