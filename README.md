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

Esse endpoint pega os sentimentos presentes na musica. Voce pode mandar a letra como no exemplo abaixo.

Exemplo de body:
```json
{
	"lyrics": "Pode ser mais simples\n Não tão complicado\nDe estarmos juntos\nE só ser amado\nE amar, amar\nSem querer o certo\nSem querer um lado\nDe estarmos perto e só ser amado\nE amar, amar\nDesde a primeira vez que te vi\nEu senti um chamado\nDe uma chama que ardeu\nE me deu um recado\nDe que eu podia te amar\nE por você ser amado\nCoisa mais simples\nNão tem que ser complicado\nSó ser amado e amar"
}
```

Exemplo de resposta de sucesso:
```json
{
	"data": [
		[
			"Pode ser mais simples",
			"satisfação"
		],
		[
			"Não tão complicado",
			"satisfação"
		],
		[
			"De estarmos juntos",
			"amor"
		],
		[
			"E só ser amado",
			"amor"
		],
		[
			"E amar, amar",
			"amor"
		],
		[
			"Sem querer o certo",
			"confiança"
		],
		[
			"Sem querer um lado",
			"confiança"
		],
		[
			"De estarmos perto e só ser amado",
			"amor"
		],
		[
			"E amar, amar",
			"amor"
		],
		[
			"Desde a primeira vez que te vi",
			"alegria"
		],
		[
			"Eu senti um chamado",
			"medo"
		],
		[
			"De uma chama que ardeu",
			"amor"
		],
		[
			"E me deu um recado",
			"confiança"
		],
		[
			"De que eu podia te amar",
			"amor"
		],
		[
			"E por você ser amado",
			"amor"
		],
		[
			"Coisa mais simples",
			"satisfação"
		],
		[
			"Não tem que ser complicado",
			"satisfação"
		],
		[
			"Só ser amado e amar",
			"amor"
		]
	]
}
```

Ou você pode mandar o artista e a musica. Observe

Exemplo de body:
```json
{
	"artist": "pixote", "track": "insegurança"
}
```

Exemplo de resposta de sucesso:
```json
{
	"data": [
		[
			"Essa noite eu notei que você demorou pra dormir",
			"tristeza"
		],
		[
			"Caminhou pela casa, ligou a TV, eu ouvi",
			"medo"
		],
		[
			"Você sussurrando, chorando baixinho pra não me acordar",
			"tristeza"
		],
		[
			"Se estiver precisando de amigo pra desabafar",
			"confiança"
		],
		[
			"Se for alguma coisa comigo, vamos conversar",
			"confiança"
		],
		[
			"Eu não quero correr o perigo de um dia você me deixar",
			"medo"
		],
		[
			"Escolhi você pra ser minha mulher",
			"amor"
		],
		[
			"E sou tão fiel à nossa relação",
			"satisfação"
		],
		[
			"Pelo amor de deus, se for insegurança, tira do teu coração",
			"confiança"
		],
		[
			"Já é tarde, vamos nos deitar",
			"satisfação"
		],
		[
			"Se quiser conversar na nossa cama",
			"confiança"
		],
		[
			"Porque sei que tudo isso passa",
			"confiança"
		],
		[
			"Você me abraça e a gente se ama",
			"amor"
		],
		[
			"Eu não vou te trair com ninguém",
			"confiança"
		]
	]
}
```