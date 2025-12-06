#! python3 

import sys,time
joltage = 0 
for bank in sys.stdin:
    bl = [int(i) for i in bank.strip()]
    sbl = bl[:]
    mi = 0 
    for i in range (12,0,-1):
        max_index = len(sbl)+1
        di = sbl.index(max(sbl[mi:max_index-i]))
        joltage += (sbl[di] * (10**(i-1)))
        sbl = sbl[di+1:]      
print(joltage)

        
        


