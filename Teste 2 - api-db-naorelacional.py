from flask import Flask, request
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps

app = Flask(__name__)

# Conexão com o banco de dados do MongoDB
client = MongoClient('localhost', 27017)
db = client['uniqcars']
collection = db['carros']

# Função GET
@app.route('/cars', methods=['GET'])
def get_carros():
    carros = list(collection.find())
    # Converter ObjectId para string antes de serializar para JSON
    carros_serializaveis = dumps(carros)
    return carros_serializaveis

# Função POST
@app.route('/cars', methods=['POST'])
def add_carro():
    data = request.json
    collection.insert_one(data)
    return 'Carro adicionado com sucesso'

# Função PUT
@app.route('/cars/<string:id>', methods=['PUT'])
def update_carro(id):
    data = request.json
    car_id = ObjectId(id)
    collection.update_one({'_id': car_id}, {'$set': data})
    print(id)
    return 'Carro atualizado com sucesso'

# Função DELETE
@app.route('/cars/<string:id>', methods=['DELETE'])
def delete_carro(id):
    car_id = ObjectId(id)
    collection.delete_one({'_id': car_id}) 
    return 'Carro excluído com sucesso'

if __name__ == '__main__':
    app.run(debug=True)