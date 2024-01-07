
### Evaluation de méthodes de segmentation de stents biorésorbable en OCT.

L'évaluation des méthodes de segmentation de stents bi-résorbables en OCT (tomographie par cohérence optique) représente un domaine crucial dans le domaine médical. Les stents biorésorbables, en raison de leur nature temporaire, exigent une précision maximale lors de leur visualisation et de leur suivi. L'OCT, une technologie d'imagerie de haute résolution, offre une opportunité prometteuse pour évaluer ces stents. Ce projet vise à examiner et à évaluer différentes méthodes de segmentation, essentielles pour une interprétation précise des images OCT et pour la surveillance appropriée des stents biorésorbables. Cette introduction offre un aperçu de l'importance clinique et de la pertinence de cette étude, soulignant l'impact potentiel sur les pratiques médicales et la qualité des soins aux patients. et dans le but de notre projet est d'**évaluer les méthodes de segmentation automatique et manuelle de des stents en OCT** 

Dans le répertoire *Biores*, qui contient les données de six patients, chaque patient dispose de deux sous-dossiers, **J0** et **M6**. Chaque sous-dossier est identifié par un numéro différent, permettant de distinguer les images spécifiques à chaque patient pour l'OCT et la segmentation manuelle réalisée par les médecins. On se trouve également le dossier *mrcc* qui contient les résultats de la segmentation automatique obtenus à l'aide d'un réseau de neurones de type **mask-RCNN** développé par des étudiants. En parallèle, nous disposons d'une méthode de segmentation interactive décrite par Pierre-Yves Menguy dans sa thèse de 2016. L'objectif global de notre projet est de comparer les résultats de segmentation et d'analyser l'évolution du volume de polymère entre l'implantation du stent (J0) et le suivi à 6 mois (M6). Cette analyse se penchera sur la variation de volume pour chaque maille, chaque coupe et dans l'ensemble de la séquence.


## Les étapes de notre projet

- Etat d'art

Nous avons entamé notre projet par une revue de littérature approfondie, centrée sur la recherche et la synthèse des travaux antérieurs liés à notre domaine d'étude. Cette revue a englobé plusieurs aspects essentiels, notamment les différents types de stents existants, leurs applications cliniques variées, les techniques d'imagerie **OCT** et leur utilisation spécifique dans la visualisation des stents au sein des artères coronaires, ainsi que l'exploration des architectures de deep learning pour la segmentation automatique de ces stents.


