# **Description du projet**
Pour ce travail, j'ai choisi le projet Unveiling Children's Theory of Mind with rs-fMRI créé par Wei-Hung Lin, & Syuan-Yu Lin et publié le 1 juin 2023. Ce projet visait à comprendre si la connectivité fonctionnelle peut être utilisée pour prédire la théorie de l'esprit (TdE) chez les enfants. Ce projet utilisait des algorithmes d'apprentissage automatique supervisé appliqués à des données d'IRMf afin de prédire les capacités de ToM chez les enfants.

Un jeu de données d'IRMf au repos prétraité provenant du Nilearn Development fMRI à été sélectionné pour réaliser ce projet. Ce jeu de données d'IRMf-repos est issu d'une étude portant sur le développement de régions cérébrales sociales fonctionnellement spécialisées, dans laquelle les participants regardaient un court métrage durant l'acquisition des données d'IRMf. Tous les enfants ont complété une tâche explicite du TdE conçue sur mesure afin de mesurer leurs capacités de TdE.

## **Données**
122 enfants
Âge moyen 6,71 ans (3–12 ans)
Score TdE moyen = 0,775

## **Projet original**
Utilisation de l'atlas BASC (Bootstrap Analysis of Stable Clusters) à 64 parcelles pour extraire les séries temporelles
Modèle
Validation croisée k-fold sur des données d'entraînement: 85 sujets
Évaluation des performances sur l’ensemble de test: 37 sujets

> [!NOTE]
>  **R2 = 0.27**

<img width="567" height="437" alt="image" src="https://github.com/user-attachments/assets/24f6dba4-157b-4afb-b68b-aaced8689845" />

# **Tâche 1: Reproduire le notebook**
## Défis de reproduction

La reproduction de ce projet a rencontré plusieurs obstacles. D'abord, l'atlas original (BASC) a été remplacé par l'atlas Schaefer à 100 ROIs. En raison des limites de mémoire locale, le code a d'abord été développé sur un sous-ensemble de 37 participants, puis exécuté sur Google Colab avec les 155 participants disponibles — sans amélioration notable (R² = -0.09).

De façon surprenante, en revenant à l'atlas BASC original sans aucune autre modification, les performances ont chuté davantage (R² = -0.27), ce qui soulève des questions sur la stabilité du pipeline.

> [!CAUTION]
> Le dépôt original ne contient aucun fichier `requirements.txt`, rendant impossible la reproduction exacte des versions des packages utilisés.
