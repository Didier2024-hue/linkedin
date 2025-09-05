# 🟩🟨🟥 Trustpilot - Analyse de la Satisfaction Client 🟥🟨🟩

Projet réalisé dans le cadre de la formation Data Engineer chez **DataScientest**.  
Il s'agit d'une application complète de **scraping**, **traitement**, **stockage** et **analyse** d'avis clients issus de **Trustpilot**.

---

## 🗂 Menu

1. [🎯 Objectifs du projet](#objectifs-du-projet)
2. [🚀 Processus en 3 Étapes](#processus-en-3-étapes)
3. [🛠️ Architecture technique](#architecture-technique)
4. [⚙️ Exécution des scripts](#exécution-des-scripts)
5. [📁 Organisation des répertoires](#organisation-des-répertoires)
6. [🧱 Schéma de base de données](#schéma-de-base-de-données)
7. [📊 Résultats](#résultats-obtenus)
8. [🌐 Extension via Wikipedia](#extension-du-projet--collecte-via-wikipedia)
9. [🌐 Suivi des modèles ML](#extension-du-projet--suivi-des-modèles-ml)
10. [🚀 Technologies utilisées](#technologies-utilisées)
11. [⚠️ Considérations éthiques](#limites-et-considérations-éthiques)
12. [⚡ Installation rapide](#installation-rapide)
13. [📄 Licence](#licence)
14. [👨‍💻 Auteur](#auteur)

---

## 🎯 Objectifs du projet
La **supply chain** représente les étapes d'approvisionnement, du processus productif et de distribution de la marchandise.  

En aval, il peut être intéressant d’évaluer la **satisfaction client** pour :  
- Étude de qualité sur la supply chain : conception, livraison, prix, durabilité…  
- Vérifier si le produit/service correspond aux attentes du marché  
- Synthétiser les feedbacks et suggestions d’amélioration  
- Aider à la réponse ou redirection des clients insatisfaits  

👉 La satisfaction des clients se mesure sur les **commentaires et avis** publiés sur des sites (**Trustpilot, distributeurs, Twitter, etc.**).

---

## 🚀 Processus en 3 Étapes

### 1️⃣ Collecte des données
- 🤖 Scraping automatisé des avis Trustpilot  
- 🌐 Collecte mensuelle via **Wikipedia API** (SIREN, CA, secteurs, etc.)  
- 🛡️ Respect des fichiers `robots.txt` et stratégie de scraping historique  

### 2️⃣ Stockage et structuration
- PostgreSQL : métadonnées structurées  
- MongoDB : avis clients JSON  
- 📊 UML pour PostgreSQL + optimisation NoSQL  

### 3️⃣ Analyse par Machine Learning
- ⚙️ Pipeline : nettoyage, NLP, BERT multilingue  
- 🏆 Benchmark : LogisticRegression, LinearSVC, RandomForest  
- 🔄 Suivi des modèles avec **MLflow**  
- 📉 Visualisation avec **Streamlit**  

---

## 🛠️ Architecture technique
1. Scraping des avis Trustpilot  
2. Stockage : PostgreSQL (métadonnées) + MongoDB (avis JSON)  
3. Traitement : nettoyage + NLP + BERT  
4. Modélisation : classification ML  
5. Visualisation : Streamlit + MLflow  

---

## ⚙️ Exécution des scripts
```bash
cd scripts

# Scraping
python scraping/cde_scrap_new.py

# Insertion en base
python scraping/insert_postgre.py
python scraping/insert_mongodb.py

# Préprocessing & ML
python preprocess/snapshot_data.py
python preprocess/sentiment_analysis.py
python preprocess/clean_data.py
python preprocess/preprocess_clean_avis.py
python models/train_dual_models.py

# MLflow
bash mlflow/start_mlflow.sh
python mlflow/mlflow_tracking.py

# Application
streamlit run app/app_streamlit.py
```

---

## 📁 Organisation des répertoires
```
cde/
├── data/          # Données brutes, modèles
├── docker-data/   # Volumes Docker
├── docs/          # Documentation
├── logs/          # Logs
├── notebooks/     # Notebooks
├── scripts/       # Scripts Python et shell
├── tests/         # Tests unitaires
└── tmp/           # Fichiers temporaires
```

---

## 🧱 Schéma de base de données
**PostgreSQL** : `societe`, `societe_<nom>_wiki`, `vue_societes_wiki_harmonisee`  
**MongoDB** : `avis_trustpilot`, `societe`

---

## 📊 Résultats obtenus
- **66 864 avis** collectés  
  - Tesla : 217 | Temu : 3 545 | Chronopost : 32 220 | Vinted : 30 882  
- **Performances ML** :  
  - Sentiment → LinearSVC (Acc. **85%**)  
  - Note → LinearSVC (Acc. **80%**)  
- **Insights** :  
  - 74,6% des avis sont à 1 ou 5⭐  
  - Thèmes dominants : livraison, service client, produit  

---

## 🌐 Extension du projet – Collecte via Wikipedia
- Métadonnées sociétales (SIREN, CA, effectifs, logos)  
- Scripts : `cde_scrap_new.py`, `cde_insert_wiki.py`  

---

## 🌐 Extension du projet – Suivi des modèles ML
- **MLflow** pour suivi des modèles, métriques, artefacts  
- Scripts : `start_mlflow.sh`, `mlflow_tracking.py`  
- URL : `http://localhost:5000`  

---

## 🚀 Technologies utilisées
Python, SQL, Shell  
PostgreSQL, MongoDB  
BERT, spaCy, NLTK, Scikit-learn  
Streamlit, Matplotlib, WordCloud  
Docker, MLflow  

---

## ⚠️ Limites et considérations éthiques
- Respect du RGPD : pas de stockage des auteurs  
- Transparence : documentation des méthodes  
- Objectivité : résultats équilibrés  
- Pas d’usage commercial/malveillant  

---

## ⚡ Installation rapide
```bash
git clone https://github.com/DataScientest-Studio/mar25_cde_satisfaction.git
cd mar25_cde_satisfaction
python3 -m venv cde_env
source cde_env/bin/activate
pip install -r requirements.txt
docker-compose up -d
bash mlflow/start_mlflow.sh
streamlit run app/app_streamlit.py
```

---

## 📄 Licence
Projet sous licence MIT → voir [LICENSE](LICENSE)

---

## 👨‍💻 Auteur

📅 Date : 24 août 2025
