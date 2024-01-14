import os

OutputFileName = input("What would you like the file name to be?   ")
HasGivenQuestionNumber = False
while HasGivenQuestionNumber == False:
    TotalQuestions = input("How many questions do you want to make?  ")
    if TotalQuestions.isnumeric() == True:
        HasGivenQuestionNumber = True
        break
    else:
        print("Please input a number\n")
        
x = 0

outfile = open(OutputFileName+'.txt', 'x')
outfile.write('score = 0' + '\n')
outfile.write('total = '+ TotalQuestions + '\n')
outfile.close()

while x < int(TotalQuestions):

    IndexNumber = x+1
    StrIndexNumber = str(IndexNumber)
    CurrentQuestion = input("What do you want question "+StrIndexNumber+" to be?    ")
    CurrentAnswer = input("What do you want your answer to be?    ").lower()
    outfile = open(OutputFileName+'.txt', "a")
  
    outfile.write(
        'Answer'+StrIndexNumber+' = input("'+CurrentQuestion+' : ")' + '\n'+
        'if Answer'+StrIndexNumber+'.lower() =='+'"'+CurrentAnswer+'"'+':'+'\n'+
        '       print("Well done")'+'\n'+
        '       score = score + 1' + '\n'+
        'else:'+'\n'+
        '       print("Wrong answer!")'+'\n'
        )
        
    outfile.close()
    x = x + 1

outfile = open(OutputFileName+'.txt', 'a')
outfile.write('print("you scored ",score," out of ",total)' + '\n')
outfile.close()
os.rename(OutputFileName+'.txt',OutputFileName+'.py')
print(" Made by https://github.com/Auxy6858 ")
