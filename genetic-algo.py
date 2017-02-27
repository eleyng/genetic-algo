#---
# Implementation of GA
#---

import math, random, heapq
# heapq for finding some number of max in a list

#---
# Objective Function
#---

def f(x):
    x = int(x, 2)
    f = math.sin(x) + 0.05 * x ** 2 + 1
    return f

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
    # rand_lst_bin_1 = []
##    rand_lst = []
##    for i in range(z):
##        rand_lst_item = [(int(rand_lst_bin[i][j],2)*size_interval + f_range[0]) for j in range(n)] #initial cand design in dec rep
##        rand_lst += (rand_lst_item)
##        rand_lst_bin_1 += (rand_lst_bin[i][j] for j in range(n))
    #print("random initial pop", rand_lst, "\n")
##    print("random inital pop as candidate design", rand_lst_bin_1, "\n")



    # Step 2: Evaluate fitness of init pop
    # Generate list of fitness of init pop
    f_lst = []
    max_sub_lst = []
    max_sub_ind_lst = []
    for i in range(len(rand_lst_bin)):
        lst = [f(x) for x in rand_lst_bin[i]]
        max_sub = max(lst)
        max_sub_ind = [i, lst.index(max(lst))]
        f_lst.append(lst)
        max_sub_lst.append(max_sub)
        max_sub_ind_lst.append(max_sub_ind)
    print("evaluation of initial pop", f_lst, "\n")  


    # Start Counter for Mating Loop
    count = 0
    
    while count < gen_iter:
        
        #Step 3: Create Mating Pool
        elites = heapq.nlargest(3, max_sub_lst)#finds the two elite candidates
        if elites[0] == elites[1]:
            elites[1] = elites[2] #set the 2nd candidate to be different
        elites.pop(2)
        print("elite chromosomes", elites, "\n")
        el_sub = [max_sub_lst.index(elites[0]), max_sub_lst.index(elites[1])]
        elites_ind = [max_sub_ind_lst[el_sub[0]], max_sub_ind_lst[el_sub[1]]] #indices
        print("elite candidates indices", elites_ind, "\n")
        elites_cand = []
        elites_cand.append(rand_lst_bin.pop(elites_ind[0][0]))
        elites_cand.append(rand_lst_bin.pop(elites_ind[1][0]))
        print("elite candidates", elites_cand, "\n")
        print("candidate mating pool", rand_lst_bin, "\n")

        
        r = random.uniform(0, 1)

            
        print(r)


        
        count += 5
        
    
    


main()


