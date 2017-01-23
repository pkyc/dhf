# using Python 2 to run
#
import sys
import json
import math
from pymongo import MongoClient
from decimal import *
from array import array
from tabulate import tabulate
from prettytable import PrettyTable

client = MongoClient()
db = client['xscore'].todos

def cal_index(league,home,away):
	pipeline_h = [ {"$match": {"Team": home, "Role": "home", "league": league}}, {"$group": {"_id": home, "totalMatch": {"$sum": 1 },  "fh": {"$sum": "$fh" }, "sh": {"$sum": "$sh" }, "fl": {"$sum": "$fl" }, "sl": {"$sum": "$sl" }} } ]
	pipeline_a = [ {"$match": {"Team": away, "Role": "away", "league": league}}, {"$group": {"_id": away, "totalMatch": {"$sum": 1 },  "fh": {"$sum": "$fh" }, "sh": {"$sum": "$sh" }, "fl": {"$sum": "$fl" }, "sl": {"$sum": "$sl" }} } ]
	#home
	result_h = list(db.aggregate(pipeline_h))
	tm_h  = result_h[0]['totalMatch']
	htg_h = result_h[0]['fh']
	shg_h = result_h[0]['sh']
	htl_h = result_h[0]['fl']
	shl_h = result_h[0]['sl']
	#away 
	result_a = list(db.aggregate(pipeline_a))
	tm_a  = result_a[0]['totalMatch']
	htg_a = result_a[0]['fh']
	shg_a = result_a[0]['sh']
	htl_a = result_a[0]['fl']
	shl_a = result_a[0]['sl']
	# i stands for index
	hti_h = Decimal(htg_h+htl_a)/Decimal(tm_h+tm_a)
	shi_h = Decimal(shg_h+shl_a)/Decimal(tm_h+tm_a)
	hti_a = Decimal(htg_a+htl_h)/Decimal(tm_h+tm_a)
	shi_a = Decimal(shg_a+shl_h)/Decimal(tm_h+tm_a)
	# index_list
	index_list = (tm_h,htg_h,shg_h,htl_h,shl_h,tm_a,htg_a,shg_a,htl_a,shl_a,hti_h,shi_h,hti_a,shi_a)
	# print table
	print tabulate([["team","role","matches","1st-h gain","2nd-h gain","1st-h loss","2nd-h loss","1st-h Index","2nd-h Index"],
        [home,"Home",tm_h,htg_h,shg_h,htl_h,shl_h,float(hti_h),float(shi_h)],
        [away,"Away",tm_a,htg_a,shg_a,htl_a,shl_a,float(hti_a),float(shi_a)]],headers="firstrow")
	#t1 = PrettyTable(['score',home+" 1st", home+" 2nd", away+" 1st", away+" 2nd"])

	return index_list
# end


