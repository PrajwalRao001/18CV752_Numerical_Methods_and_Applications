'''
    Given a square matrix, this function will output a step by step implementation
    of Gauss Jordan method to solve n equations with n variables.
'''
def gauss_jordan(coeffs, consts):

    print("Given:")
    for n in range(len(coeffs)):
        print(str(coeffs[n]) + " " + str(consts[n]))
    print("\n")

    # for every column in the coefficient matrix
    for i in range(len(coeffs)):

        # for every row in the coefficient matrix       
        for j in range(len(coeffs)):

            # ignore the diagonal elements
            if(j == i):
                continue

            # applying row transformation
            else:
                if(coeffs[i][i] > 0 and coeffs[j][i] > 0):
                    print("Applying R"+str(j+1)+" -> "+str(coeffs[i][i])+"R"+str(j+1)+" - "+str(coeffs[j][i])+"R"+str(i+1))
                elif(coeffs[i][i] < 0 and coeffs[j][i] > 0):
                    print("Applying R"+str(j+1)+" -> "+str(coeffs[i][i])+"R"+str(j+1)+" + "+str(coeffs[j][i])+"R"+str(i+1))
                elif(coeffs[i][i] < 0 and coeffs[j][i] < 0):
                    print("Applying R"+str(j+1)+" -> "+str(coeffs[i][i])+"R"+str(j+1)+" + "+str(-coeffs[j][i])+"R"+str(i+1))
                elif(coeffs[i][i] > 0 and coeffs[j][i] < 0):
                    print("Applying R"+str(j+1)+" -> "+str(coeffs[i][i])+"R"+str(j+1)+" - "+str(-coeffs[j][i])+"R"+str(i+1))
                else:
                    continue
                consts[j] = (consts[j] * coeffs[i][i]) - (consts[i] * coeffs[j][i])
                coeffs[j] = [(coeffs[i][i] * k) - (coeffs[j][i] * l) for k, l in zip(coeffs[j], coeffs[i])]
                
                for m in range(len(coeffs)):
                    print(str(coeffs[m]) + " " + str(consts[m]))
                print("\n")

    #Applying the final transformations to get the solutions
    for i in range(len(coeffs)):
        print("Final equation in variable X"+str(i+1)+": "+str(coeffs[i][i])+"X"+str(i+1)+" = "+str(consts[i]))
        print("Applying R"+str(i+1)+" -> R"+str(i+1)+"/"+str(coeffs[i][i]))
        k = coeffs[i][i]
        coeffs[i] = [(coeffs[i][j] / k) for j in range(len(coeffs[i]))]
        consts[i] = consts[i]/k
        print("=> X"+str(i+1)+" = "+str(consts[i]))
        print("\n")

    #printing solutions
    solution = "[ "
    for i in range(len(consts)):
        if(i != len(consts)-1):
            solution = solution + "X" + str(i+1) + ", "
        else:
            solution = solution + "X" + str(i+1)
    solution = solution + " ]"
    print(solution + " = " + str(consts))

coeffs = [
        [-4, 1, 1, 0],
        [1, -4, 0, 1],
        [1, 0, -4, 1],
        [0, 1, 1, -4]
    ]

consts = [-102, -204, -1, -102]

gauss_jordan(coeffs, consts)
