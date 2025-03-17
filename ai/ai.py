"""
pyBodyTrack - A Python package for motion quantification in videos.

Author: Angel Ruiz Zafra
License: MIT License
Version: 2025.2.1
Repository: https://github.com/bihut/pyBodyTrack
Created on 17/3/25 by Angel Ruiz Zafra
"""
import os
from dotenv import load_dotenv,find_dotenv
import openai

# Cargar API Key desde .env
dotenv_path = find_dotenv("../credentials.env")
load_dotenv(dotenv_path)
api_key = os.getenv("OPENAI_API_KEY")
helicone_key = os.getenv("HELICONE_KEY")
print("API KEY:",api_key)

# Crear cliente OpenAI con la nueva API
#client = openai.OpenAI(api_key=api_key)
client = openai.OpenAI(
  api_key=api_key,
  base_url="https://oai.helicone.ai/v1",
  default_headers={
    "Helicone-Auth": f"Bearer "+helicone_key
  }
)

# Hacer una consulta a OpenAI
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "¿Cuál es la capital de España?"}]
)

# Imprimir la respuesta
print(response.choices[0].message.content)

