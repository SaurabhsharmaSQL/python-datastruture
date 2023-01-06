# camel case
# all chatacter of the world small exect 1st character of the second and so on words.
#def SORTNAMES():

#def sortnames():

#def sort_name():

#def sortName():

##########################################################

'''def sortStudentName():
    #aaa
    #bbb
    #ccc
    #ddd
    #eee

    print ("Dummy-1")
    print ("Dummy-2")
    print ("Dummy-3")
    print ("Dummy-4")

sortStudentName()'''

##########################################################

'''sortStudentName()

def sortStudentName():
    #aaa
    #bbb
    #ccc
    #ddd
    #eee

    print ("Dummy-1")
    print ("Dummy-2")
    print ("Dummy-3")
    print ("Dummy-4")'''

##########################################################
#Outsidefuntions

'''def sortStudentName():


    print ("Dummy-1")
    print ("Dummy-2")
    print ("Dummy-3")
    print ("Dummy-4")

print ("Outside funtions")

sortStudentName()'''

##########################################################
#insidefuntions


'''def sortStudentName():


    print ("Dummy-1")
    print ("Dummy-2")
    print ("Dummy-3")
    print ("Dummy-4")

    print ("Inside funtions")

sortStudentName()'''

##########################################################
#Vicky Question for input


'''def sortStudentName(firstName = "Saurabh", lastName = "Sharma"):

    print ("Dummy1")

print  ("Outside functions")

sortStudentName()'''


##########################################################
#input Function

'''def sortStudentName(firstName = "Saurabh", lastName = "Sharma"):

    print ("Welcome to python " + firstName + " " + lastName )

#print  ("Outside functions")

sortStudentName()
sortStudentName("Vijay", "Mishra")
sortStudentName("Saurabh", "Sharma")
sortStudentName("Vikcy", "Mishra")
sortStudentName("Preeti", "Mishra")'''


##########################################################
#input Function

'''def greetStudents(firstName = "Saurabh", lastName = "Sharma"):

    print ("Welcome to python " + firstName + " " + lastName )

#print  ("Outside functions")

greetStudents()
greetStudents("Vijay", "Mishra")
greetStudents("Saurabh", "Sharma")
greetStudents("Vikcy", "Mishra")
greetStudents("Preeti", "Mishra")'''

##########################################################################
#Question Answer

'''def sortStudentName (firstName = "abc", lastName = "def"):
    print ("welcome to python " + firstName + " " + lastName)
    print ("------------------------------------------------")
    print ("------------------------------------------------")

sortStudentName()
sortStudentName("abc1 ", "abc2")
sortStudentName("abc3 ", "abc4")
sortStudentName("abc5 ", "abc6")
sortStudentName("abc7 ")'''

#############################################################################
#SMS

'''def sortStudentName(firstName = "Ram", lastName = "Sharma"):
    print ("Welcome to Python " + firstName + " " + lastName )
    print (" Today is your day in colleage")
    print (" Please go to noticeboard for timetable")
    print ("-----------------------------------------------")

sortStudentName()
sortStudentName("Vijay", "Mishra")
sortStudentName("Saurabh", "Sharma")
sortStudentName("Vikcy", "Mishra")
sortStudentName("Preeti", "Mishra")'''


#############################################################################
#Calling line

'''def sortStudentName(firstName = "Ram", lastName = "Sharma"):
    smsSuccessfullySent : bool = False

    print ("Welcome to Python " + firstName + " " + lastName )
    print ("Today is your day in colleage")
    print ("Please go to noticeboard for timetable")
    print ("-----------------------------------------------")

    #smsSuccessfullySent : bool = False

issent = sortStudentName()
issent = sortStudentName("Vijay", "Mishra")
issent = sortStudentName("Saurabh", "Sharma")
issent = sortStudentName("Vikcy", "Mishra")
issent = sortStudentName("Preeti", "Mishra")'''
     
    #smsSuccessfullySent


####(    veryImportantFunctions  )###################################
#####################################################################



def greetStudentsBySMS(firstName = "Ram", lastName = "Sharma"):
    smsSuccessfullySent:bool = False

    print ("Welcome to Python " + firstName + " " + lastName)
    print ("Today is your first day in our college")
    print ("Please go to noticeboard for timetable")
    print ("--------------------------------------")

    smsSuccessfullySent = True

    return(smsSuccessfullySent)

isSent =greetStudentsBySMS()
print(isSent)


isSent = greetStudentsBySMS("Vijay", "Mishra")
print(isSent)

isSent = greetStudentsBySMS("Saurabh", "Sharma")
print(isSent)

isSent = greetStudentsBySMS("Vikcy", "Mishra")
print(isSent)

isSent = greetStudentsBySMS("Preeti", "Mishra")
print(isSent)