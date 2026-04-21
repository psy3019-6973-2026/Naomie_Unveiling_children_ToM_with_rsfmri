"""
tasks.py — Pipeline automatisé pour Rioux_recreation_ToM
Commandes disponibles :
  invoke setup     → installe les dépendances
  invoke run       → exécute le notebook complet
  invoke clean     → supprime les outputs générés
  invoke fetch     → (optionnel) télécharge les données
"""
 
from invoke import task
import os
import yaml
 
# Charger la config depuis invoke.yaml
with open("invoke.yaml", "r") as f:
    config = yaml.safe_load(f)
 
NOTEBOOK = config["notebook"]
OUTPUT_DIR = config["output_data_dir"]
REQUIREMENTS = config["requirements_file"]
 
 
@task
def setup(c):
    """Installe toutes les dépendances Python."""
    print("📦 Installation des dépendances...")
    c.run(f"pip install -r {REQUIREMENTS}")
    print("✅ Dépendances installées.")
 
 
@task
def fetch(c):
    """Télécharge les données sources (fMRI + behavioural CSV)."""
    print("🌐 Les données seront téléchargées automatiquement par nilearn lors du run.")
    print("   - Dataset fMRI : nilearn.datasets.fetch_development_fmri()")
    print("   - Atlas Schaefer : nilearn.datasets.fetch_atlas_schaefer_2018()")
    print("   - Behavioural CSV : GitHub (WeiHungLin/BHS_project)")
 
 
@task
def run(c):
    """Exécute le notebook Jupyter complet et exporte les outputs."""
    print(f"🚀 Lancement du pipeline : {NOTEBOOK}")
 
    # Créer le dossier output si nécessaire
    os.makedirs(OUTPUT_DIR, exist_ok=True)
 
    # Convertir et exécuter le notebook avec papermill ou nbconvert
    output_notebook = os.path.join(OUTPUT_DIR, NOTEBOOK.replace(".ipynb", "_executed.ipynb"))
 
    # Option 1 : avec papermill (recommandé — capture les outputs cellule par cellule)
    result = c.run(f"papermill {NOTEBOOK} {output_notebook}", warn=True)
 
    if result.ok:
        print(f"✅ Notebook exécuté avec succès.")
        print(f"   Output sauvegardé : {output_notebook}")
        # Exporter aussi en HTML pour visualiser facilement
        c.run(f"jupyter nbconvert --to html {output_notebook} --output-dir {OUTPUT_DIR}")
        print(f"   Rapport HTML : {OUTPUT_DIR}/")
    else:
        print("❌ Erreur lors de l'exécution. Essaie avec nbconvert à la place...")
        c.run(
            f"jupyter nbconvert --to notebook --execute {NOTEBOOK} "
            f"--output {output_notebook}"
        )
 
 
@task
def clean(c):
    """Supprime les fichiers générés dans le dossier output."""
    print(f"🧹 Nettoyage du dossier : {OUTPUT_DIR}")
    c.run(f"rm -rf {OUTPUT_DIR}")
    print("✅ Nettoyage terminé.")
