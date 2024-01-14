score = 0
total =3
Answer1 = input("What's the capital of France : ")
if Answer1.lower() =="paris":
       print("Well done")
       score = score + 1
else:
       print("Wrong answer!")
Answer2 = input("What's 1+1 : ")
if Answer2.lower() =="2":
       print("Well done")
       score = score + 1
else:
       print("Wrong answer!")
Answer3 = input("Is java ass? : ")
if Answer3.lower() =="yes":
       print("Well done")
       score = score + 1
else:
       print("Wrong answer!")
print("you scored ",score," out of ",total)
