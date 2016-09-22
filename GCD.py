def GCD(A,B):
    if (A == 0):
        print("The Greatest Common Denominator is " + str(B))
    elif (B == 0):
        print("The Greatest Common Denominator is " + str(A))
    else:
        rem = A % B
        GCD(B,rem)


GCD(270,192)
