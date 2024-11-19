# a quick and dirty python timer
import time

def timer():
  duration = int(input("How may seconds: "))
  start = input("Type 'go' to start: ")
  if start == "go":
    print("TIMER STARTED")
    print("=============")
    # do timer stuff
    i = 0
    while i < duration:
      print(i)
      time.sleep(1)
      i += 1
      if i == duration:
        print("DONE")
  else:
    print("try again...")
    

timer()