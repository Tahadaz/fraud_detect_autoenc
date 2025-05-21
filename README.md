
# Détection de Transactions Frauduleuses par Autoencodeur

Ce projet met en œuvre une application web de détection de fraude bancaire basée sur un modèle d'autoencodeur non supervisé. Il a été réalisé dans le cadre d’un projet à l’École Mohammadia d’Ingénieurs (EMI), sous la supervision de Monsieur Youssef Lamrani, par :

- Dazine Ahmed Taha  
- Wahidi Mouad  
- Ouhannou Anouar  
- Mohamed Said Adiouane  

---

## 🔍 Objectif

L’objectif principal est de détecter automatiquement des transactions suspectes sans supervision, c’est-à-dire sans entraîner le modèle avec des exemples de fraude. Le modèle apprend uniquement à reconstruire des transactions normales, et identifie comme anomalies celles qu’il ne parvient pas à bien reconstruire.

---

## 🧠 Technologies utilisées

- **Python 3.10**
- **Keras / TensorFlow** pour le modèle autoencodeur
- **Scikit-learn** pour le prétraitement
- **Flask** pour l’interface web
- **Docker** pour le déploiement
- **Google Cloud Run** pour l’hébergement
- **HTML/CSS/JS** pour l’interface utilisateur

---

## 📁 Structure du projet

```
.
├── aut.py                 # Application Flask
├── requirements.txt       # Dépendances Python
├── Dockerfile             # Configuration Docker
├── model_config.json      # Architecture du modèle
├── anomaly.weights.h5     # Poids de l’autoencodeur entraîné
├── scaler.pkl             # Scaler des données
├── templates/             # Pages HTML (formulaire, présentation...)
├── static/                # CSS et images
└── README.md              # Ce fichier
```

---

## 🚀 Lancer le projet

### ▶️ En local

```bash
git clone https://github.com/Tahadaz/fraud_detect_autoenc.git
cd fraud_detect_autoenc
pip install -r requirements.txt
python aut.py
```
→ Accédez à l’app sur `http://localhost:8080`

### 🐳 Avec Docker

```bash
docker build -t fraud-app .
docker run -p 8080:8080 fraud-app
```

### 🌐 Version en ligne

Application déployée sur Google Cloud Run :  
👉 [fraud-app-xxxxx.a.run.app](https://fraud-app-xxxxx.a.run.app) *(à adapter)*

---

## ⚙️ Description du modèle

- Architecture : 7 → 64 → 16 → 6 → 16 → 64 → 7
- Fonction de perte : `Mean Absolute Error (MAE)`
- Seuil défini par calibration sur le 95e percentile des erreurs de reconstruction
- 7 features d’entrée (3 numériques, 4 binaires)

---

## 📊 Résultats

| Metric     | Score   |
|------------|---------|
| Recall     | 85 %    |
| Precision  | 37 %    |
| F1-Score   | 0.52    |
| Accuracy   | 86 %    |

> Ces résultats permettent un bon filtrage initial dans un système de détection en production.

---

## 📎 Livrables inclus

- Code source de l’application
- Dockerfile pour déploiement
- Modèle et scaler entraînés

---

## 📄 Licence

Projet sous licence MIT.

---

## 🙏 Remerciements

Encadré par Monsieur **Youssef Lamrani** dans le cadre d’un projet de fin d’année à l’**École Mohammadia d’Ingénieurs (EMI)**.
