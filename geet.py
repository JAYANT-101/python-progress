import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
if(timestamp>8):
    print("good night")
elif(6<timestamp>8):
    print("good evening")
elif(timestamp>6):
    print("good morning")