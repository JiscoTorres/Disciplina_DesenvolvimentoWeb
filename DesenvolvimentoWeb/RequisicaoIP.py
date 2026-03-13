
'''



EXERCÍCIO.Simule uma requisição HTTP através do Postman ou outra ferramenta gratuita (www.4alltest.com.br/testeapis ou https://reqbin.com)
https://httpbin.org
1.  Mostre o IP da requisição
2.  Solicite a exibição de um arquivo html
3.  Solicite uma imagem jpg
4.  Decodifique a string Base64 VGVzdGFuZG8gMSwgMiwgMy4uLg==



'''


import requests #Importar a biblioteca requests




#1.
resposta1 = requests.get('https://httpbin.org/ip')#pegar esse https no  https://httpbin.org
print (resposta1.status_code, resposta1.json()) #no Response content type dentro da aba Request inspection GET ip, diz que o tipo da resposta precisa ser Json()
#No terminal apareceu o ip!! 
#status code para mostar de deu certo, no caso, 200







#2.
resposta2 = requests.get('https://httpbin.org/html')#peguei o https://httpbin.org/html em Response formats GET html
print (resposta2.text)#vai aparecer o texto html








#3.
resposta3 = requests.get("https://httpbin.org/image/jpeg")#pegar esse https://httpbin.org/image/jpeg em  Images GET image jpeg

with open(r'C:\Users\joao.torres\Downloads\DesenvolvimentoWeb\arquivo.jpge', 'wb') as file:
    file.write(resposta3.content)








#4. Base 64
resposta4 = requests.get('https://httpbin.org/base64/SFRUUEJJTiBpcyBhd2Vzb21l')#peguei o https://httpbin.org/base64/SFRUUEJJTiBpcyBhd2Vzb21l em Dynamic data GET/base64/{vlue}
print (resposta4.text)

