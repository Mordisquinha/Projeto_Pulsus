API de informações de geolocation por Gabriel Santiago.

Esta API se resume em 6 módulos: main.py, disparador_de_posts.py, get.py, database.py, models.py e create_db

A - Sobre a API:

    1- main.py
        módulo principal, corpo da API, com suas rotas 3 rotas.

        rota "/":
            pagina raiz da api
        
        rota "/get":
            retorna todos os ids, latitude e longitude cadastrados no banco de dados da API

        rota "/get/{id}":
            retorna a latitude e longitude de um determinado id
        
        rota "/insere":
            insere ao banco de dados um body json de um método body 

    2- disparador_de_post.py
        como normalmente o método post só funciona com um body por vez, o disparador_de_post irá disparar tantos bodys quanto existir no json na lista "dicionario"

    3- get.py
        módulo onde é gerado o retorno dos métodos "get", tanto o da rota "/get" quanto a rota "/get/{id}"
        através de scripts "sql" pela biblioteca pymysql

    4- database.py 
        módulo onde é gerado as variáveis da biblioteca do sqlalchemy

    5- models.py 
        módulo onde definimos os modelos para as tabelas do banco de dados mysql

    6- create_db.py
        módulo onde foi gerado as tabelas de devices e locations para o uso da API

B - Como usar:

    1- Este projeto foi gerado dentro de uma virtual env do python, logo, para rodar é necessário rodar o comando: pipenv shell

    2- Para levantar a API é necessário levantar o micro servidor da biblioteca uvicorn. Para isso, basta executar o comando: uvicorn main:app --port 8080 --reload

    3- Assim, para acessar a API basta clicar no link gerado e mostrado pelo uvicorn, ou assessar em: http://localhost:8080
