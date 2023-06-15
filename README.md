# ml_api_classificacao

Treinamento e salvamento de um modelo de classificação usando Random Forest

Esta API implementa um exemplo de treinamento de um modelo de classificação usando o algoritmo Random Forest. O modelo é treinado com base no conjunto de dados Iris, que contém informações sobre as medidas das pétalas e sépalas de três espécies de flores Iris (Setosa, Versicolor e Virginica). Após o treinamento, o modelo é capaz de realizar previsões sobre novos dados.

Versão
0.0.1

Documentação da API
A documentação a seguir descreve os endpoints disponíveis na API.

Predict
Endpoint para fazer previsões usando o modelo treinado.

Método: POST

Endpoint: /predicao

Parâmetros
Os seguintes parâmetros são necessários para fazer a previsão:

s_length: comprimento da sépala da flor Iris.
s_width: largura da sépala da flor Iris.
p_length: comprimento da pétala da flor Iris.
p_width: largura da pétala da flor Iris.
Exemplo de payload
json
Copy code
{
  "s_length": 5.1,
  "s_width": 3.5,
  "p_length": 1.4,
  "p_width": 0.2
}
Exemplo de resposta
json
Copy code
{
  "prediction": "[0]"
}
Cabeçalhos
O cabeçalho token não é necessário para esta solicitação.

Respostas
200: Resposta bem-sucedida. A previsão é retornada no corpo da resposta.
Media type
application/json
Contato
Nome: Matheus J
Email: matheusjunqueira.job@gmail.com


Para fazer uma solicitação de previsão, você pode enviar uma solicitação POST para o endpoint /predicao, fornecendo os valores corretos para os parâmetros s_length, s_width, p_length e p_width. A resposta conterá a previsão feita pelo modelo.
 
