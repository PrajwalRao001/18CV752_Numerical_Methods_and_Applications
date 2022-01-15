'''
    Gauss Jacobi method to solve system of n equations in n variables
'''

def gauss_jacobi(coeffs, consts):

    print("Given:")
    for n in range(len(coeffs)):
        print(str(coeffs[n]) + " " + str(consts[n]))
    print("\n")

    X = [0.0 for x in coeffs]
    X_prev = [1.0 for x in coeffs]
    i_num = 1


    while(X_prev != X and i_num < 100):
        X_prev = X[:]
        for i in range(len(coeffs)):
            temp = consts[i]
            for j in range(len(coeffs)):
                if(i == j):
                    continue
                else:
                    temp -= coeffs[i][j] * X_prev[j]
            temp = temp / coeffs[i][i]
            X[i] = round(temp, 5)
        print("Values after iteration "+str(i_num)+": "+str(X))
        i_num += 1
        
    solution = "[ "
    for i in range(len(consts)):
        if(i != len(consts)-1):
            solution = solution + "X" + str(i+1) + ", "
        else:
            solution = solution + "X" + str(i+1)
    solution = solution + " ]"
    print("\n"+ solution + " = " + str(X))


coeffs = [
        [-4, 1, 1, 0],
        [1, -4, 0, 1],
        [1, 0, -4, 1],
        [0, 1, 1, -4]
    ]

consts = [-102, -204, -1, -102]
'''
coeffs = [
        [5, 2, 1],
        [1, 4, 2],
        [1, 2, 5]
    ]

consts = [12, 15, 20]
'''
gauss_jacobi(coeffs, consts)
