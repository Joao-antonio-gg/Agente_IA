# Assistente de Refeições Inteligente

Este projeto implementa um assistente virtual capaz de recomendar refeições com base em preferências alimentares do usuário, como restrições dietéticas, preço, ingredientes e estilo de prato. Utiliza a **OpenAI Responses API** e um **banco local de refeições em JSON**.

---

## Funcionalidades

- Recomendação inteligente com uso de linguagem natural
- Consulta de refeições locais (sem necessidade de banco de dados externo)
- Tratamento de:
  - Restrições alimentares (ex: vegano, sem lactose)
  - Preço máximo
  - Ingredientes desejados (ex: arroz, legumes, proteína)
- Suporte via **linha de comando** e **interface web simples com Flask**

---

## Tecnologias Usadas

- [Python 3.10+](https://www.python.org/)
- [OpenAI API](https://platform.openai.com/)
- [Flask](https://flask.palletsprojects.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---
## 🚀 Como Executar

### 1. Clonar o projeto
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

```  
  
### 2. Criar ambiente virtual  
```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

```

### 3. Instalar dependências  
```bash
pip install -r requirements.txt
```
### 4. Criar .env com a sua chave da OpenAI  

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx  

### 5. Executar a interface CLI
```bash
python cli.py
```

### 6. (Opcional) Executar a interface web
```bash
python app.py
```
  
