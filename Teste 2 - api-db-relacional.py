from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Conexão com o banco de dados do PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="uniqcars",
    user="postgres",
    password="123456"
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros (
        id SERIAL PRIMARY KEY,
        modelo TEXT,
        ano INTEGER,
        novo BOOLEAN
    )
''')
conn.commit()

# Função GET
@app.route('/cars', methods=['GET'])
def get_carros():
    cursor.execute('SELECT * FROM carros')
    carros = cursor.fetchall()
    return jsonify(carros)

# Função POST
@app.route('/cars', methods=['POST'])
def add_carro():
    data = request.json
    id = data['id']
    modelo = data['modelo']
    ano = data['ano']
    novo = data['novo']
    cursor.execute('INSERT INTO carros (id, modelo, ano, novo) VALUES (%s, %s, %s, %s)', (id, modelo, ano, novo))
    conn.commit()
    return 'Carro adicionado com sucesso'

# Função PUT
@app.route('/cars/<int:id>', methods=['PUT'])
def update_carro(id):
    data = request.json
    modelo = data['modelo']
    ano = data['ano']
    novo = data['novo']
    cursor.execute('UPDATE carros SET modelo=%s, ano=%s, novo=%s WHERE id=%s', (modelo, ano, novo, id))
    conn.commit()
    return 'Carro atualizado com sucesso'

# Função DELETE
@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_carro(id):
    cursor.execute('DELETE FROM carros WHERE id=%s', (id,))
    conn.commit()
    return 'Carro excluído com sucesso'

if __name__ == '__main__':
    app.run(debug=True)