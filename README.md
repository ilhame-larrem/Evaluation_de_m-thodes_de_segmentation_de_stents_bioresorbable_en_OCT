
### Evaluation de méthodes de segmentation de stents biorésorbable en OCT.

L'évaluation des méthodes de segmentation de stents bi-résorbables en OCT (tomographie par cohérence optique) représente un domaine crucial dans le domaine médical. Les stents biorésorbables, en raison de leur nature temporaire, exigent une précision maximale lors de leur visualisation et de leur suivi. L'OCT, une technologie d'imagerie de haute résolution, offre une opportunité prometteuse pour évaluer ces stents. Ce projet vise à examiner et à évaluer différentes méthodes de segmentation, essentielles pour une interprétation précise des images OCT et pour la surveillance appropriée des stents biorésorbables. Cette introduction offre un aperçu de l'importance clinique et de la pertinence de cette étude, soulignant l'impact potentiel sur les pratiques médicales et la qualité des soins aux patients. et dans le but de notre projet est d'**évaluer les méthodes de segmentation automatique et manuelle de des stents en OCT** 

Dans le répertoire *Biores*, qui contient les données de six patients, chaque patient dispose de deux sous-dossiers, **J0** et **M6**. Chaque sous-dossier est identifié par un numéro différent, permettant de distinguer les images spécifiques à chaque patient pour l'OCT et la segmentation manuelle réalisée par les médecins. On se trouve également le dossier *mrcc* qui contient les résultats de la segmentation automatique obtenus à l'aide d'un réseau de neurones de type **mask-RCNN** développé par des étudiants. En parallèle, nous disposons d'une méthode de segmentation interactive décrite par Pierre-Yves Menguy dans sa thèse de 2016. L'objectif global de notre projet est de comparer les résultats de segmentation et d'analyser l'évolution du volume de polymère entre l'implantation du stent (J0) et le suivi à 6 mois (M6). Cette analyse se penchera sur la variation de volume pour chaque maille, chaque coupe et dans l'ensemble de la séquence.



## Les étapes de notre projet

- Etat d'art

Nous avons entamé notre projet par une revue de littérature approfondie, centrée sur la recherche et la synthèse des travaux antérieurs liés à notre domaine d'étude. Cette revue a englobé plusieurs aspects essentiels, notamment les différents types de stents existants, leurs applications cliniques variées, les techniques d'imagerie **OCT** et leur utilisation spécifique dans la visualisation des stents au sein des artères coronaires, ainsi que l'exploration des architectures de deep learning pour la segmentation automatique de ces stents.

- Calcul des **composantes connexes**

Le calcul des composantes connexes est une étape importante dans le traitement d'images pour la segmentation. Pour identifier et étiqueter différentes parties connectées dans une image. Dans notre cas, on a utilisé la Librairie Python `scikit-image` (abrégée en `skimage`) qui est une puissante bibliothèque dédiée au traitement d'images. Elle offre un large éventail de fonctionnalités pour la manipulation , le traitement et l'analyse d'images, y compris la segmentation et le calcul des composantes connexes.

```python
from skimage import io, measure
```

Pour calculer les comoposantes connexes dans une image en utilisant `scikit-image` on utilise la fonction `label` du module `measure` qui attribue des étiquettes aux différents régions connectées dans une image.

Pour entamer notre projet, nous avons mis en place un code Python utilisant la bibliothèque `scikit-image`. Ce code sélectionne une image de segmentation spécifique, puis procède au calcul du nombre de struts détectés dans cette image.

```python
# Charger l'image segmentée
image_segmentee = io.imread('struts_cartesian_20141029182218_240.png')

# Obtenir les labels (étiquettes) pour chaque région
labels, nombre_de_struts = measure.label(image_segmentee, connectivity=2, return_num=True)

# Calculer les propriétés de chaque région (strut)
regions = measure.regionprops(labels)
```

En utilisant les fonctionnalités de `scikit-image`, nous avons mis en place un processus initial pour identifier et compter les struts, constituants essentiels des stents, dans les images de segmentation. Ce travail préliminaire sert de fondation pour une analyse plus approfondie et une segmentation précise des composants des stents bi-résorbables dans les images OCT.

- Calcul des métriques

Par la suite après avoir labelliser les struts détectés dans la segmentation on passe à l'évalution de cette segmentation, le calcul des métriques. Dans un premier temps, on a essayé d'écrire un code qui effectue la comparaison entre deux images de segmentation; une image de segmentation automatique('**seg_auto**') et une image de référence de segmentation manuelle ('**seg_manuelle**'). L'objectif de notre code est d'évaluer la précision de la segmentation automatique par rapport à la référence manuelle en comptant les régions communes, les **vrais positifs** , les **faux positifs** et les **faux négatifs**.

Notre code se résume de la manière suivante:
1. *Chargement des images*: Les images de segmentation et manuelle sont chargées à l'aide de la bibliothèque (`scikit-image`).
2. *Redimensionnement*: On a ajusté la taille de l'image de segmentation manuelle qui est ajustée pour correpondre à celle de l'image de segmentation automatique. 
3. *Calcul des composantes connexes*: Les composantes connexes sont identifiées dans les deux images à l'aide la fonction `measure.label` de `scikit-image`.
4. *comparaison des composantes*: Les pixels des composantes connexes sont comparés entre les deux images pour déterminer les **vrais positifs**, les **faux positifs** et les **fauw négatifs**.
5. *Création d'images pour l'évaluation*: Des images sont crées pour visualiser les régio communes, les vrais positifs, les faux positifs entre les deux segmentations.
6. *Affichage des résultats*: Les résultats de l'évaluation (nombre total de struts détectés, nombre de vrais positifs, faux positifs et faux négatifs) sont affichés dans la console. De plus, quatre sous-graphiques sont affichés dans une figure, montrant respctivement: l'image de référence; l'image de segmentation automatique, une superposition des régions communes, et une image colorée représentant les résultats de l'évaluation.

Le but de cette étape est de faire un code qui permet l'analyse visuelle et quantitative de la précision de la segmentation automatique par rapport à la segmentation manuelle des struts, en mattent en évidence les régions de concordance et les divergence entre les deux méthodes de segmentation.

 ![Texte alternatif](chemin/vers/votre/image.png)

