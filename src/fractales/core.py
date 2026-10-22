def escape_iterations ( c , max_iter):
    z=0
    cmp=0
    while abs(z)<=2 and cmp < max_iter : 
         z= z*z + c
         cmp = cmp +1
    return cmp