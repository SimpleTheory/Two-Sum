from random import randint
from random import randrange

class frac:
    def __init__(self, n, d):
        self.n = n
        if d != 0:
            self.d = d
def float_to_frac(n):
    pass
#another day ^ lol

# -----------------------------------
# Diff generators

def gen():
    return randint(1,1000), randint(1,1000)

def gen_even():
    return randrange(2,2002,2), randrange(2,2002,2)

def genx4():
    return randint(1,1000)*4, randint(1,1000)*4

def gen_choose(choose):
    return randint(1,choose), randint(1, choose)

def gen_choose_half_n(choose):
    return round(randint(1, choose)/2), randint(1, choose)

def genx1000():
    return randint(1,1000)*1000, randint(1,1000)*1000

def genxchoose(choose):
    return randint(1,1000)*choose, randint(1,1000)*choose

def gen_x_square_same_rand():
    x = randint(2,100)
    return randint(1, 1000) * x**2, randint(1, 1000) * x**2

# -----------------------------------
# Diff Solutions

def recursive(n, d):
    i=1
    loop = True

    while loop == True:
        i += 1
        if n % i == 0:
            if d % i == 0:
                loop = False

        if i > min(n, d):
            return f'{n} / {d}'

    nn = n // i
    nd = d // i
    # print(f'{nn} / {nd}')
    # print(i)
    return recursive(nn, nd), f'{n}/{d} Common DM: {i}'

def big_O(n, d):
    list_ = [f'{n} / {d} OG']
    for iteration in range(2 ,min(n, d)+1):
        if n % iteration == 0:
            if d % iteration == 0:
                list_.append(f'{n//iteration} / {d//iteration} Common D: {iteration}')
    return list_

# x,y = gen()
# print(recursive(206, 202))
# print(big_O(x, y))

# ----------------------------------
# Finding number of randomly generated prime fractions
'''
GEN() [RANDINT 1000]/[RANDINT 1000]
    Within range 1000 answer is 608 given diff sample sizes
    Within range 99999 answer is 60815.29 sample size: 100
    
GENERAL:
    All of them trend around .608*pre_sample +/- a bit, given an equal range of random numbers to choose from
    for n and d, with random.randint (ie n = randint(1,1000) | d = randint(1,1000))
    formulas is actually pretty simple 
        probability * sample_size = outcome (same as above but what causes that probability)
        probability ROUGHLY = .608 (but depends on range ratio)
        
MULTIPLYING N TO CHANGE RESULTS:
    out of the random trials I have tried dividing the range from the numerator doesnt do much unless it is divided
    by two in which case the probabilities trends to .508
    and for every subsequent even number the ratio trends to the actual ratio of .608

    if multiplying n by a fraction
        the higher the denominator the closer it trends to the real probability (henceforth real)
        if the denominator is odd it comes from the 3 end and trends down to real
        if the denominator is even it comes from the 2 and trends upto real
            the greater the ratio between the multiplied fraction's n/d the closer to the further from real
            ex: 1/2 is the lowest ratio multiplier while 2/3 is the highest
            
        if the initial range is not big enough the results will be higher and the above trends, trend to being 
        seen, the higher the inital range is to begin best results at 100+
        
If you are counting at least 2 common denominators or more the probability is roughly .838
                
    '''



def pre_solved_calc(choose, pre_sample):
    count = 0
    for i in range(pre_sample):
        x,y = gen_choose_half_n(choose)
        thing = big_O(x,y)
        if len(thing) <= 2:
            count += 1
    return count

def pre_solved_avg(range_, pre_sample, meta_sample):
    # range_ selects range of random int to be inputted in the problem
    # pre_sample is how many times the problem is solved and then counted for times with unique solutions
        # (with randomly selected int from range_)
    # meta_sample is the amount of times the count (from pre_sample) is performed to give a mean of all counts
    list_ = [pre_solved_calc(range_, pre_sample) for i in range(meta_sample)]
    print(list_)
    x = sum(list_) / len(list_)
    return f'{x} \nPercent of samples with 2 cds or less: {(x/pre_sample)*100}%'

#print(pre_solved_avg(10000, 10 ,1000))


c1 = \
'''
from frac import recursive
recursive(206,202)
'''

c2 = \
'''
from frac import big_O
big_O(206,202)
'''


# t1 = timeit(c1, number=10**5)
# t2 = timeit(c2, number=10**5)
