#---
# Implementation of GA
#---

import math, random, heapq
# heapq for finding some number of max in a list

#---
# Objective Function
#---

def f(x, size, start):
    #input x is BINARY --> must convert to dec
    x = int(x,2)
    x = start + size*x
    f = math.sin(x) + 0.05 * x ** 2 + 1
    #print('x', x, 'f', f)
    return f

def conv2var(x, size, start):
    x = int(x,2)
    num = start + (size)*x


    
def dec2bin(x, size, start):
    print("orig",x)
    x = math.ceil((x - start)/size)
    print(x)
    x = bin(x)
    x = int(x[2:])
    return x

#---
# Code GA Script
#---

def main():
    
    # Num of Generations
    gen_iter = 5
    
    # Code Variables
    # var_prop = input('Continuous or Discrete? ')
    var_prop = 'C'
    while var_prop != 'D' and var_prop != 'C':
        var_prop = input('Continuous or Discrete? ')
    # Discrete: find number of bits, m, needed
    if var_prop == 'D':
        num_discrete = int(input('Number of discrete values desired? '))
        m = math.log2(num_discrete)
        m = math.ceil(m)
        print('m =', m, "\n")
    # Continuous: divide interval into binary representation with m bit size
    else:
        #print('Input interval range: ')
        #f_range = [int(x) for x in input().split()]
        f_range = [-7, 7]
        #m = int(input('Choose number of bits in the binary representation: '))
        m = 6
        size_interval = (f_range[1] - f_range[0])/(math.pow(2,m) - 1)
        print('size interval', size_interval, "\n")


    # Setting GA Parameters
    # z, size of population. Usually 30
    #z = int(input('Size of population, z: '))
    z = 10
    # Pc, probability of crossover
    #Pc = float(input('Pc, probability of crossover: '))
    Pc = 0.6
    # Pm, probability of mutation
    # Pm = float(input('Pm, probability of mutation: '))
    Pm = 0.05
    # E, elitism strategy (number of designs to carry over to NexGen). Usually >= 2
    #E = int(input('E, number of designs to carry over to NexGen (Elitism): '))
    E = 2

    # Step 1: Create Initial Population
    # To create bin rep: first generate all binary rep (2**m-1 numbers)
    pop_lst_bin = []
    for i in range(int(math.pow(2,m))):
        bin_rep = bin(i)[2:].zfill(m)
        #print(bin_rep)
        pop_lst_bin.append(bin_rep)
    print("pop_lst_bin", pop_lst_bin, "\n")
    print("length of pop_lst_bin", len(pop_lst_bin), "\n")
    # Create random initial popul by random indexing of the pop_lst
    #n = int(input('Number of suitable solutions: '))
    n = 3
    # Generate candidate designs
    rand_lst_bin = [[pop_lst_bin[random.randint(0,math.pow(2,m)-1)] for i in range(n)] for j in range(z)] #initial candidate design in binary rep
    print("binary random initial pop", rand_lst_bin, "\n") # GEN 1, list of candidate designs

    # Step 2: Evaluate fitness of init pop
    # Generate list of fitness of init pop
    f_lst = []
    max_sub_lst = [] #list of max from each design
    max_sub_ind_lst = [] # list of indices of max from each design
    min_sub_lst = [] #list of min from each design
    min_sub_ind_lst = [] # list of indices of min from each design
    for i in range(len(rand_lst_bin)):
        lst = [f(x, size_interval, f_range[0]) for x in rand_lst_bin[i]]
        max_sub = max(lst)
        max_sub_ind = [i, lst.index(max(lst))]
        #min
        min_sub = min(lst)
        min_sub_ind = [i, lst.index(min(lst))]
        f_lst.append(lst)
        max_sub_lst.append(max_sub)
        max_sub_ind_lst.append(max_sub_ind)
        min_sub_lst.append(min_sub)
        min_sub_ind_lst.append(min_sub_ind)
    print("evaluation of initial pop", f_lst, "\n")  


    # Start Counter for Mating Loop
    count = 0
    
    while count < gen_iter:
        
        #Step 3: Create Mating Pool
        ord_lst = heapq.nlargest(len(rand_lst_bin), max_sub_lst) # finds max for each candidate
        print("MAX to MIN ord_lst", ord_lst, "\n")
        main_lst = []
        for i in ord_lst:
            el = dec2bin(i, size_interval, f_range[0])
            main_lst.append(el)
        print("MAX to MIN GENERATION", main_lst)
            
        elites = ord_lst[0:2] # find elites
        print("MAX elite fitness values", elites, "\n")
        
        while elites[0] == elites[1]: # there is a problem, must regenerate candidate pool
            print('************RETRY***************', "\n")
            rand_lst_bin = [[pop_lst_bin[random.randint(0,math.pow(2,m)-1)] for i in range(n)] for j in range(z)] #initial candidate design in binary rep
            print("binary random initial pop", rand_lst_bin, "\n") # GEN 1, list of candidate designs
            # Step 2: Evaluate fitness of init pop
            # Generate list of fitness of init pop
            f_lst = []
            max_sub_lst = [] #list of max from each design
            max_sub_ind_lst = [] # list of indices of max from each design
            min_sub_lst = [] #list of min from each design
            min_sub_ind_lst = [] # list of indices of min from each design
            for i in range(len(rand_lst_bin)):
                lst = [f(x, size_interval, f_range[0]) for x in rand_lst_bin[i]]
                max_sub = max(lst)
                max_sub_ind = [i, lst.index(max(lst))]
                #min
                min_sub = min(lst)
                min_sub_ind = [i, lst.index(min(lst))]
                f_lst.append(lst)
                max_sub_lst.append(max_sub)
                max_sub_ind_lst.append(max_sub_ind)
                min_sub_lst.append(min_sub)
                min_sub_ind_lst.append(min_sub_ind)
            print("evaluation of initial pop", f_lst, "\n")
            ord_lst = heapq.nlargest(len(rand_lst_bin), max_sub_lst) # finds max for each candidate
            print("ord_lst", ord_lst)
            elites = ord_lst[0:2] # find elites
            print("elite fitness values", elites, "\n")

        # Create ordered list of designs for ranking
        ord_sub = [max_sub_lst.index(ord_lst[i]) for i in range(len(max_sub_lst))] # finds ROW ind of max vals in ord_lst
        ord_ind = [max_sub_ind_lst[ord_sub[i]] for i in range(len(max_sub_ind_lst))] # stores the ROW AND COL indices of max vals in ord_ind
        print("MAX_MAX to MIN_MAX ordered candidates indices", ord_ind, "\n")
        ord_cand = []
        for i in range(len(ord_sub)):
            el = rand_lst_bin[ord_ind[i][0]]
            ord_cand.append(el)

        print("MAX to MIN ordered candidates", ord_cand, "\n")

        # Select and Remove Elites
        elites_cand = ord_cand[0:2]
        print("MAX Elites CANDIDATES", elites_cand, "\n")

        # Determine min and max
        # MIN
        ord_lst_min = heapq.nsmallest(len(rand_lst_bin), min_sub_lst)
        ord_sub_min = [min_sub_lst.index(ord_lst_min[i]) for i in range(len(min_sub_lst))] # finds ROW ind of max vals in ord_lst
        ord_ind_min = [min_sub_ind_lst[ord_sub[i]] for i in range(len(min_sub_ind_lst))] # stores the ROW AND COL indices of max vals in ord_ind
        print("MIN_MIN to MAX_MIN ordered candidates indices", ord_ind_min, "\n")
        ord_cand_min = []
        for i in range(len(ord_sub_min)):
            el = rand_lst_bin[ord_ind_min[i][0]]
            ord_cand_min.append(rand_lst_bin[ord_ind[i][0]])
        print("MIN to MAX ordered candidates (min)", ord_cand_min, "\n")
        fmin = ord_lst_min[0]
        print("fmin", fmin, "\n")
        # MAX
        fmax = elites[0]
        print("fmax", fmax, "\n")

        # Candidate selection (remove elites)
        r = random.uniform(0, 1)
##        for i in range(2, z, 2):
##            for j in range(n):
##                a = sum(
                
                

            
        print(r)


        
        count += 5
        
    
    


main()


