Teste enviado por [Lucas Zago](https://github.com/luc-zago)

## Objetivo

Desenvolver um serviço de captura/coleta de dados e persistência em um banco de dados.

- Este serviço deve persistir todos os dados dos aprovados (nome, CPF e score) em um banco SQL
- Os dados devem estar normalizados no banco de dados
- Os dados no banco de dados devem estar higienizados (sem acento ou caracteres especiais, maiúscula, etc.)
- Os CPFs persistidos devem ser CPFs válidos
- A utilização deve rodar através de containers (docker)
- O código deve estar disponível em um repositório público do git

## Sobre o resultado:
- São 46706 candidatos?
- Levou 28 minutos para raspar os dados e colocar no MySQL

## Maiores desafios e aprendizados:

- Usar o Docker + Docker Compose
- Usar o Docker + SQL
- Usar o Docker + SQL + Scrapy
- Usar o Docker + SQL + Scrapy + Flask
- Relembrar Python


## Melhorias futuras:
- Arquitetura: folders, ordenação de importações, divisão de domínios

- Uso de classes

- SQL: 
    - Conseguir colocar o score como FLOAT ou DECIMAL

- Testes:
    - Scraper
    - Rotas
    - DB

- Ser + Pythonico:
    - Como documentar melhor por comentários?
    
- Possivelmente mais higiene nos dados.


## Para rodar:

### Variáveis de ambiente
- Crie um arquivo **.env** na raíz do projeto
- Adicione estas variáveis:
 `HOST="mysqldb"
   USER="seu-user"
   PASSWORD="seu-password"`

### Dockerize
`sudo docker-compose -f docker-compose.dev.yml up --build`

### Crie o banco
`curl http://localhost:8000/create-db`

### Raspe os dados
`curl http://localhost:8000/start-scraping`

### Verifique o crescimento da tabela de dados




`curl http://localhost:8000/candidates`

### Pare os containers
`sudo docker-compose -f docker-compose.dev.yml down`

## Screencast
https://user-images.githubusercontent.com/37453518/154139727-3a6b6147-d287-414e-b395-1a9386bb0746.mp4
