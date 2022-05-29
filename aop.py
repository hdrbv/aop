#################################
## Art of Computer Programming ##
#################################

#Algorithm E (Euclid's algo):

def euclid_algo(m, n) : 
    i = 0
    r = m % n
    while r != 0 : 
        m = n
        n = r
        r = m % n
        i += 1
        print('step {}'.format(i))
    return n
        
euclid_algo(100, 20)



