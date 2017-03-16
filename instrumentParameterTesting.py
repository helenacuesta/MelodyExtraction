import csv
# import melodia_evaluation
import numpy as np
import csv
import os
import mir_eval
import math
import json
# import txt2csv
import averageResults
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import essentia
import essentia.standard

# change root directoy
rootdir = '/Users/joemunday/Documents/UPF Masters 1617/MIR/ParameterTuning'
exportPath = rootdir+'/Estimations/'
#change file to instrument family csv
instrumentFamiliesCSV = csv.DictReader(open(rootdir+'/InstrumentClassification.csv'))
instrumentFamilies= {}
for row in instrumentFamiliesCSV:
	instrumentFamilies[row['File Name']] = row['Predominant Family'];

peakFrameThresholdTestParams = [0.9,0.95,1.0]
peakDistributionTestParams = [0.9,1.0,1.5,2.0]

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		# print os.path.join(subdir, file)
		if "wav" in os.path.join(subdir, file):
			for peakFrameThreshold in peakFrameThresholdTestParams:
				for peakDistribution in peakDistributionTestParams:
					loader = essentia.standard.MonoLoader(filename=os.path.join(subdir, file))
					audio = loader()
					L = (len(audio)) / 44100.0 # seconds
					H = 441 # 10 ms for evaluation
					if instrumentFamilies[file] == 'Brass':
						#parameters for brass
						melodia = essentia.standard.PredominantPitchMelodia(
							hopSize=H,
							harmonicWeight=0.8,
							magnitudeCompression=1,
							magnitudeThreshold=40,
							maxFrequency=4000,
							minDuration=100,
							minFrequency=100,
							numberHarmonics=20,
							peakDistributionThreshold=peakDistribution,
							peakFrameThreshold=peakFrameThreshold,
							pitchContinuity=27.5625,
							referenceFrequency=55,
							timeContinuity=100,
							voicingTolerance=0.2,
							)
					elif instrumentFamilies[file] == 'Woodwind':
						melodia = essentia.standard.PredominantPitchMelodia(
							hopSize=H,
							harmonicWeight=0.8,
							magnitudeCompression=1,
							magnitudeThreshold=40,
							maxFrequency=4000,
							minDuration=100,
							minFrequency=100,
							numberHarmonics=20,
							peakDistributionThreshold=peakDistribution,
							peakFrameThreshold=peakFrameThreshold,
							pitchContinuity=27.5625,
							referenceFrequency=55,
							timeContinuity=100,
							voicingTolerance=0.2,
							)
					elif instrumentFamilies[file] == 'Strings':
						melodia = essentia.standard.PredominantPitchMelodia(
							hopSize=H,
							harmonicWeight=0.8,
							magnitudeCompression=1,
							magnitudeThreshold=40,
							maxFrequency=4000,
							minDuration=100,
							minFrequency=100,
							numberHarmonics=20,
							peakDistributionThreshold=peakDistribution,
							peakFrameThreshold=peakFrameThreshold,
							pitchContinuity=27.5625,
							referenceFrequency=55,
							timeContinuity=100,
							voicingTolerance=0.2,
							)
					else:
						# Default parameters
						melodia = essentia.standard.PredominantPitchMelodia(
							hopSize=H,
							harmonicWeight=0.8,
							magnitudeCompression=1,
							magnitudeThreshold=40,
							maxFrequency=4000,
							minDuration=100,
							minFrequency=100,
							numberHarmonics=20,
							peakDistributionThreshold=peakDistribution,
							peakFrameThreshold=peakFrameThreshold,
							pitchContinuity=27.5625,
							referenceFrequency=55,
							timeContinuity=100,
							voicingTolerance=0.2,
							)

					pitch,pitchconfidence = melodia(audio)
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

					updateExportPath = exportPath+'-pdt:'+str(peakDistribution)+'-pft:'+str(peakFrameThreshold)+'/'
					
					if not os.path.exists(updateExportPath):
    						os.makedirs(updateExportPath)
					
					with open(updateExportPath+exportFilename,'wb') as f:
						print f
						writer = csv.writer(f)
						for line in pitchExp: writer.writerow(line)

					print(file + ' computed and exported!')


# #evaluation

# melodia_evaluation.mirEval(pathRef=rootdir+'/GT',pathEst=rootdir+'/Estimations',pathJson=rootdir+'/Evaluations')