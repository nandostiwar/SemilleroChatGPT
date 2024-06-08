

import openai

# Reemplaza 'your-api-key' con tu clave API de OpenAI
openai.api_key = 'your-api-key'

# Define el prompt que deseas enviar
prompt = "cuánto es 2+2"

# Envía el prompt a la API de OpenAI
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Puedes elegir el modelo que prefieras
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": prompt}
    ]
)

# Muestra la respuesta en la consola
print(response.choices[0].message['content'].strip())