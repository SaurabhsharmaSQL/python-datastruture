import sys
#Imp-command line Prameter#

def main():

    #Ge the list of command line arguments
    args = sys.argv[1:]

    #Print each argument
    for arg in args:
        print(arg)

if _name_ == "_main_" :
    main()