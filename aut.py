# app.py

import streamlit as st
import numpy as np
import pandas as pd
from keras.models import model_from_json
from sklearn.preprocessing import StandardScaler
import joblib

# Charger modèle
with open("model_config.json", "r") as json_file:
    model_json = json_file.read()
autoencoder = model_from_json(model_json)
autoencoder.load_weights("anomaly.weights.h5")
autoencoder.compile(optimizer="adam", loss="mae")

# Charger scaler
scaler = joblib.load("scaler.pkl")

# Titre
st.title("Détection de Fraude avec Autoencoder")

# Choix de méthode d'entrée
option = st.radio("Entrée :", ("Une seule transaction", "Téléverser un CSV"))

if option == "Une seule transaction":
    # Entrée manuelle
    input_values = []
    for i in range(autoencoder.input_shape[1]):
        val = st.number_input(f"Feature {i+1}", step=0.01)
        input_values.append(val)

    if st.button("Prédire"):
        x = np.array(input_values).reshape(1, -1)
        x_scaled = scaler.transform(x)
        recon = autoencoder.predict(x_scaled)
        error = np.mean(np.abs(x_scaled - recon))

        threshold = 0.01  # ⚠️ à ajuster selon ton tuning
        if error > threshold:
            st.error(f"❗ Anomalie détectée (erreur = {error:.5f})")
        else:
            st.success(f"✅ Transaction normale (erreur = {error:.5f})")

else:
    # Upload CSV
    file = st.file_uploader("Téléverser un fichier CSV")
    if file:
        df = pd.read_csv(file)
        x_scaled = scaler.transform(df)
        recon = autoencoder.predict(x_scaled)
        errors = np.mean(np.abs(x_scaled - recon), axis=1)

        threshold = 0.01  # à ajuster
        anomalies = errors > threshold

        result_df = df.copy()
        result_df["Reconstruction_Error"] = errors
        result_df["Anomaly"] = anomalies

        st.write(result_df)
        st.write(f"Nombre d’anomalies détectées : {np.sum(anomalies)}")
