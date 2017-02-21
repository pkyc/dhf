#
# parse the data from www.xscores.com
#
from datetime import datetime, date, time
import sys
import csv
import commands

filename = str(sys.argv[1])
year = str(sys.argv[2])

def main():
	#for afile in filelist:
	toCSV()
	print("END")

def toCSV():
	#filename = afile
	i=0
	league = filename[:-4]
	output = league+".out"
	with open(output, 'w+') as csvoutfile:
		writer = csv.writer(csvoutfile, delimiter=',')
		writer.writerow(['Date','Team','Role','league','fh','sh','fl','sl','checkid','year'])
		with open(filename) as csvfile:
			reader = csv.reader(csvfile,delimiter="\t")
			for row in reader:
				i=i+1
				if len(row) == 1:
					date = reDate(str(row[0]))
				else:
					home = row[4].title()
					away = row[7].title()
					half_h,half_a = row[10].split('-')
					final_h,final_a = row[11].split('-')
					writer.writerow([date,home.strip(),"home",league,half_h,int(final_h)-int(half_h),half_a,int(final_a)-int(half_a),i,year])
					writer.writerow([date,away.strip(),"away",league,half_a,int(final_a)-int(half_a),half_h,int(final_h)-int(half_h),i,year])

	commandline = "mongoimport -d xscore -c todos --type csv --headerline --file "+output
	genTeam(output)
	print commandline
	#commands.getstatusoutput(commandline)

def reDate(d):
	#shortdate = d[5:11].replace('.','')
	fulldate = datetime.strptime(d, '%Y-%m-%d')
	phasedate = fulldate.strftime('%d-%m-%Y')+"T00:00:00Z"
	return(phasedate)	

def genTeam(output):
	genteam = "awk -F',' '{print $2}' " + output + " | sort | uniq > "+ output[0:-4]+".team"
	commands.getstatusoutput(genteam)
	print output[0:-4]+".team generated!"
	return()

	
main()
