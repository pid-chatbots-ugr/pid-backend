"""


Author: Angel Ruiz Zafra
License: MIT License
Version: 2025.2.1
Repository: https://github.com/pid-chatbots-ugr/pid-backend
Created on 17/3/25 by Angel Ruiz Zafra
"""
import os
from dotenv import load_dotenv,find_dotenv
import openai
class OpenAI:
    def __init__(self):
        """
        Inicializa la conexión con OpenAI usando credenciales desde .env.
        """
        # Cargar API Key desde .env
        dotenv_path = find_dotenv("../credentials.env")
        load_dotenv(dotenv_path)
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.helicone_key = os.getenv("HELICONE_KEY")
        #print("API KEY:",api_key)

        # Crear cliente OpenAI con la nueva API
        #client = openai.OpenAI(api_key=api_key)

    def initClient(self):
        self.client = openai.OpenAI(
          api_key=self.api_key,
          base_url="https://oai.helicone.ai/v1",
          default_headers={
            "Helicone-Auth": f"Bearer "+self.helicone_key
          }
        )
        #return self.client
    def request(self,message,model="gpt-4"):
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    '''
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
'''


# Imprimir la respuesta
#print(response.choices[0].message.content)

