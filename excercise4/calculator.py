print("===== Calculator =====")
x1 = int(input("Enter X1 : "))
x2 = int(input("Enter X2 : "))
sign = ["+", "-", "*", "/"]
typing = input("Select operator [+ - * /] : ")

class calculate():
  x1 = 0
  x2 = 0
  def __init__(self, in_x1, in_x2):
    self.x1 = in_x1
    self.x2 = in_x2

  def plus(self):
    result = self.x1 + self.x2
    print("Result is", self.x1 ,"+", self.x2 ,"=", result)
  def minus(self):
    result = self.x1 - self.x2
    print("Result is", self.x1 ,"-", self.x2 ,"=", result)
  def mul(self):
    result = self.x1 * self.x2
    print("Result is", self.x1 ,"x", self.x2 ,"=", result)
  def div(self):
    result = self.x1 / self.x2
    print("Result is", self.x1 ,"/", self.x2 ,"=", result)

cal = calculate(x1, x2)

if typing in sign:
  print()
  print(".....Calculating.....")
  print()
  if typing == "+":
    cal.plus()
  elif typing == "-":
    cal.minus()
  elif typing == "*":
    cal.mul()
  elif typing == "/":
    cal.div()
else:
  print()
  print("ERROR!...Please check operator agian!")
  print()
