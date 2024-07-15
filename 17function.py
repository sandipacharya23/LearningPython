#function: A set of code that perfoem certain task
# imp: we need to call a function 
 #syntax : 
# def function_name();
  #function code

#def Function
def displayName():
    print("it's me sandy")

#calling function
displayName()

##WAP to print even number between 10 to 20
def display_even(first, last):
    for i in range(first, last+1):
        if i%2==0:
            print(i)
      
start=10
end=20
display_even(start, end)


     ##types of function
     #system define
     #user define

#these divided in followings
#1. NO paramenter & No return type
#if ther is nothing inside (),it is called no parameter.
#if ther is no return keyword, it means function doesn't return any value.

def displayName():
    print("it's me sandy")

displayName()

#2. Paarameter and & No rturn type
#n1 and n2 are paramenter  (define garne parameter )
#10,20 is argument ( function call garne bela dine value is argument)

def add(n1, n2):
    total = n1+n2
    print(f"total is{total}")

add(10, 20)




