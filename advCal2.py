# using Python 2 to run
#
import sys
import json
import math
import poi
import indexCal
import poiCal
import p56Cal
import jcCal
from pymongo import MongoClient
from decimal import *
from tabulate import tabulate
from prettytable import PrettyTable
from array import array

client = MongoClient()
db = client['xscore'].todos

def main():
	rawinput = str(sys.argv[1])
	#rawinput = raw_input()
	print(rawinput)
	league1,home1,away1,league2,home2,away2 = rawinput.split(',')

	## step 1 calculate index ##
	tm_h1,htg_h1,shg_h1,htl_h1,shl_h1,tm_a1,htg_a1,shg_a1,htl_a1,shl_a1,hti_h1,shi_h1,hti_a1,shi_a1 = indexCal.cal_index(league1,home1,away1)
	tm_h2,htg_h2,shg_h2,htl_h2,shl_h2,tm_a2,htg_a2,shg_a2,htl_a2,shl_a2,hti_h2,shi_h2,hti_a2,shi_a2 = indexCal.cal_index(league2,home2,away2)

	## call poiCal ##
	res_a1 = poiCal.poiCal(hti_h1,shi_h1,hti_a1,shi_a1)
	res_a2 = poiCal.poiCal(hti_h2,shi_h2,hti_a2,shi_a2)

	## step 3 calculate each score possibility  ##
	sorted_ht_list1,sorted_sh_list1 = p56Cal.p56Cal(res_a1)
	sorted_ht_list2,sorted_sh_list2 = p56Cal.p56Cal(res_a2)

	## combine half-time and second-half , then sort ##
	htsh_list1 = [("","")]
	for h in sorted_ht_list1:
		for a in sorted_sh_list1:
			htsh_list1.append((h[0]+a[0],(h[1]*a[1])))
			sorted_htsh_list1 = sorted(htsh_list1, key=lambda x: x[1], reverse=True)

	htsh_list2 = [("","")]
	for h in sorted_ht_list2:
		for a in sorted_sh_list2:
			htsh_list2.append((h[0]+a[0],(h[1]*a[1])))
			sorted_htsh_list2 = sorted(htsh_list2, key=lambda x: x[1], reverse=True)

	## combine 1st leg and 2nd leg, then sort ##
	sorted_htsh_list1.remove(("",""))
	sorted_htsh_list2.remove(("",""))

	full_list = [("","")]
	for each1 in sorted_htsh_list1:
		for each2 in sorted_htsh_list2:
			full_list.append((each1[0]+each2[0],(each1[1]*each2[1]))) 

	sorted_full_list = sorted(full_list, key=lambda x: x[1], reverse=True)

	## temporary disable printout ##
	for i in range(20):
		print i, sorted_full_list[i][0], sorted_full_list[i][1]
	sorted_full_list.pop(0)
	jcCal.buy(sorted_full_list)

main()
