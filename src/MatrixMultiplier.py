import sys
import time

def classical(m1,m2):
    n = len(m1)
    result = [[0] * n for x in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

    
    
    
def divide(m1,m2):
    if ((len(m1) % 2 == 0) or (len(m1) == 1)):
        n = len(m1)
    else:
        n = len(m1) + 1
    result = [[0] * n for x in range(n)]
    
    if (n == 1):
        result[0][0] = m1[0][0] * m2[0][0]
    else:
        new = n//2
        a11 = [[0] * new for x in range(new)]
        a12 = [[0] * new for x in range(new)]
        a21 = [[0] * new for x in range(new)]
        a22 = [[0] * new for x in range(new)]
        
        b11 = [[0] * new for x in range(new)]
        b12 = [[0] * new for x in range(new)]
        b21 = [[0] * new for x in range(new)]
        b22 = [[0] * new for x in range(new)]
        
        c11 = [[0] * new for x in range(new)]
        c12 = [[0] * new for x in range(new)]
        c21 = [[0] * new for x in range(new)]
        c22 = [[0] * new for x in range(new)]
        
        
        a11 = [m1[i][0:new] for i in range(new)]
        a12 = [m1[i][new:len(m1)] for i in range(new)]
        a21 = [m1[i][0:new] for i in range(new,len(m1))]
        a22 = [m1[i][new:len(m1)] for i in range(new,len(m1))]
        
        b11 = [m2[i][0:new] for i in range(new)]
        b12 = [m2[i][new:len(m2)] for i in range(new)]
        b21 = [m2[i][0:new] for i in range(new,len(m2))]
        b22 = [m2[i][new:len(m2)] for i in range(new,len(m2))]
        
        c11 = add(divide(a11,b11), divide(a12,b21))
        c12 = add(divide(a11,b12), divide(a12,b22))
        c21 = add(divide(a21,b11), divide(a22,b21))
        c22 = add(divide(a21,b12), divide(a22,b22))
        
        for i in range(0, new):
            for j in range(0, new):
                result[i][j] = c11[i][j]
                result[i][j + new] = c12[i][j]
                result[i + new][j] = c21[i][j]
                result[i + new][j + new] = c22[i][j]
        
    return result    
        


        
def strassen(m1, m2):
    if ((len(m1) % 2 == 0) or (len(m1) == 1)):
        n = len(m1)
    else:
        n = len(m1) + 1
    result = [[0] * n for x in range(n)]
    
    if (n == 1):
        result[0][0] = m1[0][0] * m2[0][0]
    else:
        new = n//2
        a11 = [[0] * new for x in range(new)]
        a12 = [[0] * new for x in range(new)]
        a21 = [[0] * new for x in range(new)]
        a22 = [[0] * new for x in range(new)]
        
        b11 = [[0] * new for x in range(new)]
        b12 = [[0] * new for x in range(new)]
        b21 = [[0] * new for x in range(new)]
        b22 = [[0] * new for x in range(new)]
        
        c11 = [[0] * new for x in range(new)]
        c12 = [[0] * new for x in range(new)]
        c21 = [[0] * new for x in range(new)]
        c22 = [[0] * new for x in range(new)]
        
        p1 = [[0] * new for x in range(new)]
        p2 = [[0] * new for x in range(new)]
        p3 = [[0] * new for x in range(new)]
        p4 = [[0] * new for x in range(new)]
        p5 = [[0] * new for x in range(new)]
        p6 = [[0] * new for x in range(new)]
        p7 = [[0] * new for x in range(new)]
        
        a11 = [m1[i][0:new] for i in range(new)]
        a12 = [m1[i][new:len(m1)] for i in range(new)]
        a21 = [m1[i][0:new] for i in range(new,len(m1))]
        a22 = [m1[i][new:len(m1)] for i in range(new,len(m1))]
        
        b11 = [m2[i][0:new] for i in range(new)]
        b12 = [m2[i][new:len(m2)] for i in range(new)]
        b21 = [m2[i][0:new] for i in range(new,len(m2))]
        b22 = [m2[i][new:len(m2)] for i in range(new,len(m2))]
        
        p1 = strassen(a11,sub(b12,b22))
        p2 = strassen(add(a11,a12),b22)
        p3 = strassen(add(a21,a22),b11)
        p4 = strassen(a22,sub(b21,b11))
        p5 = strassen(add(a11,a22),add(b11,b22))
        p6 = strassen(sub(a12,a22),add(b21,b22))
        p7 = strassen(sub(a11,a21),add(b11,b12))
        
        c11 = sub(add(p6,add(p5,p4)),p2)
        c12 = add(p1,p2)
        c21 = add(p3,p4)
        c22 = sub(add(p5,p1),add(p3,p7))
        
        for i in range(0, new):
            for j in range(0, new):
                result[i][j] = c11[i][j]
                result[i][j + new] = c12[i][j]
                result[i + new][j] = c21[i][j]
                result[i + new][j + new] = c22[i][j]
        
    return result
   
   
   
   
def add(m1,m2):
    result = [[0] * len(m1[0]) for x in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] + m2[i][j]
            
    return result
    
    
    
    
def sub(m1,m2):
    result = [[0] * len(m1[0]) for x in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] - m2[i][j]
            
    return result
 
    
    
    
def generate(n):
    m1 = [[0] * n for x in range(n)]
    m2 = [[0] * n for x in range(n)]
    
    for i in range(n):
        for j in range(n):
            m1[i][j] = (j % 32)
            m2[i][j] = (j % 64)
    
    return m1,m2

    
    
    
def run(method, n):
    m1,m2 = generate(n)
        
    start = time.time()
    method(m1,m2)
    end = time.time()
        
    exe = end - start
    
    return exe

    
    
    
''' main'''

n = 1
fileC = open("data-CLASSIC.txt","w")
fileD = open("data-DIVIDE.txt","w")
fileS = open("data-STRASSEN.txt","w")
for i in range(1,100):
    avgC = 0
    avgD = 0
    avgS = 0
    n *= 2
    sys.stdout.write("n = " + str(n) + "\n")
    sys.stdout.flush()
    
    for j in range(1,4):
        sys.stdout.write("PASS #%d CLASSICAL: " % (j))
        sys.stdout.flush()
        C = run(classical, n)
        avgC += C
        fileC.write(str(n) + " " + str(C) + "\n")
        sys.stdout.write("DONE IN " + str(C) + "s" + " "*20 + "\n")
        sys.stdout.flush()
        
        sys.stdout.write("        DIVIDE:    ")
        sys.stdout.flush()
        D = run(divide, n)
        avgD += D
        fileD.write(str(n) + " " + str(D) + "\n")
        sys.stdout.write("DONE IN " + str(D) + "s" + " "*20 + "\n")
        sys.stdout.flush()
        
        sys.stdout.write("        STRASSEN:  ")
        sys.stdout.flush()
        S = run(strassen, n)
        avgS += S        
        fileS.write(str(n) + " " + str(S) + "\n")
        sys.stdout.write("DONE IN " + str(S) + "s" + " "*20 + "\n")
        sys.stdout.flush()

    avgC = avgC/3
    avgD = avgD/3
    avgS = avgS/3
    fileC.write(str(n) + " " + str(avgC) + "\n")
    fileD.write(str(n) + " " + str(avgD) + "\n")
    fileS.write(str(n) + " " + str(avgS) + "\n")
    
    print("\n   CLASSICAL Average = %f" % (avgC))
    print("\n      DIVIDE Average = %f" % (avgD))
    print("\n    STRASSEN Average = %f" % (avgS))
    
    
    print("---------------------------------------\n")
    
fileC.close()
fileD.close()
fileS.close()
