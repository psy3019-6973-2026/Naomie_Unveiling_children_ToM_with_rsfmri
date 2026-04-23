# **Description du projet** :brain:
Pour ce travail, j'ai choisi le projet Unveiling Children's Theory of Mind with rs-fMRI créé par Wei-Hung Lin, & Syuan-Yu Lin et publié le 1 juin 2023. Ce projet visait à comprendre si la connectivité fonctionnelle peut être utilisée pour prédire la théorie de l'esprit (TdE) chez les enfants. Ce projet utilisait des algorithmes d'apprentissage automatique supervisé appliqués à des données d'IRMf afin de prédire les capacités de ToM chez les enfants.

Un jeu de données d'IRMf au repos prétraité provenant du Nilearn Development fMRI à été sélectionné pour réaliser ce projet. Ce jeu de données d'IRMf-repos est issu d'une étude portant sur le développement de régions cérébrales sociales fonctionnellement spécialisées, dans laquelle les participants regardaient un court métrage durant l'acquisition des données d'IRMf. Tous les enfants ont complété une tâche explicite du TdE conçue sur mesure afin de mesurer leurs capacités de TdE.

## **License**
MIT

## **Données**
* 122 enfants
* Âge moyen 6,71 ans (3–12 ans)
* Score TdE moyen = 0,775

## **Projet original**
* Les participants ont été divisés en 4 groupes selon leur score ToM :
  - faible (0.2–0.4)
  - modéré-bas (0.4–0.6)
  - modéré-élevé (0.6–0.8)
  - élevé (0.8–1.0).

Utilisation de l'atlas BASC (Bootstrap Analysis of Stable Clusters) à 64 parcelles pour extraire les séries temporelles
Validation croisée k-fold sur des données d'entraînement: 85 sujets
Évaluation des performances sur l’ensemble de test: 37 sujets

**R2 = 0.27**

<img width="567" height="437" alt="image" src="https://github.com/user-attachments/assets/24f6dba4-157b-4afb-b68b-aaced8689845" />

# **Tâche 1: Reproduire le notebook**
## Défis de reproduction

La reproduction de ce projet a rencontré plusieurs obstacles. D'abord, l'atlas original (BASC) a été remplacé par l'atlas Schaefer à 100 ROIs. En raison des limites de mémoire locale, le code a d'abord été développé sur un sous-ensemble de 37 participants, puis exécuté sur Google Colab avec les 155 participants disponibles — sans amélioration notable (R² = -0.09).

<img width="567" height="432" alt="image" src="https://github.com/user-attachments/assets/85e98425-a7ae-447c-bce5-5209287c365b" />

## Retester le code ORIGINAL
De façon surprenante, en revenant à l'atlas BASC original sans **aucune autre modification** du code original, les performances ont chuté davantage (R² = -0.27), ce qui soulève des questions sur la stabilité du pipeline. (vous pouvez trouvez cela  dans `original_repo_2023/Reproduction_Final_Project_Unveiling_the_Theory_of_Mind_with_rs_fMRI.ipynb`)

> [!WARNING]
> Le dépôt original ne contient aucun fichier `requirements.txt`, rendant impossible la reproduction exacte des versions des packages utilisés.

## Tentatives d'amélioration :thinking:

Plusieurs stratégies ont été explorées pour tenter d'améliorer les performances du modèle, sans succès.

1. La réduction de dimensionnalité par PCA 
2. La sélection de features par KBest ont été testées, cette dernière donnant des résultats encore plus faibles.
3. Des transformations logarithmique et racine carrée ont été appliquées. <img width="556" height="435" alt="image" src="https://github.com/user-attachments/assets/e1c7976b-0b70-412e-aab9-859c2e475d28" /> <img width="543" height="436" alt="image" src="https://github.com/user-attachments/assets/bf320feb-6123-4eee-857b-eddcc02b7e4b" />
4. L'optimisation des hyperparamètres via GridSearchCV a également été tentée dans chacun de ces cas, sans succès.
5. Une stratification à 2 groupes a été testée, cette dernière donnant des résultats encore plus faibles.

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
Richardson et al (2018) ont montré que le réseau de théorie de l'esprit serait déjà différencié dès 3 ans. Dans son réseau Richardson y inclues :
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

### Classifications
Face aux faibles performances en régression, une approche par classification binaire (ToM élevé vs faible) a été testée sur les trois ensembles de features.


<img width="511" height="413" alt="image" src="https://github.com/user-attachments/assets/995add96-b1d4-4b1e-b964-8c1a0b2a0fbe" />


#### Résultats
**Accuracy des modèles sans et avec hyperparamètres**
| Modèle | Balanced Accuracy | Balanced Accuracy (best fit) |
|---|---|---|
| Cerveau entier | 0.490 | 0.609 |
| DMN | 0.449 | 0.609 |
| ToM-ROIs | 0.426 |  0.475 |

> [!NOTE]
> Le hasard correspond à une balanced accuracy de 0.50. Les modèles se situent tous près de ce seuil, ce qui indique des performances très modestes.

#### Observations générales

Tant au niveau de modèles de prédictions que de classifications, les features ToM-ROIs sont celles qui généralisent le moins bien.

> [!CAUTION]
> Aucun modèle ne performe de façon convaincante, que ce soit en régression ou en classification. La connectivité fonctionnelle mesurée dans ce jeu de données ne semble pas suffisante pour prédire le ToM chez les enfants de façon fiable.

> [!TIP]
> J'avais trouver ce blog qui montrait comment comparer des modèles : https://www.maartengrootendorst.com/blog/validate/
> Comme les modèles n'étaient pas satisfaisant la comparaison n'a pas marcher, mais les informations semblent pertinentes si jamais vos modèles semblent fonctionner!

# **Tâche 3: Création d'un connectogramme**
Voici la page pour créer des connectogrammes: 
* https://mne.tools/mne-connectivity/dev/generated/mne_connectivity.viz.plot_connectivity_circle.html
* https://mne.tools/mne-connectivity/stable/auto_examples/mne_inverse_label_connectivity.html

Voici le connectogramme des 100 connexions les plus fortes pour le modèle cerveau entier
<img width="729" height="771" alt="image" src="https://github.com/user-attachments/assets/34319d33-02cf-4c93-9055-c4a741987bf0" />

## 🎨 Améliorations visuelles du connectogramme

Plusieurs améliorations ont été apportées par rapport au connectogramme précédent :

- **Fond blanc** pour une meilleure lisibilité
- **Nœuds regroupés et triés par réseau fonctionnel** pour faciliter la lecture des connexions intra- et inter-réseaux
- **Couleurs par réseau** en utilisant une palette adaptée aux daltoniens (Vis, SomMot, DorsAttn, SalVentAttn, Limbic, Cont, Default) ( https://immunobiology.duke.edu/sites/default/files/2023-04/Colorblind-Palette.pdf )
- **Légende** ajoutée pour identifier les réseaux (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html et https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)

<img width="809" height="653" alt="image" src="https://github.com/user-attachments/assets/036e32dd-1167-4f03-834f-9d9b16d9baa2" />

## 🎨 Deuxième améliorations visuelles du connectogramme

- Ajout de connectomes au-dessus de chaque réseau pour mieux situer les régions dans le cerveau

  <img width="910" height="720" alt="connectogramme" src="https://github.com/user-attachments/assets/7d33c0c6-d413-4ee5-b448-6495f60595b3" />

> [!NOTE]
> Les connectomes superposés au connectogramme ont été créés sur Canva (forfait Pro) et ne font donc pas partie du code reproductible.

## 🎨 Création de connectogramme pour le DMN et le ToM network

Connectogramme du DMN
<img width="681" height="653" alt="image" src="https://github.com/user-attachments/assets/fee960f1-a2ee-4ed6-ada5-226e16989176" />
*Note. À gauche son les régions de l'hémisphères gauche et à droite celle de l'hémisphère droit.*

Connectogramme du ToM network
<img width="681" height="653" alt="image" src="https://github.com/user-attachments/assets/8c8d3711-4621-4b88-ac32-c555bfa8b5db" />
*Note. À gauche son les régions de l'hémisphères gauche et à droite celle de l'hémisphère droit.*

# Conclusion
Ce projet montre que contrairement au projet initial, la connectivité fonctionnelle au repos ne semble ni prédire ni classifier les performances au tâches de la théorie de l'esprit.

## Piste d'explication
- Tâche de théorie de l'esprit trop facile
- Non utilisation d'un atlas pour enfant

## Piste future
- Utiliser un autre atlas
- stratifier selon l'âge

# :toolbox: Reproduire le projet
> [!TIP]
>  Si votre ordinateur a peu de RAM, je vous recommande d'exécuter le notebook `Final_Rioux_recreation_ToM.ipynb` sur Google Colab plutôt qu'en local avec ce pipeline.

### Prérequis
- Python 3.8+
- Jupyter Notebook

### Étapes

**1. Cloner le repo**
```bash
git clone https://github.com/psy3019-6973-2026/Naomie_Unveiling_children_ToM_with_rsfmri.git
cd Naomie_Unveiling_children_ToM_with_rsfmri
```

**2. Installer les dépendances**
```bash
invoke setup
```

**3. Télécharger les données**
```bash
invoke fetch
```

**4. Rouler le notebook**
```bash
invoke run
```
Le notebook exécuté sera sauvegardé dans le dossier `output/` en format `.ipynb` et `.html`.

**5. Nettoyer les outputs (optionnel)**
```bash
invoke clean
```
## 📁 Structure du repo

| Fichier/Dossier | Description |
|---|---|
| `Final_Rioux_recreation_ToM.ipynb` | Notebook final avec toutes les analyses |
| `original_repo_2023/` | Repo original de Lin & Lin (2023) + rapport de reproduction |
| `tasks.py` | Pipeline automatisé invoke |
| `invoke.yaml` | Configuration du pipeline |
| `requirements.txt` | Dépendances Python |
| `logbook.md` | Journal de bord du projet |
| `LICENSE` | Licence MIT du projet |

# Utilisation de l'intelligence artificielle
<img width="200" height="100" alt="image" src="https://github.com/user-attachments/assets/42e4a652-9a5f-4c06-936a-fc659c45a570"/>

Le logiciel Claude a été utlisé pour:
* déchiffrer les messages d'erreurs
* aider à trouver des solutions pour améliorer mon modèle
* comprendre les différents hyperparamètres

Le logiciel Copilot a été utilisé pour:
* générer les messages de commits

## **Références**
Duke University Department of Immunobiology. (2023). Colorblind-friendly color palette. https://immunobiology.duke.edu/sites/default/files/2023-04/Colorblind-Palette.pdf

Grootendorst, M. (s.d.). How to validate your ML model. https://www.maartengrootendorst.com/blog/validate/ 

Lin, S.-Y., & Lin, W.-H. (2023, June 23). Unveiling children's theory of mind with rs-fMRI [GitHub repository]. GitHub. https://github.com/WeiHungLin/Unveiling_children_ToM_with_rsfmri

Matplotlib Development Team. (s.d.). matplotlib.patches.Patch. Matplotlib. https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html

Matplotlib Development Team. (s.d.). matplotlib.pyplot.legend. Matplotlib. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html

MNE Connectivity developers. (s.d.). Label connectivity. MNE-Connectivity. https://mne.tools/mne-connectivity/stable/auto_examples/mne_inverse_label_connectivity.html

MNE Connectivity developers. (s.d.). plot_connectivity_circle. MNE-Connectivity. https://mne.tools/mne-connectivity/dev/generated/mne_connectivity.viz.plot_connectivity_circle.html 

Richardson, H., Lisandrelli, G., Riobueno-Naylor, A. et al. Development of the social brain from age three to twelve years. Nat Commun 9, 1027 (2018). https://doi.org/10.1038/s41467-018-03399-2

Yeo, B. T. T., Krienen, F. M., Sepulcre, J., Sabuncu, M. R., Lashkari, D., Hollinshead, M., Roffman, J. L., Smoller, J. W., Zöllei, L., Polimeni, J. R., Fischl, B., Liu, H., & Buckner, R. L. (2011). The organization of the human cerebral cortex estimated by intrinsic functional connectivity. Journal of Neurophysiology, 106(3), 1125–1165. https://doi.org/10.1152/jn.00338.2011
