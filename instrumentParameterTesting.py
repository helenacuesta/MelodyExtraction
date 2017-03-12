import csv
import essentia
import essentia.standard
import melodia_mirEval

# change root directoy
rootdir = '/Users/joemunday/Documents/UPF\ Masters\ 1617/MIR/ParameterTuning'
#change file to instrument family csv
instrumentFamilies = csv.DictReader(open(rootdir+'/InstrumentClassification.csv'))

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print os.path.join(subdir, file)
        if "wav" in os.path.join(subdir, file):
        	loader = essentia.standard.MonoLoader(filename=os.path.join(subdir, file))
			audio = loader()
        	if instrumentFamilies[file] == 'Brass':
        		#parameters for brass
        		melodia = essentia.standard.PitchMelodia(
        			harmonicWeight=0.8,
        			magnitudeCompression=1,
        			magnitudeThreshold=40,
        			maxFrequency=4000,
        			minDuration=100,
        			minFrequency=100,
        			numberHarmonics=20,
        			peakDistributionThreshold=0.9,
        			peakFrameThreshold=0.9,
        			pitchContinuity=27.5625,
        			referenceFrequency=55,
        			timeContinuity=100,
        			)
        	elif instrumentFamilies[file] == 'Woodwind':
        		melodia = essentia.standard.PitchMelodia(
        			harmonicWeight=0.8,
        			magnitudeCompression=1,
        			magnitudeThreshold=40,
        			maxFrequency=4000,
        			minDuration=100,
        			minFrequency=100,
        			numberHarmonics=20,
        			peakDistributionThreshold=0.9,
        			peakFrameThreshold=0.9,
        			pitchContinuity=27.5625,
        			referenceFrequency=55,
        			timeContinuity=100,
        			)
        	elif instrumentFamilies[file] == 'Strings':
        		mmelodia = essentia.standard.PitchMelodia(
        			harmonicWeight=0.8,
        			magnitudeCompression=1,
        			magnitudeThreshold=40,
        			maxFrequency=4000,
        			minDuration=100,
        			minFrequency=100,
        			numberHarmonics=20,
        			peakDistributionThreshold=0.9,
        			peakFrameThreshold=0.9,
        			pitchContinuity=27.5625,
        			referenceFrequency=55,
        			timeContinuity=100,
        			)
        	else:
        		# Default parameters
        		melodia = essentia.standard.PitchMelodia(
        			harmonicWeight=0.8,
        			magnitudeCompression=1,
        			magnitudeThreshold=40,
        			maxFrequency=4000,
        			minDuration=100,
        			minFrequency=100,
        			numberHarmonics=20,
        			peakDistributionThreshold=0.9,
        			peakFrameThreshold=0.9,
        			pitchContinuity=27.5625,
        			referenceFrequency=55,
        			timeContinuity=100,
        			)

    pitch,pitchconfidence = melodia(audio)


#evaluation

melodia_mirEval.mirEval(pathRef=rootdir+'/GT',pathEst=rootdir+'/Estimations',pathJson=rootdir+'/Evaluations')