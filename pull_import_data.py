#!/usr/bin/python3
import requests
import os
import pandas as pd



def get_data():
	url = 'https://archive.org/download/201309_foursquare_dataset_umn/fsq.zip'

	print('Do you want to download the data (total of 1.2GB) to current directory? (Y/N)')
	u_input = input()
	if (u_input == 'y') or (u_input == 'Y'):
		cwd = os.getcwd()
		print('Downloading data to ' + cwd)

		print("downloading with requests")
		r = requests.get(url)
		with open("fsq.zip", "wb") as code:
		    code.write(r.content)
		os.system('unzip ./fsq.zip')
		os.system('mv ./umn_foursquare_datasets ./fsq_data')
	else:
		print('script terminated, no data downloaded')

def dat_to_csv():
	os.chdir('./fsq_data')
	cwdir = os.getcwd()
	files = os.listdir('.')


	for x in files:
		if x != ".DS_Store":
		    df = pd.read_csv(cwdir + '/' + x, delimiter = "|", skiprows=[1])
		    print(x, " dataframe read in with length: \t")
		    print(len(df[:-1]), "\n")
		    print("Expected: ", df.iloc[-1])

		    #clip of .dat for .csv
		    df[:-1].to_csv(x[:-4] + ".csv")

#requires sudo
# def initialize_mongodb():
# 	if os.path.lexists('/data/db'):
# 		os.system('mongod')
#
# 	else:
# 		os.system('mkdir /data')
# 		os.system('mkdir /data/db')
# 		os.system('mongod')


# find + replace C:\Users\peter\Dropbox\SMU\7330_dbmgmt\project1\fsq\umn_foursquare_datasets\ with location of your CSVs


def add_to_mongo():
	os.system('find . -name "*.dat" -type f -delete')
	import_one = '"mongoimport" --host localhost --port 27017 --db dbmg --collection '
	import_two = ' --type csv --headerline --file '
	files = os.listdir('.')
	for csv in files:
		stop = csv.find('.')
		os.system(import_one + str(csv[:stop]) + import_two + csv)

get_data()

dat_to_csv()

add_to_mongo()
