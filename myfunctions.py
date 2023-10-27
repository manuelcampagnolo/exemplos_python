pi = 3.1415926535

# converts angle in decimal degrees to radians
def deg2rad(x):
    return pi*x/180
# converts radians to decimal degrees
def rad2deg(x):
    return 180*x/pi

# Square root function using bissection method
# Input: number
def  mysqrt(x):
    if x<0:
        return 'NaN'
    else:
        tol=10**(-10)
        min=0
        max=x+1
        mid=(min+max)/2
        while abs(mid*mid-x)>tol:
            if mid*mid>x:
                max=mid
            else:
                min=mid
            mid=(min+max)/2
        return mid

# McLaurin approximation for cosine
# Input: angle in degrees
def mycos(x):
    x=x%360
    x=deg2rad(x)
    n=9
    cos = 1
    fact = 2
    for i in range(1, n + 1):
        cos += ((-1) ** i) * (x**(2*i) / fact)
        fact *= (2*i+1)*(2*i+2)
    return cos

def mysin(x):
    x=x%360
    x=deg2rad(x)
    n=9
    sin = x
    fact= 3*2
    for i in range(1, n + 1):
        sin += ((-1) ** i) * (x**(2*i+1) / fact)
        fact *= (2*i+2)*(2*i+3)
    return sin

#print(mysin(30),mysin(45),mysin(-45), mysin(-135))

# Arcsin using bissection method
# input: number
# output: angle in decimal degrees
def myarcsin(x):
    if not -1 <= x <= 1:
        return 'NaN'
    tol=10**(-13)
    min= -90
    max= 90
    mid=(min+max)/2
    while abs(mysin(mid)-x)>tol:
        if mysin(mid)>x:
            max=mid
        else:
            min=mid
        mid=(min+max)/2
    return mid

# input: string (prompt to user), float (minimum value for input), float (maximum value for input)
# output: float (user's provided value between minimum and maximum)
def get_decimal(prompt: str,Min: float, Max: float) -> float:
    while True:
        try:
            x=float(input(prompt+' '))
        except ValueError:
            pass
        else:
            if Min <= x <= Max:
                return x
