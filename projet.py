import os
import numpy as np
from skimage import io, measure, img_as_ubyte
from skimage.transform import resize
import matplotlib.pyplot as plt

def patient_segmentation(num_patient, dossier_manuelle, dossier_auto, dossier_graphes, fichier_resultats, debut, fin, identifiant_struts_manuelle, identifiant_struts_auto):
    with open(fichier_resultats, 'a') as fichier_resultats_patient:
        for jour in range(debut, fin + 1):
            identifiant_jour_manuelle = f"{identifiant_struts_manuelle}_{jour}"
            identifiant_jour_auto = f"{identifiant_struts_auto}_{jour}"

            chemin_image_manuelle = os.path.join(dossier_manuelle, identifiant_jour_manuelle + '.png')
            chemin_image_auto = os.path.join(dossier_auto, identifiant_jour_auto + '.png')

            image_manuelle = io.imread(chemin_image_manuelle)
            image_auto = io.imread(chemin_image_auto)

            image_manuelle = resize(image_manuelle, image_auto.shape[:2], anti_aliasing=True)

            labels_auto, num_labels_auto = measure.label(image_auto, connectivity=2, return_num=True)
            labels_manuelle, num_labels_manuelle = measure.label(image_manuelle, connectivity=2, return_num=True)

            vrais_positifs = []
            faux_positifs = []
            faux_negatifs = []

            for label in range(1, num_labels_auto + 1):
                region_auto = (labels_auto == label)
                intersection = np.logical_and(region_auto, labels_manuelle > 0)

                if np.any(intersection):
                    vrais_positifs.append(label)
                else:
                    faux_positifs.append(label)

            for label in range(1, num_labels_manuelle + 1):
                region_manuelle = (labels_manuelle == label)
                intersection = np.logical_and(region_manuelle, labels_auto == 0)

                if np.any(intersection):
                    faux_negatifs.append(label)

            overlay_with_colors = np.zeros((image_auto.shape[0], image_auto.shape[1], 4), dtype=np.uint8)

            for label in vrais_positifs:
                overlay_with_colors[labels_auto == label] = [0, 255, 0, 255]  # VP en vert

            for label in faux_positifs:
                overlay_with_colors[labels_auto == label] = [255, 0, 0, 255]  # FP en rouge

            for label in faux_negatifs:
                overlay_with_colors[labels_manuelle == label] = [0, 0, 255, 255]  # FN en bleu

            overlay = np.zeros_like(image_auto)

            for label in range(1, num_labels_auto + 1):
                region_auto = (labels_auto == label)
                intersection = np.logical_and(region_auto, labels_manuelle > 0)
                
                if np.any(intersection):
                    overlay[region_auto] = 1

            fig, axs = plt.subplots(2, 2, figsize=(7, 7))

            axs[0, 0].imshow(image_manuelle, cmap='gray')
            axs[0, 0].set_title("Ground truth")
            axs[0, 0].axis('off')

            axs[0, 1].imshow(image_auto, cmap='gray')
            axs[0, 1].set_title("Segmentation automatique")
            axs[0, 1].axis('off')

            axs[1, 0].imshow(overlay, cmap='gray')  # Affichage de l'image superposée
            axs[1, 0].set_title("Image superposée")
            axs[1, 0].axis('off')

            axs[1, 1].imshow(overlay_with_colors)
            axs[1, 1].set_title("Image des métriques")
            axs[1, 1].axis('off')

            dossier_patient = os.path.join(dossier_graphes, f"Patient{num_patient}")
            if not os.path.exists(dossier_patient):
                os.makedirs(dossier_patient)

            nom_fichier = f"superposition_patient{num_patient}_jour{jour}.png"
            chemin_fichier = os.path.join(dossier_patient, nom_fichier)
            plt.savefig(chemin_fichier)
            plt.close(fig)

            fichier_resultats_patient.write(f"Résultats pour le patient {num_patient}, Jour {jour} :\n")
            fichier_resultats_patient.write(f"Chemin de l'image manuelle : {chemin_image_manuelle}\n")
            fichier_resultats_patient.write(f"Chemin de l'image automatique : {chemin_image_auto}\n")
            fichier_resultats_patient.write(f"Nombre total de struts détectés (automatique) : {num_labels_auto}\n")
            fichier_resultats_patient.write(f"Nombre total de struts de référence (manuelle) : {num_labels_manuelle}\n")
            fichier_resultats_patient.write(f"Nombre de vrais positifs : {len(vrais_positifs)}\n")
            fichier_resultats_patient.write(f"Nombre de faux positifs : {len(faux_positifs)}\n")
            fichier_resultats_patient.write(f"Nombre de faux négatifs : {len(faux_negatifs)}\n")
            fichier_resultats_patient.write(f"Chemin du graphe : {chemin_fichier}\n")
            fichier_resultats_patient.write("\n")

## ''' PATIENT 1: DOSSIER J0 et M6 '''

# Pour le J0 du patient 1

patient_segmentation(
    num_patient="1",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\1\J0',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient1J0',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesJ0patient1',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsJ0patient1.txt',
    debut=237,
    fin=395,
    identifiant_struts_manuelle="Struts_20141029182218",
    identifiant_struts_auto="struts_cartesian_20141029182218"
)

# Pour le M6 du patient 1

patient_segmentation(
    num_patient="1",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\1\M6',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient1M6',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesM6patient1',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsM6patient1.txt',
    debut=218,
    fin=372,
    identifiant_struts_manuelle="Struts_20150429114648",
    identifiant_struts_auto="struts_cartesian_20150429114648"
)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

## ''' PATIENT 2: DOSSIER J0 et M6 '''

# POUR le J0 du patient 2

patient_segmentation(
    num_patient="2",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\2\J0',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient2J0',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesJ0patient2',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsJ0patient2.txt',
    debut=156,
    fin=373,
    identifiant_struts_manuelle="Struts_20141124130653",
    identifiant_struts_auto="struts_cartesian_20141124130653"
)

# POUR le M6 du patient 2

patient_segmentation(
    num_patient="2",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\2\M6',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient2M6',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesM6patient2',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsM6patient2.txt',
    debut=175,
    fin=396,
    identifiant_struts_manuelle="Struts_20150513104518",
    identifiant_struts_auto="struts_cartesian_20150513104518"
)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


## ''' PATIENT 3: DOSSIER J0 et M6 '''

# POUR le J0 du patient 3

patient_segmentation(
    num_patient="3",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\3\J0',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient3J0',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesJ0patient3',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsJ0patient3.txt',
    debut=91,
    fin=306,
    identifiant_struts_manuelle="Struts_20141126124321",
    identifiant_struts_auto="struts_cartesian_20141126124321"
)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

## ''' PATIENT 4: DOSSIER J0 et M6 '''

# POUR le J0 du patient 4

patient_segmentation(
    num_patient="4",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\4\J0',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient4J0',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesJ0patient4',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsJ0patient4.txt',
    debut=142,
    fin=299,
    identifiant_struts_manuelle="Struts_20141217150502",
    identifiant_struts_auto="struts_cartesian_20141217150502"
)

# POUR le M6 du patient 4 "pas d'image 210 dans le ségmentation automatique M6"

patient_segmentation(
    num_patient="4",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\4\M6',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient4M6',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesM6patient4',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsM6patient4.txt',
    debut=80,
    fin=233,
    identifiant_struts_manuelle="Struts_20150810114215",
    identifiant_struts_auto="struts_cartesian_20150810114215"
)


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

## ''' PATIENT 5: DOSSIER J0 et M6 '''

# POUR le J0 du patient 5

patient_segmentation(
    num_patient="5",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\5\J0',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient5J0',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesJ0patient5',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsJ0patient5.txt',
    debut=157,
    fin=307,
    identifiant_struts_manuelle="Struts_20150619093736",
    identifiant_struts_auto="struts_cartesian_20150619093736"
)

# POUR le M6 du patient 5

patient_segmentation(
    num_patient="5",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\5\M6',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient5M6',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesM6patient5',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsM6patient5.txt',
    debut=199,
    fin=347,
    identifiant_struts_manuelle="Struts_20151103152109",
    identifiant_struts_auto="struts_cartesian_20151103152109"
)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

## ''' PATIENT 6: DOSSIER J0 et M6 '''

# POUR le J0 du patient 6

patient_segmentation(
    num_patient="6",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\6\J0',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient6J0',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesJ0patient6',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsJ0patient6.txt',
    debut=34,
    fin=393,
    identifiant_struts_manuelle="Struts_20150114125448",
    identifiant_struts_auto="struts_cartesian_20150114125448"
)

# POUR le M6 du patient 6

patient_segmentation(
    num_patient="6",
    dossier_manuelle=r'C:\Master Techmed 2\TP synthèse\Biores\6\M6',
    dossier_auto=r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient6M6',
    dossier_graphes=r'C:\Master Techmed 2\TP synthèse\result\GraphesM6patient6',
    fichier_resultats=r'C:\Master Techmed 2\TP synthèse\result\resultatsM6patient6.txt',
    debut=160,
    fin=517,
    identifiant_struts_manuelle="Struts_20150603113535",
    identifiant_struts_auto="struts_cartesian_20150603113535"
)