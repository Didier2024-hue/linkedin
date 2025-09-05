import pandas as pd
import matplotlib.pyplot as plt

# Chargement du CSV
df = pd.read_csv("/home/datascientest/cde/data/processed/report_sentiment_avis_avec_sentiments.csv")

print(df.head())  # pour vérification

# Création de l'histogramme avec les bonnes colonnes
plt.figure(figsize=(8, 5))
bars = plt.bar(df["sentiment_note"], df["count"], color='skyblue', edgecolor='black')
plt.title("Répartition des avis par note de sentiment (1 à 5)", fontsize=14)
plt.xlabel("Note de sentiment (1 = très négatif, 5 = très positif)")
plt.ylabel("Nombre d'avis")
plt.xticks(df["sentiment_note"])

# Ajouter les valeurs au-dessus des barres
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 50, f"{yval}", ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig("/home/datascientest/cde/data/processed/sentiment_distribution.png")  # sauvegarde le graphique dans un fichier PNG
print("Graphique sauvegardé sous sentiment_distribution.png")
