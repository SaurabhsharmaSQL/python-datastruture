'''def sum_recursive(n):
    if n == 1:
        print("Finally 1 found")
        return 1
    else:
        print ("Recusion for n")'''

def addValue(n:int):
    if n<100:
        print(n)
        addValue(n+1)
    else:
        return(n)
finalValue = addValue(1)
print("Final value{0}", finalValue)