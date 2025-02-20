
#Q1
name=input("what is your name")
print(name)
print("hello"+ name)

Id=input("what is your Student ID")
print(Id)
print("your ID is"+ Id)

#Q2
var1=input("enter a number :")
var2=input("enter another number :")
sum= int(var1)+int(var2)
diff=int(var1)-int(var2)
prod=int(var1)+int(var2)
print( var1 ,var2, sum,diff,prod)

#Q3
name2=input("enter your name :")
gradeLab=input("enter your lab grade :")
gradeMidterm=input("enter your midterm grade :")
gradeFinal=input("enter your final grade :")
print("lab :" + gradeLab)
print("midterm :"+gradeMidterm)
print("final :"+ gradeFinal)
lastscore=(float(gradeLab)/4)+(float(gradeMidterm)*35/100)+(float(gradeFinal)*4/10)
print("last score: ",lastscore)


#Q4
print('"*"\n "**" \n"***"\n"***"\n "**" \n"*"\n')
