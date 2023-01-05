'''Sample  = [1,2,3,4,5,[100,200,300,400,500,["poor","fair","good","very good","Excilent"]]]
#Sample  = [1,2,3,4,5]

print(Sample)

def nest(x):
    for i in x:
        if isinstance(i,list):
            nest(i)
        else:
             print(i)

nest(Sample)'''

print ("my first cdoe")