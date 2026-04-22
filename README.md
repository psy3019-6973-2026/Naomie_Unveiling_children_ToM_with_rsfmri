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
R2 = 0.365
