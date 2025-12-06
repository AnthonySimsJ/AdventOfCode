#! python3

import sys
joltage = 0 
for bank in sys.stdin:
    bl = [int(i) for i in bank.strip()]
    ti = bl.index(max(bl[0:-1]))
    oi = bl.index(max(bl[ti+1:]))
    joltage += bl[ti]*10
    joltage += bl[oi]
print(joltage)