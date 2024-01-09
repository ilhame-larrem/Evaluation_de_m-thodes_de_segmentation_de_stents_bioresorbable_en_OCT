'''
But du code : séparer les resultats du seg auto des patients
'''
import os
import glob
import shutil

'''
patient 1: 20141029182218 "J0" / 20150429114648 "M6"
patient 2: 20141124130653 "J0" / 20150513104518 "M6"
patient 3: 20141126124321 "J0" / 20150511103534 "M6"
patient 4: 20141217150502 "J0" / 20150810114215 "M6"
patient 5: 20150619093736 "J0" / 20151103152109 "M6"
patient 6: 20150114125448 "J0" / 20150603113535 "M6"

'''

dossier_test = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\output_test_images'
dossier_train = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\output_train_images'

dossier_patient_1_J0 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient1J0'
dossier_patient_1_M6 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient1M6'

dossier_patient_2_J0 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient2J0'
dossier_patient_2_M6 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient2M6'

dossier_patient_3_J0 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient3J0'
dossier_patient_3_M6 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient3M6'

dossier_patient_4_J0 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient4J0'
dossier_patient_4_M6 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient4M6'

dossier_patient_5_J0 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient5J0'
dossier_patient_5_M6 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient5M6'

dossier_patient_6_J0 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient6J0'
dossier_patient_6_M6 = r'C:\Master Techmed 2\TP synthèse\mrcnn\mrcnn\Patient6M6'



identifiant_Patient_1_J0= "struts_cartesian_20141029182218_"
identifiant_Patient_1_M6= "struts_cartesian_20150429114648_"

identifiant_Patient_2_J0= "struts_cartesian_20141124130653_"
identifiant_Patient_2_M6= "struts_cartesian_20150513104518_"

identifiant_Patient_3_J0= "struts_cartesian_20141126124321_"
identifiant_Patient_3_M6= "struts_cartesian_20150511103534_"

identifiant_Patient_4_J0= "struts_cartesian_20141217150502_"
identifiant_Patient_4_M6= "struts_cartesian_20150810114215_"

identifiant_Patient_5_J0= "struts_cartesian_20150619093736_"
identifiant_Patient_5_M6= "struts_cartesian_20151103152109_"

identifiant_Patient_6_J0= "struts_cartesian_20150114125448_"
identifiant_Patient_6_M6= "struts_cartesian_20150603113535_"


def copier_images_du_patient(source_folder, identifiant_Patient, dossier_patient):
    for dossier, _, fichiers in os.walk(source_folder):
        for fichier in fichiers:
            if fichier.startswith(identifiant_Patient):
                chemin_source = os.path.join(dossier, fichier)
                shutil.copy(chemin_source, dossier_patient)

# Copie pour le dossier Patient 1 J0
copier_images_du_patient(dossier_train, identifiant_Patient_1_J0, dossier_patient_1_J0)
copier_images_du_patient(dossier_test, identifiant_Patient_1_J0, dossier_patient_1_J0)

# Copie pour le dossier Patient 1 M6
copier_images_du_patient(dossier_train, identifiant_Patient_1_M6, dossier_patient_1_M6)
copier_images_du_patient(dossier_test, identifiant_Patient_1_M6, dossier_patient_1_M6)
 
# Copie pour le dossier Patient 2 J0
copier_images_du_patient(dossier_train, identifiant_Patient_2_J0, dossier_patient_2_J0)
copier_images_du_patient(dossier_test, identifiant_Patient_2_J0, dossier_patient_2_J0)

# Copie pour le dossier Patient 2 M6
copier_images_du_patient(dossier_train, identifiant_Patient_2_M6, dossier_patient_2_M6)
copier_images_du_patient(dossier_test, identifiant_Patient_2_M6, dossier_patient_2_M6)

# Copie pour le dossier Patient 3 J0
copier_images_du_patient(dossier_train, identifiant_Patient_3_J0, dossier_patient_3_J0)
copier_images_du_patient(dossier_test, identifiant_Patient_3_J0, dossier_patient_3_J0)

# Copie pour le dossier Patient 3 M6
copier_images_du_patient(dossier_train, identifiant_Patient_3_M6, dossier_patient_3_J0)
copier_images_du_patient(dossier_test, identifiant_Patient_3_M6, dossier_patient_3_J0)

# Copie pour le dossier Patient 4 J0
copier_images_du_patient(dossier_train, identifiant_Patient_4_J0, dossier_patient_4_J0)
copier_images_du_patient(dossier_test, identifiant_Patient_4_J0, dossier_patient_4_J0)

# Copie pour le dossier Patient 4 M6
copier_images_du_patient(dossier_train, identifiant_Patient_4_M6, dossier_patient_4_M6)
copier_images_du_patient(dossier_test, identifiant_Patient_4_M6, dossier_patient_4_M6)

# Copie pour le dossier Patient 5 J0
copier_images_du_patient(dossier_train, identifiant_Patient_5_J0, dossier_patient_5_J0)
copier_images_du_patient(dossier_test, identifiant_Patient_5_J0, dossier_patient_5_J0)

# Copie pour le dossier Patient 5 M6
copier_images_du_patient(dossier_train, identifiant_Patient_5_M6, dossier_patient_5_M6)
copier_images_du_patient(dossier_test, identifiant_Patient_5_M6, dossier_patient_5_M6)

# Copie pour le dossier Patient 6 J0
copier_images_du_patient(dossier_train, identifiant_Patient_6_J0, dossier_patient_6_J0)
copier_images_du_patient(dossier_test, identifiant_Patient_6_J0, dossier_patient_6_J0)

# Copie pour le dossier Patient 6 M6
copier_images_du_patient(dossier_train, identifiant_Patient_6_M6, dossier_patient_6_M6)
copier_images_du_patient(dossier_test, identifiant_Patient_6_M6, dossier_patient_6_M6)