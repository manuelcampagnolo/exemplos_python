pi = 3.1415926535

# converts angle in decimal degrees to radians
def deg2rad(x):
    return pi*x/180
# converts radians to decimal degrees
def rad2deg(x):
    return 180*x/pi
""" 
def mysqrt(y):
    N=100
    if y==0:
        return 0.0
    if y<0:
        return 'NaN'
    
    def f(x):
        return x*x-y
    
    a=0
    b=y+1

    '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    m_N : number
        The x intercept of the secant line on the the Nth interval
            m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
        for some intercept m_n then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iterations, the secant method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f,1,2,5)
    1.6180257510729614
    '''
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return 'NaN'
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

#print(sqrt_secant(0.0001,100)) """

# Square root function using bissection method
# Input: number
def  mysqrt(x):
    tol=10**-10
    if x<0:
        return 0
    else:
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
    Q=x//90
    x=deg2rad(x)
    n=12
    cos = 1
    fact = 2
    for i in range(1, n + 1):
        cos += ((-1) ** i) * (x**(2*i) / fact)
        fact *= (2*i+1)*(2*i+2)
    return cos

def mysin(x):
    x=x%360
    x=deg2rad(x)
    n=12
    sin = x
    fact= 3*2
    for i in range(1, n + 1):
        sin += ((-1) ** i) * (x**(2*i+1) / fact)
        fact *= (2*i+2)*(2*i+3)
    return sin

#print(mysin(30),mysin(45),mysin(-45), mysin(-135))

""" 
def myarcsin(y):
    N=100
    if y <= -1:
        return -90
    if y >= 1:
        return 90
    
    def f(x):
        return mysin(x)-y
    
    a=-90
    b=90

    '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    m_N : number
        The x intercept of the secant line on the the Nth interval
            m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
        for some intercept m_n then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iterations, the secant method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f,1,2,5)
    1.6180257510729614
    '''
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return 'NaN'
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
 """
#print(arcsin_secant(0.5,100), arcsin_secant(-0.5,100))

# Arcsin using bissection method
# input: number
# output: angle in decimal degrees
def myarcsin(x):
    tol=10**-10
    if x <= -1:
        return -90
    if x >= 1:
        return 90
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
