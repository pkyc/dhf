import poi

def poiCal(hti_h,shi_h,hti_a,shi_a):
   res_a = [[0 for x in range(4)] for y in range(8)]
   for i in range(8):
       result_ht_h = poi.poisson_probability(i,float(hti_h))
       result_sh_h = poi.poisson_probability(i,float(shi_h))
       result_ht_a = poi.poisson_probability(i,float(hti_a))
       result_sh_a = poi.poisson_probability(i,float(shi_a))
       res_a[i]= [result_ht_h,result_sh_h, result_ht_a, result_sh_a]
       #t1.add_row([i, result_ht_h, result_sh_h, result_ht_a, result_sh_a])
   return res_a 
 

