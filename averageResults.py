import json
import numpy as np 
import csv
import os

def readJson(path):
	with open(path) as data_file:
		data = json.load(data_file)
	return data


def parseValues(data):
	
	VR = data['Voicing Recall']
	RCA = data['Raw Chroma Accuracy']
	OA = data['Overall Accuracy']
	RPA = data['Raw Pitch Accuracy']
	VFA = data['Voicing False Alarm']

	return VR,RCA,OA,RPA,VFA

def main(path):

	# path is the directory where the json files with the evaluation metrics are stored

	listOfFiles = os.listdir(path)

	output = np.array(['Voicing Recall', 'Voicing False Alarm', 'Raw Pitch Accuracy', 'Raw Chroma Accuracy', 'Overall Accuracy']).reshape([1,5])

	for file in listOfFiles:
		if 'json' not in file: continue

		data = readJson(path+file)
		vr,rca,oa,rpa,vfa = parseValues(data)

		output = np.concatenate([output, np.array([vr,vfa,rpa,rca,oa]).reshape(1,5)], axis=0)

	output = np.array(output)

	with open(path+'overallResults.csv','wb') as f:
		writer = csv.writer(f)
		for line in output: writer.writerow(line)




