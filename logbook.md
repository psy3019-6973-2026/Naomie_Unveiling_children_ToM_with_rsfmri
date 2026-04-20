## Logbook

1. **Mise à jour des dépendances Nilearn**

Problème :
Utilisation de nilearn.input_data, devenu obsolète dans les versions récentes.

Action :
Mise à jour des imports vers l’API recommandée.

Résultat :
Erreur résolue, compatibilité restaurée.

2. **Chargement de l’atlas Schaefer**

Contexte :
Transition de l’atlas BASC vers Schaefer pour l’extraction des ROI.

Problèmes rencontrés :

instabilité lors du chargement de l’atlas
erreurs lors de l’augmentation du nombre de participants et/ou ROI

Expérimentations :

réduction du nombre de ROI (400 → inférieur) → échec
réduction du nombre de sujets :
50 sujets → échec
40 sujets → instable
37 sujets → fonctionnement stable

Solution retenue :

exécution du pipeline sur Google Colab pour stabiliser l’environnement computationnel

3. **Modélisation prédictive du ToM (régression)**
3.1 Configuration initiale
Régression du score ToM à partir de la connectivité fonctionnelle
Modèles testés : SVR,
Validation croisée (CV = 10 folds)

Résultat initial :

R² systématiquement négatif (performance inférieure à la baseline)
3.2 Simplification du problème

Hypothèse : réduction de la complexité du problème

Passage de 4 classes ToM → 2 classes / regroupement

Résultat :

R² ≈ -0.6 (aucune amélioration)
3.3 Restriction des features (DMN)

Approche :

utilisation exclusive du Default Mode Network (DMN)

Problèmes techniques :

erreur IndexError: too many indices for array
cause : mauvaise gestion des dimensions (array 1D traité comme 2D)
correction de la structure des données
suppression des indices liés au "background"

Résultat :

performance toujours négative (R² < 0)
3.4 Réseau ToM (Richardson et al., 2018)

Approche :

sélection de régions cérébrales associées au Theory of Mind

Résultat :

R² ≈ -0.1 (légère amélioration mais insuffisante)
3.5 Optimisation des hyperparamètres

Méthode :

GridSearchCV sur les paramètres des modèles

Résultat :

aucune amélioration significative des performances
3.6 Passage à la classification

Approche :

transformation du problème de régression en classification (ToM)

Résultat :

performances légèrement améliorées après optimisation
mais précision globale encore limitée

4. **Visualisation de la connectivité (connectogramme)**
4.1 Implémentation initiale
tentative avec nichord (package externe)

Limitation :

documentation insuffisante
incompatibilité avec le pipeline MNE

4.2 Implémentation MNE-Connectivity

Solution retenue :

utilisation des fonctions officielles MNE :

Références :

https://mne.tools/mne-connectivity/dev/generated/mne_connectivity.viz.plot_connectivity_circle.html
https://mne.tools/mne-connectivity/stable/auto_examples/mne_inverse_label_connectivity.html
4.3 Problèmes techniques

1. Erreur de labels

parcellations.labels not found
résolu via correction des imports et installation de mne-connectivity

2. Problème de dimension

matrice de connectivité mal vectorisée (format 1D incorrect)
cause identifiée : inclusion du label "background"

Solution :

suppression du label "background"
correction de la structure des matrices
4.4 Qualité de visualisation

Problèmes observés :

signal faible → visualisation peu interprétable
surcharge visuelle des régions

Optimisations testées :

ajustement des paramètres vmin / vmax
regroupement des régions par palette de couleurs adaptée pour daltonien.ne.s
tentative de suppression des labels individuels

ajout de connectome  à l'entour du connectogramme


5. Synthèse générale
Pipeline global fonctionnel mais limité par :
faible taille d’échantillon pour train (N = 85)
forte dimensionnalité des features
faible signal prédictif comportemental
Les différentes optimisations (modèle, features, hyperparamètres) n’ont pas permis d’améliorer significativement les performances de régression
Les résultats suggèrent une relation faible entre connectivité fonctionnelle rs-fMRI et scores ToM individuels dans ce dataset
