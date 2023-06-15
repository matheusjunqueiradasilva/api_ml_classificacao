from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle


class Ml_def:
    def __init__(self):
        self.iris = load_iris()
        self.var_x = self.iris.data
        self.var_target = self.iris.target

    def train(self):
        self.var_x_treino, self.var_x_teste, self.var_y_treino, self.var_y_teste = train_test_split(
            self.var_x, self.var_target, test_size=0.2)

    def classifier(self):
        self.train()
        self.clf = RandomForestClassifier(n_estimators=15)
        self.clf.fit(self.var_x_treino, self.var_y_treino)
        self.prev = self.clf.predict(self.var_x_teste)
        print(accuracy_score(self.var_y_teste, self.prev))

    def save_model(self):
        self.classifier()
        with open('modelo/treino.pkl', 'wb', ) as mdl:
            pickle.dump(self.clf, mdl)


Ml_def().save_model()
