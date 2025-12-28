# python program to create a expense tracker
while True :
  print("hy user you can track your expense here\n Choose a option below from the menu \n 1> Add expense \n 2> show expense \n 3> show total expense\n 4> exited from the menu")
  a=int(input("enter a number from the menu : "))

  if(a==1):
   print("program for add expenses")
   b=input("Enter the amount:")
   c=input("Enter the category of expense:")
   with open ("data.txt","a")as file:
    file.write(b+","+c+"\n") 
   print("expenses saved succesfully")

  elif(a==2):
   print("program for show expenses")
   with open("data.txt", "r") as file:
            for line in file:
                amount, category = line.strip().split(",")
                print("Amount:", amount, "| Category:", category)
  elif(a==3):
    total=0
    print('python program to add total expesnses')
    with open("data.txt",'r')as file:
       for line in file:
        amount,category=line.strip().split(",")
        d=int(amount)
        total=total+d
    print(f"the total expense are {total}")

  elif(a==4):
   break
print("you have sussesfully exited the menu ")
