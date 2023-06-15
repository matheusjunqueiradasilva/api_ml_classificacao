import pickle
import numpy as np
from fastapi import FastAPI, Request


class ModelLoader:
    def __init__(self, path):
        self.path = path
        self.model = self.load_model()

    def load_model(self):
        with open(self.path, 'rb') as file:
            model = pickle.load(file)
        return model


class Predictor:
    def __init__(self, model):
        self.model = model

    def predict(self, features):
        prediction = self.model.predict(np.array([features]))
        return str(prediction)


description = "Resumo: O código apresenta um exemplo de treinamento de um modelo de classificação utilizando o algoritmo Random Forest. Ele carrega o conjunto de dados Iris, divide-o em conjuntos de treinamento e teste, e treina um modelo Random Forest com 15 estimadores. Em seguida, realiza a classificação dos dados de teste e calcula a acurácia do modelo. Por fim, o modelo treinado é salvo em um arquivo pickle para uso futuro. O código demonstra o uso das bibliotecas scikit-learn e pickle para treinar e persistir o modelo de classificação. abaixo a documentação da api para"
core = FastAPI(
    title="Treinamento e salvamento de um modelo de classificação usando Random Forest",
    description=description,
    version="0.0.1",
    contact={
        "name": "Matheus J ",
        "email": "matheusjunqueira.job@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
model = ModelLoader('modelo/treino.pkl').model
predictor = Predictor(model)


@core.post('/predicao')
async def predict(request: Request):
    """
    O conjunto de dados Iris é um conjunto de dados muito conhecido na área de aprendizado de máquina e é comumente usado como exemplo para classificação. Ele contém informações sobre as medidas das pétalas e sépalas de três espécies de flores Iris (Setosa, Versicolor e Virginica)
    parâmetros necessários para fazer a previsão são s_length, s_width, p_length e p_width, que representam as medidas das sépalas e pétalas da flor Iris.

    
<h2>Obter a previsão do modelo</h2>

<h3> HTTP Request<h2>

<code>POST http://127.0.0.1:8000/predicao</code>

<h3 >Payload</h3>
<p>
<h4> Exemplo: </h4>
<code> {
    "s_length": 5.1,
    "s_width": 3.5,
    "p_length": 1.4,
    "p_width": 0.2
} </code>

<p>
<h4> response: </h4>
<code> {
   "[0]"
} </code>



<h3>Headers</h3>
<table><thead>
<tr>
<th>Header</th>
<th>Obrigatório</th>
<th>Descrição</th>
</tr>
</thead><tbody>
<tr>
<td>token</td>
<td>nao</td>
<td>não necessario</td>
</tr>
</tbody></table>



    """
    request_data = await request.json()
    features = [
        request_data["s_length"],
        request_data["s_width"],
        request_data["p_length"],
        request_data["p_width"]
    ]

    prediction = predictor.predict(features)
    return prediction
