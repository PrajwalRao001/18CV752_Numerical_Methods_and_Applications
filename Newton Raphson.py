'''
    Newton Raphson Method for finding a root of a given function

    Assumptions:
    1) The given function must be continuous and differentiable
    2) The given function must be a polynomial function
    3) One of the roots of function must exist between -1000 and 1000
'''

'''
    Given problem:
        f(x) = (x^3) - 2(x) - 5
        f1(x) = 3(x^2) - 2
'''

def substitute(x, F):
    value = 0
    for i in range(len(F)):
        value += F[i] * (x**(len(F)-(i+1)))
    return value

def newton_raphson(fx, f1x):
    x = 0
    i_num = 1
    for i in range(-1000, 1000):
        if(substitute(i, fx) > 0):
            x = i
            break
    x_next = x-1
    print("Intitial value of x: "+str(x_next))
    while(x_next != x and i_num <= 20):
        x = x_next
        x_next = x - (substitute(x, fx)/substitute(x, f1x))
        x_next = round(x_next, 5)
        print("x after iteration "+str(i_num)+": "+str(x_next))
        i_num += 1
    print("Solution of f(x) is: x = "+str(x))

fx = [1, 0, -2, -5]
f1x = [0, 3, 0, -2]

newton_raphson(fx, f1x)
