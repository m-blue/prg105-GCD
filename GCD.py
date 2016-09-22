def gcd(A,B):
    if (A == 0):
        print("The Greatest Common Denominator is " + str(B))
    elif (B == 0):
        print("The Greatest Common Denominator is " + str(A))
    else:
        rem = A % B
        gcd(B, rem)


gcd(270,192)
