import asyncio
from agente import gerar_resposta, filtrar_refeicoes

async def main():
    while True:
        pergunta = input("Você: ").strip()
        if not pergunta:
            continue
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Até a próxima! 👋")
            break

        resultados = filtrar_refeicoes(pergunta)
        resposta = await gerar_resposta(pergunta, resultados)
        print("\nAssistente:\n" + resposta + "\n")

if __name__ == "__main__":
    asyncio.run(main())
