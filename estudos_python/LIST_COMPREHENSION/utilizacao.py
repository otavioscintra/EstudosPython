#https://www.youtube.com/watch?v=1YbTDczvqco

def divisionfn(x,y):
    return x / y

def multiplicationfn(x,y):
    return x * y

def exponentiation(x,y):
    return x ** y


numbers = [1,2,3,4,5]
division = [divisionfn(number , 2) for number in numbers]
multiplication = [multiplicationfn(numero , 2) for numero in numbers]
squared = [exponentiation(numero , 2) for numero in numbers] # squared = elevado ao quadrado (1 ** 2)

print(numbers)
print(division)
print(multiplication)
print(squared)