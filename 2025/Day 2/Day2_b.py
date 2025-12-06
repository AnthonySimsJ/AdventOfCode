#! python3
#welp.. regex.. but still kinda brute force

import sys, re

inputString = sys.stdin.read().split(",")
answer = 0 
for rg in inputString:
   left, right = map(int,rg.split("-"))
   while left <= right:
      working = str(left)
      for i in range(2,len(str(right))+1):
         if(len(str(working))%i == 0):
            rs = re.compile(fr"({working[:len(working)//i]}){{{i}}}")
            if(rs.search(working)):
               answer += left
               break
      left += 1

print(answer)

