hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))
while True:
  if(hours<0 or hours>20 or minutes<0 or minutes>59):
    print("Invalid time.")
    break
  if(buyAmt>3000):
    print("No charge, thank you.")
    break
  a = hours+(minutes**(minutes//60))
  b = hours+(minutes/60)
  if(0<=minutes<=59 and hours>=0):
    if(hours==1 and minutes==0 or hours==1 and minutes>0):
      print("No charge, thank you.")
      break
    if(hours<=2 and minutes==0):
      print("No charge, thank you.")
      break
    elif(hours==2 and minutes>0):
      if(300<=buyAmt<=3000):
        print("No charge, thank you.")
        break
      if(buyAmt<300):
        print("Total amount due is 20 Baht, thank you.")
        break
    elif(3<=b<=4):
      if(300<=buyAmt<=3000):
        if(b==3 or b==4 and minutes==0):
          print("No charge, thank you.")
          break
        if(b>=3 and b<4 ):
          if(minutes>0):
            print("No charge, thank you.")
            break
        if(b==4 ):
          if(minutes>0):
            print("Total amount due is 50 Baht, thank you.")
            break
      elif(buyAmt<300):
        if(b==3 and minutes==0):
          print("Total amount due is 20 Baht, thank you.")
          break
        elif(b==3 and minutes>0):
          print("Total amount due is 40 Baht, thank you.")
          break
        elif(b==4 and minutes==0):
          print("Total amount due is 40 Baht, thank you.")
          break
        elif(b==4 and minutes>0):
          print("Total amount due is 90 Baht, thank you.")
          break
    else:
      if(300<=buyAmt<=3000):
        if(minutes==0):
          c = (50*(hours-4))
          print(f"Total amount due is {c:.0f} Baht, thank you.")
          break
        if(minutes>0):
          d = (50*(a-4))
          print(f"Total amount due is {d:.0f} Baht, thank you.")
          break
      elif(buyAmt<300):
        if(minutes==0):
          e = 40+(50*(hours-4))
          print(f"Total amount due is {e:.0f} Baht, thank you.")
          break
        if(minutes>0):
          f = 40+(50*(a-4))
          print(f"Total amount due is {f:.0f} Baht, thank you.")
          break