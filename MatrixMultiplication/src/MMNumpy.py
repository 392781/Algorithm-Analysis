import sys
import time
import numpy as np


def classical(m1,m2):
    """ 
    Classical matrix multiplication method.
    3 loops, n^3 time
        
    Parameters:
        m1 (ndarray):       2d array size n 
        m2 (ndarray):       2d array size n
    
    Returns:
        result (ndarray):   2d array containing the solution
    """
    
    n = m1.shape
    result = np.zeros(n, dtype = int)

    for i in range(n[0]):
        for j in range(n[0]):
            for k in range(n[0]):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

    
    
    
def divide(m1,m2):
    """ 
    Divide and conquer matrix multiplication method
    Subdivides the arrays into smaller portions and recursively calls the solutions
        
    Parameters:
        m1 (ndarray):       2d array size n 
        m2 (ndarray):       2d array size n
    
    Returns:
        result (ndarray):   2d array containing the solution
    """
    
    if ((m1.shape[0] % 2 == 0) or (m1.shape[0] == 1)):
        n = m1.shape[0]
    else:
        n = m1.shape[0] + 1
    result = np.zeros((n, n), dtype = int)
    
    if (n == 1):
        result[0][0] = m1[0][0] * m2[0][0]
    else:
        new = n//2
               
        a11, a12, a21, a22 = m1[:new, :new], m1[new:, :new], m1[:new, new:], m1[new:, new:]
        b11, b12, b21, b22 = m2[:new, :new], m2[new:, :new], m2[:new, new:], m2[new:, new:]
        
        result[:new, :new] = divide(a11,b11) + divide(a12,b21)
        result[new:, :new] = divide(a11,b12) + divide(a12,b22)
        result[:new, new:] = divide(a21,b11) + divide(a22,b21)
        result[new:, new:] = divide(a21,b12) + divide(a22,b22)
        
    return result    
        


        
def strassen(m1, m2):
    """ 
    Strassen method for matrix multiplication
    Applies the Strassen algorithm which saves 1 multiplication compared to a regular 
    divide and conquer
        
    Parameters:
        m1 (ndarray):       2d array size n 
        m2 (ndarray):       2d array size n
    
    Returns:
        result (ndarray):   2d array containing the solution
    """
    
    if ((m1.shape[0] % 2 == 0) or (m1.shape[0] == 1)):
        n = m1.shape[0] 
    else:
        n = m1.shape[0] + 1
    result = np.zeros((n, n), dtype = int)
    
    if (n == 1):
        result[0][0] = m1[0][0] * m2[0][0]
    else:
        new = n//2
        
        a11, a12, a21, a22 = m1[:new, :new], m1[new:, :new], m1[:new, new:], m1[new:, new:]
        b11, b12, b21, b22 = m2[:new, :new], m2[new:, :new], m2[:new, new:], m2[new:, new:]
        
        p1 = strassen(a11, b12 - b22)
        p2 = strassen(a11 + a12, b22)
        p3 = strassen(a21 + a22, b11)
        p4 = strassen(a22, b21 - b11)
        p5 = strassen(a11 + a22, b11 + b22)
        p6 = strassen(a12 - a22, b21 + b22)
        p7 = strassen(a11 - a21, b11 + b12)
        
        result[:new, :new] = p5 + p4 - p2 + p6
        result[new:, :new] = p1 + p2
        result[:new, new:] = p3 + p4 
        result[new:, new:] = p5 + p1 - p3 - p7
        
    return result
 
    
    
    
def generate(n):
    """ 
    Function to generate two n sized arrays.  One with repeating 
    values from 0 to 31 and the other with repeating values from 0 to 63.
        
    Parameters:
        n (int):            array size
    
    Returns:
        m1 (ndarray):       2d array size n 
        m2 (ndarray):       2d array size n
    """
    
    m1 = np.zeros((n, n), dtype = int)
    m2 = np.zeros((n, n), dtype = int)
    
    for i in range(n):
        for j in range(n):
            m1[i][j] = (j % 32)
            m2[i][j] = (j % 64)
    
    return m1,m2

    
    
    
def run(method, n):
    """ 
    Runner function, takes the method name and desired array 
    size as parameters.  Tt generates 2 n-sized arrays then runs 
    and times the desired method.
        
    Parameters:
        method (string):    Desired method name to run (classical, divide, strassen)
        n (int):            array size
    
    Returns:
        exe (float):        Execution time
    """
    
    m1,m2 = generate(n)
        
    start = time.time()
    method(m1,m2)
    end = time.time()
        
    exe = end - start
    
    return exe

    
    
    
''' main'''

n = 1
fileC = open("data-CLASSICnpy.txt","w")
fileD = open("data-DIVIDEnpy.txt","w")
fileS = open("data-STRASSENnpy.txt","w")

# Initial loop to execute test
for i in range(1,100):
    # Averages for classical (C), divide (D), and strassen (S) metthods
    avgC = 0
    avgD = 0
    avgS = 0
    n *= 2
    sys.stdout.write("n = " + str(n) + "\n")
    sys.stdout.flush()
    
    # Loop to test each algorithm through 3 passes
    for j in range(1,4):
        # Classical test, adds to average, prints and writes execution time
        sys.stdout.write("PASS #%d CLASSICAL: " % (j))
        sys.stdout.flush()
        C = run(classical, n)
        avgC += C
        fileC.write(str(n) + " " + str(C) + "\n")
        sys.stdout.write("DONE IN " + str(C) + "s" + " "*20 + "\n")
        sys.stdout.flush()
        
        # Divide test, adds to average, prints and writes execution time
        sys.stdout.write("        DIVIDE:    ")
        sys.stdout.flush()
        D = run(divide, n)
        avgD += D
        fileD.write(str(n) + " " + str(D) + "\n")
        sys.stdout.write("DONE IN " + str(D) + "s" + " "*20 + "\n")
        sys.stdout.flush()
        
        # Strassen test, adds to average, prints and writes execution time
        sys.stdout.write("        STRASSEN:  ")
        sys.stdout.flush()
        S = run(strassen, n)
        avgS += S        
        fileS.write(str(n) + " " + str(S) + "\n")
        sys.stdout.write("DONE IN " + str(S) + "s" + " "*20 + "\n")
        sys.stdout.flush()
        
    # Calculates averages of each method and writes to respective file
    avgC = avgC/3
    avgD = avgD/3
    avgS = avgS/3
    fileC.write(str(n) + " " + str(avgC) + "\n")
    fileD.write(str(n) + " " + str(avgD) + "\n")
    fileS.write(str(n) + " " + str(avgS) + "\n")
    
    # Prints to terminal execution time
    print("\n   CLASSICAL Average = %f" % (avgC))
    print("\n      DIVIDE Average = %f" % (avgD))
    print("\n    STRASSEN Average = %f" % (avgS))
    
    
    print("---------------------------------------\n")
    
fileC.close()
fileD.close()
fileS.close()
