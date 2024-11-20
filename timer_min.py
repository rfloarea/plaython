# TODO: Pause/Resume function
# TODO: Stop function

import time

def timer():
  duration = int(input("How many minutes: "))
  start = input("Type 'go' to start: ")
  if start == "go":
    txt = f"{duration} MIN TIMER STARTED"
    print(txt)
    print(len(txt) * "=")
    i = 0
    while i < duration:
      print(i)
      time.sleep(10)
      i += 1
    print("DONE")

timer()