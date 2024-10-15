def modify(x):
    x += 10
    return x

def modify_list(my_list):
    my_list.append(10)
    
def greet(name="student"):
    print("Hello, " + name)    

number = 3
print(modify(number))
print(number)
my_list = [1, 5]
print(modify_list(my_list))
greet()