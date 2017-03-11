import csv
import os

def main(pathIn='../Orchset/GT_txt/',pathOut='../Orchset/GT_csv/'):
	listOfTxt = os.listdir(pathIn)
	for file in listOfTxt:

		if '.txt' not in file: continue

		txt_file = pathIn+file
		csv_file = pathOut+file[:-3]+'csv'


		in_txt = csv.reader(open(txt_file, 'rb'), delimiter = '\t')
		out_csv = csv.writer(open(csv_file, 'wb'))

		out_csv.writerows(in_txt)


main()
