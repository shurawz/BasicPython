print("""Love
is 
life""")

age = 25
#print("Mr. bajaj is" + age + "years old") is false b'coz a number cannot be concanetated or whatever it is
#So,
# First Method of printing number is
print("Mr. Bajaj is " +str(age)+ " years old.")

#Second method of printing number is
print('Mr. Bajaj is {0} years old'.format(age))

print("There are {0} days in {1} , {2} , {3} , {4} , {5} , {6} , {7} \n".format("31" , "January" , "March" , "May" , "July" , "August" , "October" , "December" ))
#Result: There are 31 days in January , March , May , July , August , October , December

print("""Janaury: {2}
Febraury: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format("28","30","31"))

print("Mr. Bajaj is %d years old" %age)
print('Actually, Mr. Bajaj is %d %s %d %s' % (age, "years" , 7 , "months"))

for i in range(1,12): #1 means starting from 1 and 5 means less than value 5
    print('The value of %2d in square is %3d and cube is %4d '%(i,i ** 2, i ** 3))

print("PI is %12.50f" %(22/7))
