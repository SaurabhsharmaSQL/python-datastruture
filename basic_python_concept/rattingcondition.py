int1 = int(input("Please enter 1st Interger: "))

if int1 <90:
    print(int1,"Rating--> (1) -->Need Improvement")
   
   #2nd condtn
elif int1 >=90 and int1 <=100:
	print(int1,"Rating ->>(2),,Meet Expedctation")

#3rd condt
elif int1 >100 and int1 <=105:
	print(int1,"Rating ->>(3),,Exceed Expedctation")

#4th condtn
elif int1 > 105:
   print(int1,"Rating-->(4) Outstanding")

elif int1 == null: 
    print("nul not allowed")

'''while (True):
    try:
        user_input= input("Enter the grade: ")
        if user_input == "quit" or user_input == "": break
        grade_value = float(user_input)
        if grade_value<0: break                  
        if grade_value >=0 and grade_value<=89:'''