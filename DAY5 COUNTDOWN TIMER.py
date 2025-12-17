#DAY 5: Countdown Timer
import time 
#Step 1 Take user input for where countdown should start
start = int(input ("Enter the number to start countdown from: "))
 
 #Step 2 Countdown using while loop: 
while start > 0:
    print(start)
    time.sleep(1)
    start = start -1
#Step 3: Print message when countdown is finished 
print("Countdown Complete!")
print("\n Happy New Year!")

