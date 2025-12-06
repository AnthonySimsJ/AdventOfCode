#! python3
#good ol brute force

import sys

inputString = sys.stdin.read().split(",")
answer = 0 
for rg in inputString:
   left, right = map(int,rg.split("-"))
   while left <= right:
      working = str(left)
      if(len(working)%2==0):
        if(working[len(working)//2:] == working[:len(working)//2] ):
           answer += left
      left +=1
print(answer)