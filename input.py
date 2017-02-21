# input.py
# copy from jc -> paste in txt file -> run this with parameter
#
import sys
from pymongo import MongoClient
import csv
import commands
import json
import random
from itertools import islice

filename = str(sys.argv[1])

client = MongoClient()
jin = client['xscore'].jinput
db = client.xscore

def main():
	parse_record()

def parse_record():
	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		for row in reader:
			if row[0] == '1st leg':
				ran = str(random.random())[2:12]
				d1 = row[1]
				l1 = l_lookup(row[2],ran)
				hh1,aa1 = row[3].split(' vs ')
				h1,a1 = t_lookup(l1,hh1,aa1,ran)
				writeresult = jin.insert_one(
					{"rid": ran, "l1": {
						"date": d1,
						"league": row[2],
						"away": hh1,
						"home": aa1
					}}
				)
			elif row[0] == '2nd leg':
				d2 = row[1]
				l2 = l_lookup(row[2],ran)
				hh2,aa2 = row[3].split(' vs ')
				h2,a2 = t_lookup(l2,hh2,aa2,ran)
				writeresult = jin.update_one(
					{"rid": ran},
					{"$set": {"l2": {
						"date": d2,
						"league": row[2],
						"away": hh2,
						"home": aa2
						}}
					}
				)
			else:
				print("done")
		resu = d1.replace(" ","") + d2.replace(" ","") + "-" + ran
		commandline = "python cal2.py '" + l1 + "," + h1 + "," + a1 + "," + l2 + "," +h2+ "," +a2+ "' 1617 > result/" + resu + ".txt"
		commandlinet10 = "python cal2-t10.py '" + l1 + "," + h1 + "," + a1 + "," + l2 + "," +h2+ "," +a2+ "' 1617 > result/" + resu + "t10.txt"
		print commandline
		print commandlinet10

def l_lookup(l,ran):
	try:
		result = db.code.find_one({"jleague" : l},{"_id": 0, "code": 1})
		result = result["code"]
	except:
		print("Can't find league " + l)
		result = '<-----not found----->'
		writeresult = jin.update_one({"rid": ran},{"$set": {"flag": "notfound-l"}})

	return(result) 

def t_lookup(l,h,a,ran):
	try:
		h = db.code.find_one({"jteam": h},{"_id": 0, "xteam": 1})
		h = h["xteam"]
	except:
		print "Unexpected error:", sys.exc_info()
		print("Can't find " + h )
		h = '<-- not found -->'
		writeresult = jin.update_one({"rid": ran},{"$set": {"flag": "notfound-h"}})

	try:
		a =  db.code.find_one({"jteam": a},{"_id": 0, "xteam": 1})
		a = a["xteam"]
	except:
		print("Can't find "+ a)
		a = '<-- not found -->'
		writeresult = jin.update_one({"rid": ran},{"$set": {"flag": "notfound-a"}})

	return(h,a)

# call the main program
main()
