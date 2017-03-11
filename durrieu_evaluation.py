# -*- coding: utf-8 -*-
import numpy as np
import csv
import os
import json
import mir_eval
import txt2csv
import averageResults

def mirEval(refPath, estPath, pathJson):

# Given the melody estimations (in the format <time,pitch>) and the ground truth, evaluate the performance
# of the pitch estimation algorithms. 
# The evaluation metrics are extracted using the mir_eval library [3], and the metrics that are used follow
# the MIREX guidelines.
# This code assumes the files to be .csv. If you have .txt files, use the script txt2csv.py
	
# [3] Colin Raffel, Brian McFee, Eric J. Humphrey, Justin Salamon, Oriol Nieto, Dawen Liang, and Daniel P. W. Ellis, 
# mir_eval: A Transparent Implementation of Common MIR Metrics", Proceedings of the 15th International Conference on 
# Music Information Retrieval, 2014.

	listOfRef = os.listdir(refPath) # GT path
	listOfEst = os.listdir(estPath) # melody estimation path

	for ref in listOfRef:
		if '.csv' not in ref: continue
		if ref.startswith('._'): continue
		print ref

		# Read reference (ground truth GT)
		refData = []
		with open(refPath+ref, 'rb') as f:
			reader = csv.reader(f)
			for line in reader: refData.append(line)
		refData = np.array(refData, dtype=float)

		# Read predictions txt files

		if ref[:-4]+'.txt' in os.listdir(estPath): # Durrieu's method did not work for all the files, evaluate only the ones that worked

			estData = []
			with open(estPath+ref[:-4]+'.txt', 'rb') as f:
				for line in f: 
					words = line.split(" ")
					estData.append(words)

			estData = np.array(estData,dtype=np.float32)



			## Evaluation metrics

			scores = mir_eval.melody.evaluate(refData[:,0], refData[:,1], estData[:,0], estData[:,1])

			# Export a json with the metrics for each audio file
			with open(pathJson+ref[:-3]+'json', 'w') as fp:
				json.dump(scores, fp)

	return 1

def main(refPath,predPath):

	jsonPath = predPath+'jsonResults/' # export results path
	txt2csv.main(predPath,predPath)

	mirEval(refPath,predPath,jsonPath)
	averageResults.main(jsonPath)



