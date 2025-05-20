# ─────────────────────────────────────────────
#  Dockerfile – Fraud Detect Autoencoder
# ─────────────────────────────────────────────
FROM python:3.10-slim

# 1. Répertoire de travail
WORKDIR /app

# 2. Copie des dépendances Python et installation
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 3. Copie du reste du code et des fichiers statiques
COPY . .

# 4. Variables d’environnement Flask
ENV FLASK_APP=aut.py
ENV FLASK_RUN_PORT=8080

EXPOSE 8080

# 5. Lancement de l’application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
