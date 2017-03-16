import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import melodia_evaluation_joe
import os
import averageResults

rootdir = '/Users/joemunday/Documents/UPF Masters 1617/MIR/ParameterTuning/Estimations'
gtpath = '/Users/joemunday/Documents/UPF Masters 1617/MIR/ParameterTuning/GT_csv/'
for subdir, dirs, files in os.walk(rootdir):
	for directory in dirs:
		estPath = rootdir + '/' + directory+ '/'
		pathJson = rootdir+ '/' + directory+'/evaluation/'
		if not os.path.exists(pathJson):
				os.makedirs(pathJson)

		print pathJson
		print 'estpath'
		print estPath
		melodia_evaluation_joe.mirEval(gtpath,estPath,pathJson)
		averageResults.main(pathJson)