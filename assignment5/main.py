

while True:
  print("============= Welcome to Calculator =============")
  select = input("[sign up/sign in] > ")
  if select == "sign up":
    print()
    print("========== Sign up ==========") 

    while True:
      fname = input("Insert Firstname : ")
      if fname != "":
        break
      else:
        print("--- ALERT! Please insert Firstname")
        print()

    while True:
      lname = input("Insert Lastname  : ")
      if lname != "":
        break
      else:
        print("--- ALERT! Please insert Lastname")
        print()

    while True:
      user = input("Insert Username  : ")
      if user != "":
        break
      else:
        print("--- ALERT! Please insert Username")
        print()

    while True:
      password = input("Insert Password  : ")
      if password != "":
        break
      else:
        print("--- ALERT! Please insert password")
        print()

    while True:
      confirm_password = input("Confirm Password : ")
      if confirm_password == "":
        print("--- Please insert Confirm password")
        print()
      elif password != confirm_password:
        print("--- Password do not match, Please check password again")
        print()
      else:
        break

    while True:
      email = input("Insert Email     : ")
      if email != "":
        break
      else:
        print("--- ALERT! Please insert Email")
        print()

    print()
    print("------------- Sign up SUCCESS! --------------")
    print("Name     : ",fname," ",lname)
    print("Username : ",user)
    print("Password : ",password)
    print("Email    : ",email)
    print()
    print(">>> Enjoy your mind to programing <<<")
    print("---------------------------------------------")
    print()
  elif select == "sign in":
    print()
    print("=================================================")
    while True:
      login = input("Username : ")
      if login == "":
        print("--- ALERT! Please insert username")
        print()
      elif login != user:
        print("--- ALERT! Don't have user in Authentication, Please sign up before")
        print()
      elif login == user:
        break
    
    while True:
      login_pass = input("Password : ")
      if login_pass == "":
        print("--- ALERT! Please insert password")
        print()
      elif login_pass != password:
        print("--- ALERT! Don't have user in Authentication, Please sign up before")
        print()
      elif login_pass == password:
        print()
        print("----------------------------")
        print("       Login Success")
        print("----------------------------")
        print()
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
          print("ERROR!...Please check operator again!")
          print()
        break
  else:
    print("--- ALERT! check contruction again")
    print()
