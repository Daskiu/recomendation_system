import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

#Iniciar la app Flask
app = Flask(__name__)
CORS(app)

@app.route('/nuevo_usuario', methods=['POST'])
def nuevo_usuario():
        # Get the data from the POST endpoint
    data = request.get_json()
    global user
    user = data
    if not data:
        resp = (jsonify({'error': 'No data provided'}), 400)
        return resp
    print("USUARIO ACTUAL \n", user['answer'])
    resp = (jsonify({"Access-Control-Allow-Origin": "*",'response': data}), 201, {'Access-Control-Allow-Origin': '*'})
    print(resp)

    return resp


@app.route('/recommend', methods=['GET'])
def recommend():
    books_data = pd.read_csv("books.csv")
    users_data = pd.read_csv("./static/users.csv")

    books_data_copy = books_data
    users_data_copy = users_data
    user_copy = user

    print("BOOKS COLUMNA")
    books_raw_1 = books_data_copy.loc[books_data_copy['Genre'] == 
    user_copy["answer"]["genero_usuario_1"]]
    books_recommend_1 = books_raw_1.filter(items=['Title'])

    books_raw_2 = books_data_copy.loc[books_data_copy['Genre'] == 
    user_copy["answer"]["genero_usuario_2"]]
    books_recommend_2 = books_raw_2.filter(items=['Title'])

    books_recomendados = pd.concat([books_recommend_1, books_recommend_2])
    print(books_recomendados)
    
    print()


    print("BOOKS RECOMMEND")
    resp = (jsonify({"msg": [list(books_recommend_1['Title']), 
    list(books_recommend_2['Title'])]}))
    print(resp)

    return resp


if __name__ == '__main__':
    app.run(debug=True)