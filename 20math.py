#create function that find square of a number 
import math
def square(n1):
    num= n1*n1
    print(f"square is {num}. ")

square(4)

#square root finder 
sq_root =math.sqrt(25)
value =int(sq_root)
print(value)

## point paxadi ko 2 ota number matra lina 
number = 2.11234
print(f"{number:.3f}")

## 
n1=math.ceil(10.1)  #it print 11
n2=math.floor(10.6)  #it peint 10
n3=math.pow(2,3)     # it print 2^3=8

print(round(10.2))
print(round(10.7))

## Create function that round number 3.11
def round_num(n):
    
    print(round(round_num(n)))

round_num(3.11)
    


