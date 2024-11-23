# get two numbers and math them!

def get_num():
  # I thought this was a clever way to keep the program running,
  # rather than killing the program and needing to run it again
  # when the input is wrong
  while True:
    num = input("Number please: ")
    try:
      return float(num)
    except:
      print("Pick a better number")

number_a = get_num()
number_b = get_num()
operand = input("What math do you want? ")

result = 0
if operand == "+":
  result = number_a + number_b
elif operand == "-":
  result = number_a - number_b
elif operand == "*":
  result = number_a * number_b
elif operand == "**":
  result = number_a ** number_b
elif operand == "/":
  if number_b != 0: 
    result = number_a / number_b
  else:
    print("Can't divide by zero. Sorry babe :(")
    raise SystemExit
elif operand == "%":
  if number_b != 0: 
    result = number_a % number_b
  else:
    print("Can't modulo by zero. Sorry babe :(")
    raise SystemExit
else:
  print("That's not how you math. Use + - * / % **")
  raise SystemExit

print(result)