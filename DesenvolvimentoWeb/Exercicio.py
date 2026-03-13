'''


Exercício

1. Consulta de API Pública (GET)
• Use a API gratuita https://jsonplaceholder.typicode.com/posts
• Faça uma requisição GET para buscar todos os posts.
• Exiba apenas os títulos dos 5 primeiros posts.



2. Consulta com Parâmetros (GET com query string)
• Use https://jsonplaceholder.typicode.com/comments
• Envie um GET com parâmetro postId=1.
• Exiba os emails dos usuários que comentaram nesse post.



3. Envie uma requisição POST para https://jsonplaceholder.typicode.com/posts.
• Envie no corpo JSON:
• { "title": "Teste API", "body": "Primeiro post com requests", "userId": 123 }
• Exiba a resposta retornada pelo servidor.



4. Faça uma requisição GET para https://httpbin.org/headers:
• Enviando no cabeçalho um campo "X-Aluno": "SeuNome".
• Verifique se o cabeçalho aparece na resposta.





'''


import requests
url = 'https://jsonplaceholder.typicode.com'






#1.
resposta1 = requests.get(url=url + "/comments?postId=1")
for c in resposta1.json():
    print(c)









#2.
#O segredo aqui é usar a chave correta: 'postId' com I maiúsculo
filtros = {'postId': 1}
resposta2 = requests.get("https://jsonplaceholder.typicode.com/comments", params=filtros)

print("\n---Resposta GET ---")
print(resposta2.json()[:1]) #mostra apenas o primeiro cometário










#3
param = {"title": "Teste API",
         "body": "Primeiro post com requests",
         "userId": 123
}


resposta3 = requests.get("https://jsonplaceholder.typicode.com/posts", json=param)

print("\n---Resposta POST ---")
# O Status_code 201 confirma que o recurso foi criado com sucesso
print(f"Status: {resposta3.status_code}")
print(resposta3.json())









#4
cabecalho = {"X-Aluno": "SeuNome"          
}


resposta4 = requests.get("https://httpbin.org/headers", json=cabecalho)


print("\n---Resposta Cabeçalho ---")
print(f"Status: {resposta4.status_code}")
print(resposta4.json())



