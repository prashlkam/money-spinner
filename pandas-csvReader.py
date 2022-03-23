# csv reader using pandas module

# requires Anaconda 2 for pthon data science

import pandas as pnd

class pandas-csvReader:
	def ReadColFromCSV(csv_file, colToRead):
		filedata = pnd.read_csv(csv_file)
		colData = filedata[colToRead]
		return colData
