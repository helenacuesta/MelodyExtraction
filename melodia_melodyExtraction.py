# -*- coding: utf-8 -*-

### MELODY EXTRACTION 

import essentia.standard as es
import numpy as np 
import csv
import os
import mir_eval
import math
import json

def melody_extraction_melodia(audioPath,exportPath):

# Predominant pitch extraction using MELODIA[1] (implementation from Essentia[2])
# The audioPath input variable is the path of the audio files we want to extract the pitch of

# [1] J. Salamon and E. Gomez, "Melody Extraction from Polyphonic Music Signals using Pitch Contour Characteristics", 
# IEEE Transactions on Audio, Speech and Language Processing, 20(6):1759-1770, Aug. 2012.
# [2] Bogdanov, D., Wack N., Gomez E., Gulati S., Herrera P., Mayor O., et al. (2013). ESSENTIA: an Audio Analysis Library for
# Music Information Retrieval. International Society for Music Information Retrieval Conference (ISMIR'13). 493-498.


	listOfFiles = os.listdir(audioPath)

	for file in listOfFiles:
		if '.wav' not in file: continue
		if file.startswith('._'): continue

		# Loading audio
		audioLoader = es.EqloudLoader(filename=audioPath+file)
		audio = audioLoader()

		if '_MIX' in file:
			file = file[:-8]+'.wav' # handle MedleyDB with original names

		L = (len(audio)) / 44100.0 # seconds
		H = 441 # 10 ms for evaluation
		
		# MELODIA algorithm
		melodia = es.PredominantPitchMelodia(hopSize=H)
		[pitch,confidence] = melodia(audio)
		pitch = np.array(pitch)

		N = pitch.shape[0]

		# Create time vector for output format
		time = []
		k = 0
		for i in range(N):
			time.append(round(k,2))
			k+=0.01
		
		time = np.array(time)

		pitchExp = np.zeros([N,2])
		pitchExp[:,0] = time
		pitchExp[:,1] = pitch
		pitchExp = np.reshape(pitchExp, [N,2])

		# Export predictions
		# path to save files with predictions
		exportFilename = file[:-3]+'csv'

		
		with open(exportPath+exportFilename,'wb') as f:
			writer = csv.writer(f)
			for line in pitchExp: writer.writerow(line)

		print(file + ' computed and exported!')



def main(audioPath,exportPath):
	melody_extraction_melodia(audioPath,exportPath)









