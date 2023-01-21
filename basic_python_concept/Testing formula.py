#***a=2
#b=2
#a+b

#print(a+b)
#print(a+b*a)***

Sample  = [1,2,3,4,5,[100,200,300,400,500,["poor","fair","good","very good","Excilent"]]]

print(Sample)
#for i in Sample:
    #print(i) 

def loop(x):
    for item in x:
        if isinstance(item,list):
            loop(item)
        else:
            print(item)
loop(Sample)
            

#test = ["a","b","c",["Sam","Ram","Bam",["qw","er"]]]
#print(list(test))                

#metrix = [[1,2,3],
          [1,2,3],
          [1,2,3]]

#print(metrix)
#for i in metrix:
    #print(i)