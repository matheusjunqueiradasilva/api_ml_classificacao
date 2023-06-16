
<h1>Treinamento e salvamento de um modelo de classificação usando Random Forest</h1>

Esta API implementa um exemplo de treinamento de um modelo de classificação usando o algoritmo Random Forest. O modelo é treinado com base no conjunto de dados Iris, que contém informações sobre as medidas das pétalas e sépalas de três espécies de flores Iris (Setosa, Versicolor e Virginica). Após o treinamento, o modelo é capaz de realizar previsões sobre novos dados.
<p>
 
<h2> Como Usar</h2>
<p>
1. Primeiro clone o repositório.
<p>
2.  instale a versão do Python de acordo com o arquivo python-version.
<p>
3. Crie a virtuaenv e inicie ela.
<p>
4. No terminal apontando pra a pasta do requirements.txt rode o seguinte comando: <code>Pip install -r requirements.txt </code> para instlar as dependencias.
<p>
5. Rode o servidor do uvicorn com o seguinte comando: <code>uvicorn core:core --reload</code>

Versão
0.0.1

Documentação da API
A documentação a seguir descreve os endpoints disponíveis na API.

Predict
Endpoint para fazer previsões usando o modelo treinado.

Método: POST

Endpoint: ``localhost:8000/predicao``

<h3>Parâmetros</h3>
Os seguintes parâmetros são necessários para fazer a previsão:

s_length: comprimento da sépala da flor Iris.
s_width: largura da sépala da flor Iris.
p_length: comprimento da pétala da flor Iris.
p_width: largura da pétala da flor Iris.
## Exemplo de payload
<h3> Json</h3>
<h4>Copy code:</h4><code>{
  "s_length": 5.1,
  "s_width": 3.5,
  "p_length": 1.4,
  "p_width": 0.2
}</code>

## Exemplo de resposta
<h3>Json</h3>
<h4>Copy code:</h4> <code>{
  "prediction": "[0]"
}</code>

<h2>Cabeçalhos</h3>
O cabeçalho token não é necessário para esta solicitação.
<h3>Respostas</h3>
200: Resposta bem-sucedida.
A previsão é retornada no corpo da resposta.
