# **Description du projet** :brain:
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

<img width="567" height="432" alt="image" src="https://github.com/user-attachments/assets/85e98425-a7ae-447c-bce5-5209287c365b" />


De façon surprenante, en revenant à l'atlas BASC original sans **aucune autre modification** du code original, les performances ont chuté davantage (R² = -0.27), ce qui soulève des questions sur la stabilité du pipeline.

> [!CAUTION]
> Le dépôt original ne contient aucun fichier `requirements.txt`, rendant impossible la reproduction exacte des versions des packages utilisés. :unamused:

## Tentatives d'amélioration :thinking:

Plusieurs stratégies ont été explorées pour tenter d'améliorer les performances du modèle, sans succès.

1. La réduction de dimensionnalité par PCA
2. La sélection de features par KBest ont toutes deux été testées, cette dernière donnant des résultats encore plus faibles.
3. Des transformations logarithmique et racine carrée ont été appliquées: sans amélioration notable.
4. L'optimisation des hyperparamètres via GridSearchCV a également été tentée dans chacun de ces cas, sans succès.

> [!NOTE]
> Malgré l'ensemble de ces tentatives, aucune configuration n'a permis d'obtenir un R² positif satisfaisant.

> [!CAUTION]
> Il est possible de convenir que le repo n'est **PAS** REPRODUCTIBLE à cette étape.

Voici la matrice de corrélation original
<img width="835" height="661" alt="image" src="https://github.com/user-attachments/assets/c99f439a-5bc3-4147-b20c-92753fcde10d" />

Voici la matrice de corrélation avec le nouvelle atlas
<img width="913" height="811" alt="image" src="https://github.com/user-attachments/assets/a142526a-cab2-4630-99eb-50c2b27c9d1a" />

# **Tâche 2: ~~Comparer~~ Tester différents modèles**
> [!WARNING]
> Puisque tous les R² étaient au final très mauvais cette tâche a davantage été de l'exploration que de la comparaison

### 🧠 Modèle DMN (Default Mode Network)

Plutôt que d'utiliser toutes les connexions fonctionnelles, ce modèle se restreint aux connexions intra-DMN, un réseau particulièrement associé aux processus sociaux et à la théorie de l'esprit. L'atlas Schaefer 100 ROIs identifie **26 ROIs appartenant au DMN**, générant **325 features** de connectivité.

| Métrique | Résultat |
|---|---|
| R² | -0.51 |
| Variance expliquée | -0.48 |
| MAE | 0.196 |
| Median AE | 0.167 |

> [!CAUTION]
> Restreindre les features au DMN détériore les performances par rapport au modèle complet (R² = -0.27 → -0.51), suggérant que la connectivité intra-DMN seule n'est pas suffisante pour prédire le ToM chez les enfants.

### 🧠 Modèle ToM Network
Richardson et al (2018) ont montré que le réseau de théorie de l'esprit serait déjà différencié dès 3 ans. Dans son réseau Richardson y incluesÈ
- TPJ
- PCC
- dmPFC
- vmPFC

Ce modèle cible spécifiquement 16 ROIs associées à la théorie de l'esprit dans la littérature : la jonction temporo-pariétale (TPJ), le cortex cingulaire postérieur (PCC), le cortex préfrontal médian dorsal (dmPFC) et ventral (vmPFC). Ces régions génèrent **120 features** de connectivité.

| Métrique | Résultat |
|---|---|
| R² | -0.74 |
| Variance expliquée | -0.68 |
| MAE | 0.211 |
| Median AE | 0.164 |

> [!CAUTION]
> Ce modèle est le moins performant de tous ceux testés. Cibler uniquement les régions classiquement associées au ToM ne suffit pas et l'optimisation des hyperparamètres n'a pas été tentée étant donné les résultats déjà peu prometteurs. La connectivité fonctionnelle de ces régions ne semble pas prédire le ToM de façon fiable dans ce jeu de données.
