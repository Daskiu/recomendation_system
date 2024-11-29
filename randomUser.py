import pandas as pd
import random

#Géneros literarios para generar los usuarios aleatorios
genres = ["signal_processing", "data_science", "mathematics", "economics", "history", "science", "psychology", "fiction", "computer_science", "nonfiction", "philosophy", "comic"]

#Generar datos para 50 usuarios
users_data = {
    "user_id": [f"user_{i}" for i in range(1,51)], #Generar ID de los usuarios del 1 al 50
    "preferred_genres": ["," .join(random.sample(genres, k=2)) for _ in range(50)], #Genera 2 géneros preferidos por usuario
}

#Crear el DataFrame
users_df = pd.DataFrame(users_data)

#Guardar el DF como archivo CSV
users_df.to_csv("users.csv", index=False)

print("El csv 'users.csv' se creo con éxito")