Teste enviado por [Lucas Zago](https://github.com/luc-zago)

## Objetivo

Desenvolver um serviço de captura/coleta de dados e persistência em um banco de dados.

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
    - Como documentar por comentários?
    
- Possivelmente mais higiene nos dados.
- Calculadora de performance.

## Para rodar:

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
