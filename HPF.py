import essentia.standard as es 
import csv
import numpy as np 
import json
import mir_eval
import os
import math
import averageResults


def HPFilter(audio,cutoff):

	HPF = es.HighPass(cutoffFrequency=cutoff)

	filtered_audio = HPF(audio)

	writer = es.MonoWriter(filename='holst_test.wav')

	writer(filtered_audio)

	return filtered_audio



def melody_extraction_melodia(audioPath,exportPath):

	listOfFiles = os.listdir(audioPath)

	for file in listOfFiles:
		if '.wav' not in file: continue
		if file.startswith('._'): continue

		# Loading audio
		audioLoader = es.EqloudLoader(filename=audioPath+file)
		audio = audioLoader()

		# Filter audio
		cutoff = 700
		newaudio = HPFilter(audio,cutoff)
		del audio
		audio = newaudio

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

def mirEval(refPath, estPath, pathJson):

	listOfRef = os.listdir(refPath) # GT path
	listOfEst = os.listdir(estPath) # melody estimation path

	for ref in listOfRef:
		if '.csv' not in ref: continue
		if ref.startswith('._'): continue

		# Read estimation and GT files
		print ref

		# Reference (GT)
		refData = []
		with open(refPath+ref, 'rb') as f:
			print refPath+ref
			reader = csv.reader(f)
			for line in reader: refData.append(line)
		refData = np.array(refData, dtype=float)

		# Estimation (predictions)
		estData = []
		with open(estPath+ref, 'rb') as f:
			reader = csv.reader(f)
			for line in reader: estData.append(line)
		estData = np.array(estData, dtype=float)

		## Evaluation metrics computation

		scores = mir_eval.melody.evaluate(refData[:,0], refData[:,1], estData[:,0], estData[:,1])

		# Export a json with the metrics for each audio file
		with open(pathJson+ref[:-3]+'json', 'w') as fp:
			json.dump(scores, fp)


	return 1


#======================================================================



refPath = '../Orchset/GT_csv/'
predPath = './filteringtest_orchset/'
# 
melody_extraction_melodia(audioPath,predPath)
pathJson = predPath+'jsonResults/' # export results path
mirEval(refPath,predPath,pathJson)
averageResults.main(pathJson)





