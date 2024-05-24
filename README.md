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
#### A API deve estar ativa antes de rodar esta aplicação Xlsx_Extractor. Quando a aplicação está funcionando normalmente, cada registro de funcionário coletado da planilha e enviado para a API será exibido no terminal junto com o código de status retornado.

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
