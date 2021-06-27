def circle():
  diameter = int(input("input the diameter "))
  radius = diameter/2
  area = 3.14*radius**2
  circumference = 3.14*diameter
  print(radius)
  print(area)
  print(circumference)


def add():
  num1 = int(input("number 1"))
  num2 = int(input("number 2"))
  ans = num1+num2
  print(ans)

def convert_temp():
  fahrenheit = int(input("input heat in f"))
  cel = (fahrenheit - 32) * (5/9)
  print(cel)

def h_and_w():
  height = int(input("input height in inches "))
  weight = int(input("input weigth in stone"))
  h_ans = height*2.54
  w_ans = weight = weight*6.364
  print(h_ans)
  print(w_ans)

def menu():
  print("1.circle, 2. addition,3.temp,4.height and weight")
  ans = int(input())
  if ans == 1:
    circle()
  elif ans == 2:
    add()
  elif ans == 3:
    convert_temp()
  elif ans ==4:
    h_and_w()
  else:
    print("invalid number")
    menu()

menu()

