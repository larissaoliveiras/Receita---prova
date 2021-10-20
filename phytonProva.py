from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

receita = [
{
    'Titulo': "Brigadeiro",
    'Ingredientes':[
        " 395ml de Leite condensado",
        " 200ml Creme de leite",
        "50g gramas de cacau em pó",

    ],
    'modo de preparo': " Misturar todos os ingredientes e levar ao fogo médio por 10 minutos "
}
]

class Recs(Resource):
    def get(self):
        return {'status': 200, 'data': receita}

    def post(self):
        newRec = json.loads(request.data)
        receita.append(newRec)
        return {
            "message": "Updated!",
            "new": newRec
        }

class Rec(Resource):
    def get(self, indice):
        try:
            return receita[indice]
        except IndexError:
            messagem = "Indice {} não encontrado!".format(indice)
            return {"status": "Erro de índice!" 
                          "mensage"


                    }

        except:

            messagem = "Erro desconhecido"
            return {
                "status": "Erro de índice",
                "mensage": messagem,
            }


    def put(self, indice):
        newValue = json.loads(request.data)
        receita[indice] = newValue
        return {
            "message": "Updated!",
            "new": newValue
        }

    def delete(self, indice):
        receita.pop(indice)
        return {
            "message": "Deleted!",
            "Lista de Receitas": receita
        }


api.add_resource(Recs,'/recs/')
api.add_resource(Rec,'/recs/<int:indice>')

if __name__ == '__main__':
    app.run(debug=True)
