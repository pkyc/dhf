import re
import operator
import pandas as pd
from operator import itemgetter, attrgetter
from itertools import groupby
from prettytable import PrettyTable


jc_list = []

## calcuate the half score (1h) and final score(1f=1h+2h), group and sorted. ##
def buy(sorted_full_list):
	for i in range(20):
		jc = re.findall('\d',sorted_full_list[i][0])
		h1 = str(jc[0]+jc[1])
		h_f1 = str(int(jc[0])+int(jc[2]))
		a_f1 = str(int(jc[1])+int(jc[3]))
		h2 = str(jc[4]+jc[5])
		h_f2 = str(int(jc[4])+int(jc[6]))
		a_f2 = str(int(jc[5])+int(jc[7]))
		jc_list.append([i,h1,str(h_f1+a_f1),h2,str(h_f2+a_f2)])

	jc = pd.DataFrame(jc_list, columns = ['R','1h','1f','2h','2f'])

	for i in jc_list:
		a = 1
		#print(i)
	
	for k,g in jc.groupby(['1h','1f','2h','2f']):
		a = k[0]
		b = k[1]
		c = k[2]
		d = k[3]
		print(a,b,c,d)

	return()

