import os
import cv2
import matplotlib.pyplot as plt
from skimage import io

def calculate_polymer_volume(image_path):
    # Charger l'image en niveaux de gris
    image = io.imread(image_path, as_gray=True)

    # Compter le nombre de pixels blancs
    white_pixel_count = cv2.countNonZero((image * 255).astype('uint8'))

    return white_pixel_count

def process_patient(patient_folder, start, end, identifier):
    volumes = []

    # Boucle pour parcourir les images
    for numero_coupe in range(start, end + 1):
        # Construire le chemin complet de l'image
        if identifier == 'J0':
            image_path = os.path.join(patient_folder, f'struts_cartesian_20150114125448_{numero_coupe}.png')
        elif identifier == 'M6':
            image_path = os.path.join(patient_folder, f'struts_cartesian_20150603113535_{numero_coupe}.png')
        else:
            raise ValueError("Identifier doit être 'J0' ou 'M6'.")

        # Vérifier si l'image existe
        if os.path.exists(image_path):
            # Calculer le volume de polymère (nombre de pixels blancs)
            volume = calculate_polymer_volume(image_path)
            volumes.append(volume)

            # # Écrire les résultats dans un fichier texte
            # fichier_resultats = f'resultats_coupe_{identifier}_{numero_coupe}.txt'
            # with open(fichier_resultats, 'w') as fichier:
            #     fichier.write(f'Nombre de pixels blancs pour {image_path} : {volume}')

    return volumes

def plot_comparison(volumes_J0, volumes_M6):
    plt.figure(figsize=(10, 6))  # Ajuster la taille de la figure

    plt.plot(volumes_J0, label='J0', marker='o', linestyle='-', color='blue')
    plt.plot(volumes_M6, label='M6', marker='o', linestyle='-', color='green')

    # Ajouter une ligne horizontale pour faciliter la comparaison
    plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)

    plt.title('Évolution du nombre de pixels blancs entre J0 et M6')
    plt.xlabel('Numéro de coupe')
    plt.ylabel('Nombre de pixels blancs')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    # # Ajouter des annotations pour indiquer les points de changement
    # plt.annotate('Changement J0 -> M6', xy=(150, 0), xytext=(150, 20000),
    #              arrowprops=dict(facecolor='red', shrink=0.05))

    # plt.annotate('Changement M6 -> J0', xy=(200, 0), xytext=(200, 20000),
    #              arrowprops=dict(facecolor='red', shrink=0.05))

    plt.show()
    
def main():
    # Dossiers contenant les images J0 et M6
    patient_folder_J0 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient6J0'
    patient_folder_M6 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient6M6'

    # Numéros de la première et de la dernière coupe pour J0 et M6
    j0_start, j0_end = 34, 393
    m6_start, m6_end = 160, 517

    # Traitement pour J0
    j0_volumes = process_patient(patient_folder_J0, j0_start, j0_end, 'J0')

    # Traitement pour M6
    m6_volumes = process_patient(patient_folder_M6, m6_start, m6_end, 'M6')

    # Afficher le graphique comparatif
    plot_comparison(j0_volumes, m6_volumes)

if __name__ == "__main__":
    main()
