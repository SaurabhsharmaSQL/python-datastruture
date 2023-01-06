import random   

def greetStudentsBySMS(firstName = "Ninja", lastName = "Hathodi"):
    smsSuccessfullySent :bool =False

    print("Welcome to python -" + firstName + " " + lastName)
    print("Today is your first day in our Superlearners Class")
    print("Please prepare your random function program")

    smsSuccessfullySent = bool(random.getrandbits(1))

    print('###########################################')

    return(smsSuccessfullySent)

isSent = greetStudentsBySMS()
print(isSent)


isSent = greetStudentsBySMS("Boss.Vijay", "Mishra")
print(isSent)

isSent = greetStudentsBySMS("Coder.Preeti", "Sharma")
print(isSent)

isSent = greetStudentsBySMS("Decoder.Gaurav", "Sharma")
print(isSent)


isSent = greetStudentsBySMS("Learner.Saurabh",)
print(isSent)

