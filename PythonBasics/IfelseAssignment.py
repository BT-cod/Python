import time
now = time.strftime('%H:%M:%S')
h = time.strftime('%H')
hour = int(h)
print(now)
if(hour < 11 and hour > 1):
        print("GOOD MORNING BROO..!")
elif(hour > 11 and hour < 17):
        print("GOOD AFTERNOON BROO..!")
elif(hour > 17 and hour < 23):
        print("GOOD EVENING BROO..!")
else :
        print("GOOD NIGHT BROO..!")