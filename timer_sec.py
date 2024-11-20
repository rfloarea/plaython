# TODO: Pause/Resume function
# TODO: Stop function

import time

def timer():
  duration = int(input("How many seconds: "))
  start = input("Type 'go' to start: ")
  if start == "go":
    txt = f"{duration} SEC TIMER STARTED"
    print(txt)
    print(len(txt) * "=")
    i = 0
    while i < duration:
      print(i)
      time.sleep(1)
      i += 1
    print("DONE")
  else:
    print("try again...")

timer()