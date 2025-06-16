import os
import json
from openai import AsyncOpenAI
from dotenv import load_dotenv
from difflib import get_close_matches

load_dotenv()

client = AsyncOpenAI()

# Carrega o JSON com as refeições
with open("refeicoes.json", "r", encoding="utf-8") as f:
    refeicoes = json.load(f)

# Lista de possíveis tags
TAGS_VALIDAS = {"picante", "vegano", "sem lactose", "sem gluten", "sem glúten", "sem açúcar", "sem açucar"}

# Função para filtrar refeições com base nos termos
def filtrar_refeicoes(pergunta: str):
    pergunta_lower = pergunta.lower()

    resultados = []

    for item in refeicoes:
        match_score = 0

        nome = item.get("nome", "").lower()
        desc = item.get("descricao", "").lower()
        tags = set(t.lower() for t in item.get("tags", []))

        # Boost se termos estiverem no nome ou descrição
        if any(term in nome or term in desc for term in ["arroz", "legume", "proteína", "carne", "frango", "tofu", "ovo"]):
            match_score += 1

        # Filtros por tags na pergunta
        for tag in TAGS_VALIDAS:
            if tag in pergunta_lower and tag in tags:
                match_score += 1

        if match_score > 0:
            resultados.append((match_score, item))

    # Ordena por score (decrescente) e retorna os top 10
    resultados.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in resultados[:10]]

# Gera uma resposta amigável com base na pergunta e resultados
async def gerar_resposta(pergunta, resultados):
    if not resultados:
        return "Poxa, não encontrei nenhuma refeição que combine com isso 😕. Quer tentar com outros critérios?"

    prompt = f"""
Você é um assistente de recomendação de refeições. O usuário fez a seguinte pergunta:

"{pergunta}"

Com base nisso, recomende amigavelmente até 5 das seguintes refeições, destacando os pontos fortes e respeitando as preferências:

{json.dumps(resultados, indent=2, ensure_ascii=False)}
"""

    resposta = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return resposta.choices[0].message.content.strip()
