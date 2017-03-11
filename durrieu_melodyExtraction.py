# -*- coding: utf-8 -*-
import numpy as np 
import subprocess
from os import listdir
import shutil


def melody_extraction(audioPath,predictionsPath):
	# The input audio path and the output path for the predictions need to be complete paths


	listOfAudio = listdir(audioPath)

	for file in listOfAudio:

		if '.wav' not in file: continue # avoid attempting to process non-audio files
		if '._' in file: continue

		predName = file[:-3]+'txt'

		# -n flag means no other output than the pitches
		# -p flag sets the output path for the pitch predictions
		subprocess.call('python2.6 separateLeadStereo/separateLeadStereoParam.py ' + audioPath+file + ' -p ' + predictionsPath+predName + ' -n', shell=True)


