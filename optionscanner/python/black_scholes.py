import math

def F(C_or_P_value, C_or_P_indicator, T_t, St, K, r,
      a=1e-9, b=10, tolerance=1e-9, nmax=1000):

    def f_factory(C_or_P_value, T_t, St, K, r):
        """ This closure is to produce the function f of one variable sigma.

        """
        def f(sigma):
            
            def N(x):
                return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
            
            d1 = (math.log(St / K) + (r + math.pow(sigma, 2) / 2.0) * T_t) \
                 / (sigma * math.sqrt(T_t))
            
            d2 = d1 - sigma * math.sqrt(T_t)
            
            return N(d1) * St - N(d2) * K * math.exp(-r * T_t) - C_or_P_value
        
        return f

    def sign(x):
        return (x > 0) - (x < 0)

    T_t = T_t / 365
    
    if C_or_P_indicator == 'P':
        C_or_P_value = C_or_P_value - K * math.exp(-r * T_t) + St
    
   
    f = f_factory(C_or_P_value, T_t, St, K, r)

    # Bisectional root-finding method
    
    if (a >= b) or (sign(f(a)) == sign(f(b))):
        return None # There is no solution in the range from a to b
        
    n = 0
    while n < nmax:
        
        c = (a + b) / 2
        
        if (f(c) == 0) or ((b - a) / 2 < tolerance):
            return c
        
        n += 1
        
        if sign(f(c)) == sign(f(a)):
            a = c
        else:
            b = c

    return None # Method failed

if __name__ == '__main__':
    # for test purposes 
    print(F(14, 'P', 35, 236.9, 250, 0.02))
    print(F(1.19, 'C', 35, 236.9, 240, 0.02))
