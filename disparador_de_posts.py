import requests

#dict do exemplo
dicionario = [{
"id":23,
"lat":22.33333,
"longi":23.4444
},
{
"id":23,
"lat":22.55555,
"longi":23.3333
},
{
"id":23,
"lat":22.66666,
"longi":23.88888
}]

def disparador(dicionario):
    url = 'http://localhost:8080/insere'

    for d in dicionario:
        r = requests.post(url, json=d)
        print(r.text)
    return "Todo o body do post foi adicionado com sucesso!"

disparar = disparador(dicionario)
print(disparar)