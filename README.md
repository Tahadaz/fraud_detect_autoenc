# Détection de Fraude par Autoencodeur

Ce projet implémente un système de détection de transactions bancaires frauduleuses utilisant un autoencodeur entraîné sur des données de transactions normales. Le modèle apprend à reconstruire les transactions légitimes et détecte les anomalies par une erreur de reconstruction élevée.

---

## Fonctionnalités principales

- Modèle autoencodeur symétrique entraîné uniquement sur les transactions non frauduleuses
- Calcul d’un score d’anomalie basé sur l’erreur moyenne absolue de reconstruction (MAE)
- Interface web Flask pour tester les transactions en temps réel
- Déploiement Dockerisé prêt pour production
- Calcul et calibration automatique d’un seuil de détection basé sur la distribution des erreurs

---

## Structure du projet

```├── aut.py # API Flask avec logique de prédiction
```├── requirements.txt # Dépendances Python
```├── Dockerfile # Containerisation du projet
```├── templates/ # Pages HTML (index, présentation, etc.)
```├── static/ # Fichiers statiques (CSS, images)
```├── model_config.json # Configuration du modèle Keras
```├── anomaly.weights.h5 # Poids du modèle autoencodeur
```├── scaler.pkl # Scaler pour la normalisation des features
```└── README.md # Ce fichier



## Installation et utilisation

### Prérequis

- Python 3.10+
- Docker (optionnel mais recommandé)
- Pipenv ou virtualenv pour isoler l’environnement Python

### Installation locale

```bash
# git clone https://github.com/Tahadaz/fraud_detect_autoenc.git
cd fraud_detect_autoenc
pip install -r requirements.txt
python aut.py
Le serveur Flask démarre sur http://localhost:8080.

Utilisation avec Docker
docker build -t fraud-app .
docker run -p 8080:8080 fraud-app
Description technique
Modèle : autoencodeur dense symétrique 7→64→16→6→16→64→7, activations ReLU sauf dernière couche linéaire.

Données : 7 features (3 numériques + 4 binaires) extraites et normalisées.

Seuil d’anomalie : fixé au 95e percentile de l’erreur MAE sur transactions normales (~0.543).

Prédiction : une transaction est signalée comme frauduleuse si l’erreur dépasse ce seuil.

Interface : formulaire web pour saisir les données d’une transaction et afficher le résultat.

Résultats
Rappel (Recall) : 85%

Précision (Precision) : 37%

F1-score : 0.52

Accuracy : 86%

Ces résultats représentent un bon compromis pour un système de filtrage de premier niveau.

Auteurs & Encadrement
Ce projet a été réalisé par :

Dazine Ahmed Taha

Wahidi Mouad

Ouhannou Anouar

Mohamed Said Adiouane

Sous l’encadrement de Monsieur Youssef Lamrani, dans le cadre d’un projet à l’École Mohammadia d’Ingénieurs (EMI).

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Remarques
Pensez à adapter le fichier scaler.pkl et les poids anomaly.weights.h5 si vous réentraîner le modèle.

Le seuil d’anomalie (THRESHOLD) est modifiable dans aut.py pour ajuster la sensibilité du détecteur.
