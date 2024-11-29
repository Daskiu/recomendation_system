import pandas as pd
from flask import Flask, request, jsonify

#Iniciar la app Flask
app = Flask(__name__)

#Importar los datos
books_data = pd.read_csv("books.csv")
users_data = pd.read_csv("./static/users.csv")

def recommended_books(user_row, books_data, user_data, method="average"):
    try:
        # Asegurarse de que las columnas son listas y no cadenas
        preferred_genres = user_row["preferred_genres"].split(',') if isinstance(user_row["preferred_genres"], str) else user_row["preferred_genres"]

        # Filtrar libros que coincidan con los géneros preferidos
        filtered_songs = books_data[
            (books_data["Genre"].isin(preferred_genres))
        ].copy()

#Endpoint para obtener los usuarios
@app.route('/users', methods=['GET'])
def get_users():
    #Cargar a los usuarios desde el CSV
    users_df = pd.read_csv("users.csv")
    #Convertir en lista de diccionario
    users = users_df[["user_id"]].to_dict(orient="records")
    return jsonify(users)

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get("user_id")
    method = request.args.get("method", "average")

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    try:
        user_row = users_data[users_data["user_id"] == user_id]
        if user_row.empty:
            return jsonify({"error": "user not found"}), 404
        
        user_row = user_row.iloc[0]
        recommendations = recommend_books(user_row, books_data, users_data, method=method)

        return jsonify(recommendations)
    except Exception as e:
        print(f"Error en /recommended: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)