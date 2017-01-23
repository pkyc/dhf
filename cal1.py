# using Python 2 to run
#
import sys
import json
import math
import poi
import indexCal
import poiCal
import p56Cal
from pymongo import MongoClient
from decimal import *
from tabulate import tabulate
from prettytable import PrettyTable
from array import array

client = MongoClient()
db = client['xscore'].todos

league,home,away = raw_input().split(',')


################# step 1 calculate index #############################

# call def indexCal
tm_h,htg_h,shg_h,htl_h,shl_h,tm_a,htg_a,shg_a,htl_a,shl_a,hti_h,shi_h,hti_a,shi_a = indexCal.cal_index(league,home,away)


################# step 2 calculate poisson #############################

print tabulate([["team","role","matches","1st-h gain","2nd-h gain","1st-h loss","2nd-h loss","1st-h Index","2nd-h Index"],
	[home,"Home",tm_h,htg_h,shg_h,htl_h,shl_h,float(hti_h),float(shi_h)],
	[away,"Away",tm_a,htg_a,shg_a,htl_a,shl_a,float(hti_a),float(shi_a)]],
	headers="firstrow")

# call poiCal
t1 = PrettyTable(['score',home+" 1st", home+" 2nd", away+" 1st", away+" 2nd"])
res_a = poiCal.poiCal(hti_h,shi_h,hti_a,shi_a)

# return poiCal and print table
for i in range(8):
	t1.add_row([i, res_a[i][0],res_a[i][1],res_a[i][2],res_a[i][3]])

#print(t1)

sorted_ht_list,sorted_sh_list = p56Cal.p56Cal(res_a)

htsh_list = [("","")]

for h in sorted_ht_list:
   for a in sorted_sh_list:
      htsh_list.append((h[0]+a[0],(h[1]*a[1])))
      sorted_htsh_list = sorted(htsh_list, key=lambda x: x[1], reverse=True)

for item in sorted_htsh_list:
   print sorted_htsh_list.index(item), item

#for i in range(1000):
#   print i,sorted_htsh_list[i][0],sorted_htsh_list[i][1]

