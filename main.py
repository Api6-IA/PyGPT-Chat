import requests
import json

API_KEY = "INSERT YOUR API KEY"

link = "https://api.openai.com/v1/chat/completions"

msg_content = input("Digite o que deseja pesquisar no ChatGPT: ") 

body_msg = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": msg_content}]
}

body_msg = json.dumps(body_msg)
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

request = requests.post(link, headers=headers, data=body_msg)

answer = request.json()
msg = answer["choices"][0]["message"]["content"]
print(msg)
