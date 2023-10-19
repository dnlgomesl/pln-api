# PLN API
## Como executar a API?

1. Faça o clone deste repositório para o seu ambiente local.

```bash
git https://github.com/dnlgomesl/rate-movies-api.git
```

2. Navegue até o diretório do projeto.

```bash
cd pln-api
```
3. Instale o Docker e o docker-compose.

Siga o tutorial do próprio Docker que está nesse [link](https://docs.docker.com/get-docker/).

4. Copie as variáveis de ambiente e coloque sua key da api do openai.

```bash
cp .env-example .env
```

5. Após instalar o Docker faça o build.

```bash
docker-compose up --build
```

## Endpoints da API

### Status
Endpoint: GET /status/

Esse endpoint retorna o status da api.

Exemplo de resposta:

```json
{
"status": "online",
"timestamp": 1690268056,
"started": 1690268052,
"service": "api",
"version": "1.0"
}
```
### Sentiment
Endpoint: POST /sentiment/

Esse endpoint cria um filme.

Exemplo de body:
```json
{
	"lyrics": "Pode ser mais simples\n Não tão complicado\nDe estarmos juntos\nE só ser amado\nE amar, amar\nSem querer o certo\nSem querer um lado\nDe estarmos perto e só ser amado\nE amar, amar\nDesde a primeira vez que te vi\nEu senti um chamado\nDe uma chama que ardeu\nE me deu um recado\nDe que eu podia te amar\nE por você ser amado\nCoisa mais simples\nNão tem que ser complicado\nSó ser amado e amar"
}
```
Todos os itens são obrigatórios, é retornado erro se faltar algum.

Exemplo de resposta de sucesso:
```json
{
	"html": "<html>\n  <p id=\"alegria\">Não tão complicado</p>\n  <p id=\"satisfação\">De estarmos juntos</p>\n  <p id=\"amor\">E só ser amado</p>\n  <p id=\"amor\">E amar, amar</p>\n  <p id=\"alegria\">Sem querer o certo</p>\n  <p id=\"alegria\">Sem querer um lado</p>\n  <p id=\"satisfação\">De estarmos perto e só ser amado</p>\n  <p id=\"amor\">E amar, amar</p>\n  <p id=\"amor\">Desde a primeira vez que te vi</p>\n  <p id=\"amor\">Eu senti um chamado</p>\n  <p id=\"amor\">De uma chama que ardeu</p>\n  <p id=\"confiança\">E me deu um recado</p>\n  <p id=\"amor\">De que eu podia te amar</p>\n  <p id=\"amor\">E por você ser amado</p>\n  <p id=\"alegria\">Coisa mais simples</p>\n  <p id=\"alegria\">Não tem que ser complicado</p>\n  <p id=\"amor\">Só ser amado e amar</p>\n</html>"
}
```
