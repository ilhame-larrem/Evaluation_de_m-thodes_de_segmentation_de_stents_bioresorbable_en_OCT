import os
import cv2
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

# Chemin du dossier contenant les images
dossier_images = r"C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient6M6"

# Liste pour stocker les aires des struts
aires_struts = []

# Espacement entre les coupes (à adapter)
espacement_entre_coupes = 0.1  # Par exemple, 0.1 mm

# Parcours des images dans le dossier
for nom_fichier in os.listdir(dossier_images):
    if nom_fichier.endswith(".png"):
        chemin_image = os.path.join(dossier_images, nom_fichier)

        # Charger l'image en niveaux de gris
        image = io.imread(chemin_image, as_gray=True)

        # Segmenter les struts (à adapter en fonction de vos images)
        _, seuil_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

        # Trouver les contours des struts
        contours, _ = cv2.findContours(seuil_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Dessiner les contours sur l'image
        image_contours = np.copy(image)
        cv2.drawContours(image_contours, contours, -1, (255, 0, 0), 2)

        # Calculer l'aire des struts
        aire_struts = cv2.countNonZero(seuil_image)
        aires_struts.append(aire_struts)

        # Afficher l'image avec les contours
        # plt.imshow(image_contours, cmap='gray')
        # plt.title(f'Aire des struts : {aire_struts} pixels')
        # plt.show()

# Calculer le volume total
volume_total = sum(aires_struts) * espacement_entre_coupes

# Afficher le volume total
print("Volume total des struts (mm³) :", volume_total)
