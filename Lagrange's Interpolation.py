def lagrange_polynomial(X, Y):
    pol = ""
    for i in range(len(X)):
        numerator = ""
        denominator = ""
        for j in range(len(Y)):
            if(i == j):
                continue
            else:
                numerator += "(x-" + str(X[j]) + ")"
                denominator += "(" + str(X[i]) + "-" + str(X[j]) + ")"
        pol += "(" + numerator + "("+str(Y[i])+")" + ")/(" + denominator + ")\n"
        if(i != len(X) - 1):
            pol += "+"
    print(pol)

def lagrange(X, Y, x):

    Fx = 0
    
    for i in range(len(X)):
        numerator = 1
        denominator = 1
        for j in range(len(Y)):
            if(i == j):
                continue
            else:
                numerator *= (x - X[j])
                denominator *= (X[i] - X[j])

        Fx += (numerator/denominator)*Y[i]
    print("Lagrange's Polynomial: ")
    lagrange_polynomial(X, Y)
    print("f("+str(x)+") = "+str(Fx))


X = [0, 20, 40, 60, 80, 100]
Y = [26, 48.6, 61.6, 71.2, 74.8, 75.2]
x = 35

lagrange(X, Y, x)
