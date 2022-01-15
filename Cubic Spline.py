'''
    Cubic Splines method
    Assumption: m(0) = m(n-1) = 0
'''

import numpy as np

def find_m(Y, h):
    Mx = [[0 for i in range(len(Y) - 2)] for j in range(len(Y) - 2)]
    My = [0 for i in range(len(Y) - 2)]
    for i in range(len(Mx)):
        My[i] = (6/(h*h)) * (Y[i] - (2 * Y[i+1]) + Y[i+2])
        for j in range(len(Mx)):
            if(i == j):
                Mx[i][j] = 4
                if(i == 0):
                    Mx[i][j+1] = 1
                elif(i == len(Mx) - 1):
                    Mx[i][j-1] = 1
                else:
                    Mx[i][j+1] = 1
                    Mx[i][j-1] = 1
    Mx = np.array(Mx)
    My = np.array(My)
    M_unknowns = np.linalg.solve(Mx, My)
    M = []
    M.append(0)
    for i in M_unknowns:
        M.append(round(i, 5))
    M.append(0)
    print("The values of m: "+str(M)+"\n")
    return M
    # M[i] = (-(M[i-1] + M[i+1]) + ((6/(h*h)) * (Y[i-1] - (2 * Y[i]) + Y[i+1])))/4

def print_cubic_spline(X, Y, M, h, i):

    eq = "f(x) = "
    eq += "(("+str(X[i])+"-x)^3)("+str(M[i-1])+")/(6*"+str(h)+")\n"
    eq += "+ ((x-"+str(X[i-1])+")^3)("+str(M[i])+")/(6*"+str(h)+")\n"
    eq += "+ (("+str(X[i])+"-x)/"+str(h)+")("+str(Y[i-1])+"-("+str(h*h)+"/6)("+str(M[i-1])+"))\n"
    eq += "+ ((x-"+str(X[i-1])+")/"+str(h)+")("+str(Y[i])+"-("+str(h*h)+"/6)("+str(M[i])+"))\n"
    print("Cubic spline equation for "+str(X[i-1])+" <= X <= "+str(X[i]))
    print(eq + "\n")

def find_cubic_spline_value(X, Y, M, h, x):
    fx = 0
    i = 0
    for j in range(len(X)):
        if(x < X[j]):
            i = j
            break
    fx += (((X[i] - x)**3)*M[i-1])/(6*h)
    fx += (((x - X[i-1])**3)*M[i])/(6*h)
    fx += ((X[i] - x)/(h))*((Y[i-1]) - (((h**2)/6) * M[i-1]))
    fx += ((x - X[i-1])/(h))*((Y[i]) - (((h**2)/6) * M[i]))
    return fx

def cubic_spline(X, Y, x):

    h = X[1] - X[0]
    M = find_m(Y, h)
    for i in range(1, len(Y)):
        print_cubic_spline(X, Y, M, h, i)
    fx = find_cubic_spline_value(X, Y, M, h, x)
    print("The value of f("+str(x)+") is: " + str(fx))


#X = [1, 2, 3, 4, 5]
#Y = [1, 0, 1, 0, 1]

X = [0, 1, 2, 3]
Y = [1, 2, 33, 244]

x = 2.5

cubic_spline(X, Y, x)
