# Xlsx_Extractor_API

#### O projeto Xlsx_Extractor_API é uma aplicação desenvolvida em Django que realiza a integração de funcionários aos planos de saúde requisitados.
---
### Instalando dependências 

Após extrair o .zip do projeto e acessar a pasta Xlsx_Extractor é necessário:

* Criar um ambiente virtual (venv) - ``` python3 -m venv venv```
* Acessar o ambiente virtual ( linux / windows )
  
   ``` source venv/bin/activate ```
  
   ``` source venv/scripts/activate ```

* Instalar as dependências - ``` pip install -r requirements.txt"  ```
  
* Aplicar migrations ```python3 manage.py migrate```
* Rodar o projeto - ``` python3 manage.py runserver ```


---
## **Características da vida**


| Campo      | Tipo   | Descrição                                        |
| -----------|--------|--------------------------------------------------|
| id         | uuid   | Identificador único de vida.                      |
| cpf        | string | cpf da vida.                                      |
| nome       | string | O nome da vida.                                  |
| idade      | number | Idade da vida.                                    |
| sexo       | choicefield | sexo da vida ( Masculino, Feminino, Not Inf)|
| cargo      | string | cargo da vida.                                   |
| data_da_criacao | DateTimeField | Data de inclusão no sistema. |
| integracao | choicefield | Status de integração (Pendente, Integrado, Revisar |



## **Características de Plano**


| Campo      | Tipo   | Descrição                                        |
| -----------|--------|--------------------------------------------------|
| id         | long/number | Identificador único de plano.   |
| nome       | string | O nome do plano.                                |
| servicos   | textfield| área para descrição do plano.|
| valor      | number | Valor do plano.|
| dependentes| number | Numero de depentes que o plano cobre.|


---
### Endpoints
#### based_url = http://localhost:8000/api

#### Vida

| Método   | Rota                   | Descrição                                       |
|----------|------------------------|-----------------------------------------------|
| POST     | /vidas               | Criação de uma vida.                          |
| GET      | /vidas               | Lista todas as vidas.                        |
| GET      | /vida/:vida_id | busca uma vida usando seu ID como parâmetro. |
| PATCH    | /vida/:vida_id   | Atualiza uma vida usando seu ID como parâmetro.|
| DELETE   | /vida/:vida_id   | Deleta uma vida usando seu ID como parâmetro.   |  

#### Plano

| Método   | Rota                   | Descrição                                       |
|----------|------------------------|-----------------------------------------------|
| POST     | /planos               | Criação de uma plano.                          |
| GET      | /planos               | Lista todos os planos.                        |
| GET      | /plano/:plano_id | busca um plano usando seu ID como parâmetro. |
| PATCH    | /plano/:plano_id   | Atualiza um plano usando seu ID como parâmetro.|
| DELETE   | /plano/:plano_id   | Deleta um plano usando seu ID como parâmetro.   |  


---
### Vidas

### 1 - **Criação de Vida**

### `/vidas`

### Exemplo de Request:
```
POST /vidas
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
{
	"cpf": "00011122244",
	"nome": "Ana Maria",
	"idade": 20,
	"planos": [1], 
	"cargo": "Recepcista", <-- não obrigatório
	"sexo": "Feminino" <-- não obrigatório
}
```

### Validação:
```
    cpf: string (max 11),
	nome: string,
	idade: number,
	planos: [number], 
	cargo: string, <-- não obrigatório
	sexo: string OPTIONS - Masculino, Feminino <-- não obrigatório (not informed)
```
OBS.: Chaves não presentes no schema serão removidas.

### Exemplo de Response:
```
201 Created
```

```json
{
	"id": "dc69700a-8e3b-46a1-87c9-ad64fa8ccd15",
	"planos": [
		1
	],
	"cpf": "00011122244",
	"nome": "Ana Maria",
	"idade": 20,
	"sexo": "Feminino",
	"cargo": "Recepcista",
	"data_de_criacao": "2024-04-12T00:15:52.647560Z",
	"integracao": "Pendente"
}
```

### Possíveis Erros:
| Código do Erro |                 Descrição                   |
|----------------|---------------------------------------------|
| 400 BAD REQUEST   | "message": "X field is required" |

---


### 2 - **Lista de Vidas**

### `/vidas`

### Exemplo de Request:
```
GET /vidas
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
200 OK
```
```json
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": "6b67d98c-7928-4aaf-9b11-ebb56581820e",
			"planos": [
				1
			],
			"cpf": "03045933384",
			"nome": "Josué Amaral",
			"idade": 23,
			"sexo": "Masculino",
			"cargo": "Operador De Empilhadeira",
			"data_de_criacao": "2024-04-12T00:15:19.243293Z",
			"integracao": "Pendente"
		},
		{
			"id": "dc69700a-8e3b-46a1-87c9-ad64fa8ccd15",
			"planos": [
				1
			],
			"cpf": "00011122244",
			"nome": "Ana Maria",
			"idade": 20,
			"sexo": "Feminino",
			"cargo": "Recepcista",
			"data_de_criacao": "2024-04-12T00:15:52.647560Z",
			"integracao": "Pendente"
		}
	]
}

```

### Possíveis Erros:
Nenhum, o máximo que pode acontecer é a lista estar vazia.

---

### 3 - **Buscando uma vida**

### `/vida/uuid`

### Exemplo de Request:
```
GET /vida/05e5369f-b22e-4f21-8bcb-a45580178cf7
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
200 OK
```
```json
{
	"id": "82dfde58-f904-419d-8a26-19b9d23f4f4b",
	"planos": [
		1
	],
	"cpf": "00011122244",
	"nome": "Ana Maria",
	"idade": 20,
	"sexo": "Feminino",
	"cargo": "Recepcista",
	"data_de_criacao": "2024-04-12T16:17:36.931046Z",
	"integracao": "Pendente"
}
```

### Possíveis Erros:
| Código do Erro |                   Descrição                   |
|----------------|-----------------------------------------------|
| 404 NOT FOUND  | "detail": "No Vida matches the given query."  |



OBS.: Chaves não presentes no schema serão removidas.

---

### 4 - **Atualização de vida**

### `/vida`

### Exemplo de Request:
```
PATCH /vida/uuid
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
{
	"cpf": "03045933384",
	"nome": "Josué Amaral",
	"idade": 23,
	"planos": [1],
	"cargo": "Operador De Empilhadeira",
	"sexo": "Masculino",
	"integracao": "Revisar"
}
```

### Validação:
```
	cpf: string (max 11),
	nome: string,
	idade: number,
	planos: [number],
	cargo: string,
	sexo: string OPTIONS - Masculino, Feminino
	integracao: string OPTIONS Revisar

```
OBS.: Chaves não presentes no schema serão removidas.


### Exemplo de Response:
```
200 OK
```

```json
{
	"id": "05e5369f-b22e-4f21-8bcb-a45580178cf7",
	"planos": [
		1
	],
	"cpf": "03045933384",
	"nome": "Josué Amaral",
	"idade": 23,
	"sexo": "Masculino",
	"cargo": "Operador De Empilhadeira",
	"data_de_criacao": "2024-04-11T23:53:23.405242Z",
	"integracao": "Revisar"
}
```

### Possíveis Erros:
| Código do Erro |                 Descrição                     |
|----------------|-----------------------------------------------|
| 404 NOT FOUND  | "detail": "No Vida matches the given query."  |

---


### 5 - **Deletando uma vida**

### `/vida/uuid`

### Exemplo de Request:
```
DELETE /vida/05e5369f-b22e-4f21-8bcb-a45580178cf7
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
204 NO CONTENT
```
```json
NO BODY
```

### Possíveis Erros:
| Código do Erro |                   Descrição                   |
|----------------|-----------------------------------------------|
| 404 NOT FOUND  | "detail": "No Vida matches the given query."  |



OBS.: Chaves não presentes no schema serão removidas.

---

### Planos

### 1 - **Criação de plano**

### `/planos`

### Exemplo de Request:
```
POST /planos
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
{
	"nome": "Basic Care",
	"servicos": "Clinica geral e procedimento odontológicos",
	"valor": 39.90,
	"dependentes": 1
}
```

### Validação:
```
    nome: string,
    servicos: string,
    valor: float,
    dependentes: integer <-- não obrigatório ( 0 DEFAULT)
```
OBS.: Chaves não presentes no schema serão removidas.

### Exemplo de Response:
```
201 Created
```

```json
{
	"id": 1,
	"nome": "Basic Care",
	"servicos": "Clinica geral e procedimento odontológicos",
	"valor": "39.90",
	"dependentes": 1
}
```

### Possíveis Erros:
| Código do Erro  |                 Descrição                   |
|-----------------|---------------------------------------------|
| 400 Bad Request | " X field": "This field is required"        |

---



### 2 - **Lista de planos**

### `/planos`

### Exemplo de Request:
```
GET /planos
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
200 OK
```
```json
{
	"count": 3,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"nome": "Basic Care",
			"servicos": "Clinica geral e procedimento odontológicos",
			"valor": "39.90",
			"dependentes": 0
		},
		{
			"id": 2,
			"nome": "Basic Care",
			"servicos": "Clinica geral e procedimento odontológicos",
			"valor": "39.90",
			"dependentes": 1
		},
		{
			"id": 4,
			"nome": "Basic Care",
			"servicos": "Clinica geral e procedimento odontológicos",
			"valor": "39.90",
			"dependentes": 1
		}
	]
}
```

### Possíveis Erros:
Nenhum, o máximo que pode acontecer é a lista estar vazia.

---

### 3 - **Buscando um plano**

### `/plano/id`

### Exemplo de Request:
```
GET /plano/1
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
200 OK
```
```json
{
	"id": 1,
	"nome": "Basic Care",
	"servicos": "Clinica geral e procedimento odontológicos",
	"valor": "39.90",
	"dependentes": 0
}
```

### Possíveis Erros:
| Código do Erro |                   Descrição                   |
|----------------|-----------------------------------------------|
| 404 NOT FOUND  | "detail": "No plano matches the given query."  |



OBS.: Chaves não presentes no schema serão remoplanos.

### 4 - **Atualização de plano**

### `/plano/id`

### Exemplo de Request:
```
PATCH /plano/4
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
{
	"nome": "Basic Care 2",
	"servicos": "Clinica geral ",
	"valor": 39.90
}
```

### Validação:
```
    nome: string,
    servicos: string,
    valor: float,
    dependentes: number
```
OBS.: Chaves não presentes no schema serão removidos.


### Exemplo de Response:
```
200 OK
```

```json
{
	"id": 4,
	"nome": "Basic Care 2",
	"servicos": "Clinica geral",
	"valor": "39.90",
	"dependentes": 1
}
```

### Possíveis Erros:
| Código do Erro |                 Descrição                     |
|----------------|-----------------------------------------------|
| 404 NOT FOUND  | "detail": "No plano matches the given query."  |

---

### 5 - **Deletando um plano**

### `/plano/id`

### Exemplo de Request:
```
DELETE /plano/1
Host: localhost:8080
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
204 No Content
```
```json
Vazio
```

### Possíveis Erros:
| Código do Erro |                   Descrição                   |
|----------------|-----------------------------------------------|
| 404 NOT FOUND  | "detail": "No plano matches the given query."  |



OBS.: Chaves não presentes no schema serão remoplanos.

