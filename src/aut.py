"""
Back‑end Flask pour l’application Fraud Detector.
Routes :
    /            → page d’accueil
    /analyse     → formulaire + résultat
    /presentation, /about
"""
from flask import Flask, render_template, request
import numpy as np, pandas as pd, joblib, os
from keras.models import model_from_json

# ─────────── Chargement du modèle et du scaler
with open("model_config.json") as f:
    model = model_from_json(f.read())
model.load_weights("anomaly.weights.h5")
scaler = joblib.load("scaler.pkl")

# ─────────── Constantes
FEATURE_NAMES = [
    "distance_from_home", "distance_from_last_transaction",
    "ratio_to_median_purchase_price", "repeat_retailer",
    "used_chip", "used_pin_number", "online_order"
]
NUM_COLS, CAT_COLS = FEATURE_NAMES[:3], FEATURE_NAMES[3:]
THRESHOLD = 0.297596          # seuil d’erreur → fraude

# ─────────── App
app = Flask(__name__)

# ══════════════ ROUTES ════════════════════════════════════════
@app.route("/")
def home():
    """Page d’accueil avec boutons de navigation"""
    return render_template("home.html")

@app.route("/analyse", methods=["GET", "POST"])
def analyse():
    """Formulaire de transaction et détection de fraude"""
    result = None
    if request.method == "POST":
        try:
            # 1) récupération des 7 valeurs
            vals = [float(request.form.get(f"feature{i+1}")) for i in range(7)]

            # 2) préparation
            df = pd.DataFrame([vals], columns=FEATURE_NAMES)
            scaled = scaler.transform(df[NUM_COLS])
            X = np.concatenate([scaled, df[CAT_COLS].values], axis=1)

            # 3) reconstruction
            recon = model.predict(X, verbose=0)
            err = float(np.mean(np.abs(X - recon)))

            # 4) score et niveau de risque
            score = err / THRESHOLD
            level, color = (
                ("faible", "success") if score < 1
                else ("moyen", "warning") if score < 3
                else ("élevé", "danger")
            )

            result = {
                "error": round(err, 5),
                "score": round(score, 2),
                "level": level,
                "color": color,
                "fraud": err > THRESHOLD
            }
        except Exception as e:
            result = {"error": str(e), "fraud": None}

    return render_template("index.html", result=result)

@app.route("/presentation")
def presentation():
    return render_template("presentation.html")

@app.route("/about")
def about():
    return render_template("about.html")

# ─────────── Lancement
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
