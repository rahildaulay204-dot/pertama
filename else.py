str_input = input('Enter your grade: ')
grage = int(str_input)

if grage == 100:
    print("perfect")
elif grage >= 85:
    print("awesome")
elif grage >= 65:
    print("passed the exam")
else:
  print("below the passing grade")

