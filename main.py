# -*- coding: utf-8 -*-

import melodia_melodyExtraction
import melodia_evaluation
import durrieu_melodyExtraction
import durrieu_evaluation
import averageResults

'''

The following code performs the melody extraction using MELODIA [1] and Source/filter model by Durrieu [2] in Orchset and MedleyDB datasets
and evaluates the results using the Python mir_eval library [3].


The directories in the code are local, so you will need to change them. 
* Datasets: MedleyDB [4] and Orchset [5]
* Python requirements:
- Python2.6 and 2.7 distributions
- json, csv, numpy, essentia

Last modified on Sat. March 11th 2017

Owners: Helena Cuesta and Joe Munday
Contact e-mail: helena -DOT- cuesta01 -AT- estudiant -DOT- upf -DOT - edu

[1] J. Salamon and E. Gomez, "Melody Extraction from Polyphonic Music Signals using Pitch Contour Characteristics", 
IEEE Transactions on Audio, Speech and Language Processing, 20(6):1759-1770, Aug. 2012.

[2] Durrieu, J., & David, B. (2010). Source / Filter Model for Unsupervised Main Melody, 18(3), 1–12.

[3] Colin Raffel, Brian McFee, Eric J. Humphrey, Justin Salamon, Oriol Nieto, Dawen Liang, and Daniel P. W. Ellis, 
 mir_eval: A Transparent Implementation of Common MIR Metrics", Proceedings of the 15th International Conference on 
 Music Information Retrieval, 2014.

 [4] Bittner, R., Salamon, J., Tierney, M., Mauch, M., Cannam, C., & Bello, J. (2014). MedleyDB: A multitrack dataset for annotation - 
 intensive mir research. International Society for Music Information Retrieval Conference, 155–160.

 [5] Bosch, J. J., Marxer, R., & Gómez, E. (2016). Evaluation and combination of pitch estimation methods for melody extraction in symphonic 
 classical music. Journal of New Music Research, 45(2), 101–117. https://doi.org/10.1080/09298215.2016.1182191

'''


#==============================
# MELODIA with ORCHSET DATASET
#==============================

audioPath = '../Orchset/audio/mono/'
predPath = './MELODIAResults/'

# Melody extraction
melodia_melodyExtraction.main(audioPath,predPath)

# # Evaluation
GTPath = '../Orchset/GT_csv/'
melodia_evaluation.main(GTPath,predPath)

#=================================
# MELODIA with MEDLEYDB DATASET
#=================================

audioPath = '/Volumes/HCM2T/SMC/MedleyDB/Audio/MIX/'
predPath = '/Volumes/HCM2T/SMC/MedleyDB/Annotations/MELODIA_metrics/MELODIAResults/'

# Melody extraction
melodia_melodyExtraction.main(audioPath,predPath)

# ---------------------------------------
# Evaluation using MELODY1 annotations
# ---------------------------------------

GTPath = '/Volumes/HCM2T/SMC/MedleyDB/Annotations/Melody_Annotations/MELODY1/'
melodia_evaluation.main(GTPath,predPath)

# ---------------------------------------
# Evaluation using MELODY2 annotations
# ---------------------------------------

GTPath = '/Volumes/HCM2T/SMC/MedleyDB/Annotations/Melody_Annotations/MELODY2/'
melodia_evaluation.main(GTPath,predPath)



#==============================
# DURRIEU with ORCHSET DATASET
#==============================

audioPath = '../Orchset/audio/mono/'
predPath = './DurrieuResults/'

durrieu_melodyExtraction.melody_extraction(audioPath,predPath)

# Evaluation

GTPath = '../Orchset/GT_csv/'
durrieu_evaluation.main(GTPath,predPath)

#===============================
# DURRIEU with MEDLETDB DATASET
#===============================

audioPath = '/Volumes/HCM2T/SMC/MedleyDB/Audio/MIX/'
predPath = '/Volumes/HCM2T/SMC/MedleyDB/Annotations/Durrieu_metrics/DurrieuResults/'

durrieu_melodyExtraction.melody_extraction(audioPath,predPath)

# ---------------------------------------
# Evaluation using MELODY1 annotations
# ---------------------------------------

GTPath = '/Volumes/HCM2T/SMC/MedleyDB/Annotations/Melody_Annotations/MELODY1/'
durrieu_evaluation.main(GTPath,predPath)


# ---------------------------------------
# Evaluation using MELODY2 annotations
# ---------------------------------------

GTPath = '/Volumes/HCM2T/SMC/MedleyDB/Annotations/Melody_Annotations/MELODY2/'
durrieu_evaluation.main(GTPath,predPath)



