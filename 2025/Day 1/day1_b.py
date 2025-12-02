import sys

cur_pos = 50
answer = 0   
        
for movement in sys.stdin:
    direction = movement[0]
    rotation = int(movement[1:])
    
    last_pos = cur_pos
    answer+= rotation//100
  
    if (direction == 'R'):
        cur_pos = last_pos + rotation
        if(last_pos != 0 and last_pos + rotation%100> 100):
            answer+=1
    else:
        cur_pos = last_pos - rotation
        if(last_pos != 0 and last_pos - rotation%100<0):
            answer+=1
    cur_pos = cur_pos%100
    if (cur_pos%100 ==0 and last_pos != 0):
        answer +=1
    
print(answer)