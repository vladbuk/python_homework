# In order to test out your brand new python skills, 
# we would like to suggest a little challenge for you. 
# Especially, function, that should find the roots 
# of quadratic equation need to be implemented. 
# Quadratic equation should be in classic form: ax^2+bx+c=0, 
# so a,b,c will be entered from user input 
# (don't forget to implement messages for user, who will use this script).


def main():
    # main() here our program will be started, 
    # and all required data asked
    a, b, c = ask_value("Enter 3 values of a, b, c backspace devided\n")
    print("a, b, c : ", a, b, c)
    print("Results: ", solv_square(a, b, c))

def ask_value(message):
    # ask_value(message) this function should ask user for input, 
    # and then return variable. 
    # Good to have additional input validation here.
    a, b, c = input(message).split()
    return int(a), int(b), int(c)
    
    #print("Input a"); a = int(input())
    #print("Input b"); b = int(input())
    #print("Input c"); c = int(input())
    #print(a, b, c)
    #print("Discriminant= ", discriminant(a, b, c))

def discriminant(a, b, c):
    # discriminant(a,b,c) no much, no less just return discriminant.
    d = b**2 - 4 * a * c
    return d

def roots():
#def roots(d, a, b, c):
    # roots(d,a,b,c) will show on the screen all acceptable roots
    a, b, c = ask_value("Enter 3 values of a, b, c backspace devided\n")
    d = discriminant(a, b, c)
    print(d)
    if d > 0:
        root1 = (-b + (d ** 0.5) ) / (2 * a)
        print(root1)
        root2 = (-b - (d ** 0.5) ) / (2 * a)
        print(root2)
        print("root1 = {}, root2 = {}".format(root1, root2))
    elif d == 0:
        root1 = root2 = -b / (2 * a)
        print("root1 == root2 = {}").format(root1)
    else:
        real = -b / (2 * a)
        imaginary = -d ** 0.5 / (2 * a)
        print(real, imaginary)
        #print("Roots are imaginary - {} plus-minus {} i").format(real, imaginary)

def solv_square(a, b, c):
    # solv_square(a,b,c) this function should 
    # contain inside discriminant and roots functions.
    return roots(discriminant(a, b, c), a, b, c)

#main()
roots()