#---
# Implementation of GA
#---

import math, random, heapq
from operator import itemgetter
# heapq for finding some number of max in a list

#---
# Objective Function
#---

def f(x, size, start):
    #input x is BINARY --> must convert to dec
    f = -1*(math.sin(x) + 0.05 * x ** 2 + 1)
    #print('x', x, 'f', f)
    return f

def conv2var(x, size, start):
    x = int(x,2)
    num = start + (size)*x
    return num

#---
# Code GA Script
#---

def main():

    print("ELEY NG, HW2: GA Implementation", "\n")
    
    
    # Num of Generations
    gen_iter = 5
    
    # Code Variables
    f_range = [-7, 7]
    # m = number of bits in the binary representation
    m = 6
    size_interval = (f_range[1] - f_range[0])/(math.pow(2,m) - 1)
    print('size interval', size_interval, "\n")


    # Setting GA Parameters
    # z, size of population. Usually 30
    z = 10
    # Pc, probability of crossover
    Pc = 0.6
    # Pm, probability of mutation
    Pm = 0.05
    # E, elitism strategy (number of designs to carry over to NexGen). Usually >= 2
    E = 2

    # To create bin rep: first generate all binary rep (2**m-1 numbers)
    pop_lst_bin = []
    pop_lst = []
    pop_d = {}
    for i in range(int(math.pow(2,m))):
        bin_rep = bin(i)[2:].zfill(m)
        var = conv2var(bin_rep, size_interval, f_range[0])
        fn = f(var, size_interval, f_range[0])
        pop_lst.append(var)
        pop_lst_bin.append(bin_rep)
        pop_d[fn] = bin_rep
    print("pop_lst_bin", pop_lst_bin, "\n")
    print("pop_lst ", pop_lst, "\n")
    print("pop_d", pop_d, "\n")
    print("length of pop_lst_bin", len(pop_lst_bin), "\n")

##############################################################################################################################
    
    # Step 1: Create Initial Population
    # Create random initial popul by random indexing of the pop_lst
    n = 1
    # Generate candidate designs
    rand_lst_bin = [pop_lst_bin[random.randint(0,math.pow(2,m)-1)] for j in range(z)] #initial candidate design in binary rep
    print("Gen 1: binary random initial pop rand_lst_bin", rand_lst_bin, "\n") # GEN 1, list of candidate designs
    rand_lst = [conv2var(rand_lst_bin[int(i)], size_interval, f_range[0]) for i in range(len(rand_lst_bin))]
    print("Gen 1: random initial pop", rand_lst, "\n")

##############################################################################################################################
    
    # Step 2: Evaluate fitness of init pop
    # Generate list of fitness of init pop

    lst = []
    for i in range(len(rand_lst)):
        fn = f(rand_lst[i], size_interval, f_range[0])
        lst.append(fn)
    print("fitness val", lst, "\n")
    ord_lst = sorted(lst)
    print("Gen 1: min to max sorted list of fn", ord_lst, "\n")
    fmin = ord_lst[0]
    fmax = ord_lst[len(ord_lst)-1]        

    # Determine elites and sort list
    ord_v = heapq.nlargest(len(lst), lst)
    print("Gen 1: Y Values", ord_v, "\n")
    ord_cand = [pop_d[ord_v[i]] for i in range(z)]
    print("Gen 1: X Values (binary)", ord_cand, "\n")
    ord_cand_val = [conv2var(ord_cand[i], size_interval, f_range[0]) for i in range(z)]
    print("Gen 1: X Values (dec)", ord_cand_val, "\n")
    e1 = ord_cand[0]
    e2 = ord_cand[1]
    el_cand = [e1, e2]
    print("elites cand", el_cand, "\n")
    #print("Gen 1: Ordered cand", ord_cand, "\n")

    #roulette
    den = sum([(ord_lst[i]-fmin) for i in range(z)])
    num_J_1 = []
    num_J = []
    print("MATING POOL generation", "\n")
    for i in range(z):
        print("Candidate Design", i+1)
        wk = ord_lst[i] - fmin
        num_J.append(wk)
        if i != (z-1):
            num_J_1.append(wk)
        r = random.uniform(0,1)
        print("r", r)
        lownum = sum(num_J_1)
        hinum = sum(num_J)
        low = lownum/den
        hi = hinum/den
        if low <= r and r >= hi:
            print("low ({}) is lower than r = {} and high ({}) is higher than r --> ACCEPT".format(low,r,hi), "\n")
            continue
        else:
            #insert elite if reject the candidate
            print("REJECT candidate and replace with elite", "\n")
            del ord_lst[i]
            ord_lst.insert(0, ord_v[0])
            
    print("ORD_LST", ord_lst)
        
    # Redetermine elites and sort list
    ord_v = heapq.nlargest(len(ord_lst), ord_lst)
    ord_ind = [i for i, j in enumerate(ord_v) if j in ord_v]
    ord_cand = [rand_lst_bin[ord_ind[i]] for i in range(len(ord_ind))]
    e1 = ord_cand[0]
    e2 = ord_cand[1]
    el_cand = [e1, e2]
    print("elites cand", el_cand, "\n")
    print("Gen 1: Ranked Candidates", ord_cand, "\n")
       
##############################################################################################################################
    
    # START Loop

    it = 50
    count = 2
    while count <= it:
        # STEP 3: Generate mating pool
        e1 = ord_cand.pop(0)
        e2 = ord_cand.pop(0)
        mp = ord_cand
        print("Crossover & mutation", mp)

        new_cand = [e1,e2] #make next gen list that includes elites
        #print("elites designs removed", new_cand)
        for i in range(0, len(mp), 2):
            r = random.uniform(0, 1)
            if r <= Pc:
                print("crossover!!!")
                str_len = m
                r = random.randint(0,m)
                m1 = str(mp[i])
                m1a = m1[:r]
                m1b = m1[r:]
                m2 = str(mp[i+1])
                m2a = m2[:r]
                m2b = m2[r:]
                p1 = m1a + m2b
                p2 = m1b + m2a
                print("New Child #1", p1, "New Child #2", p2, "\n")
                new_cand.append(p1)
                new_cand.append(p2)
            else:
                print("No crossover: Parents = Children")
                new_cand.append(mp[i])
                new_cand.append(mp[i+1])
            #print("mp[i]", mp[i])
            for e in range(len(str(mp[i]))):
                r = random.random()
                if r <= Pm:
                    print("mutate!!!")
                    mps = list(str(mp[i]))
                    if mps[e] == "1":
                        mps[e] = "0"
                    else:
                        mps[e] = "1"
                    "".join(mps)
        print("Gen {} Candidates".format(count), new_cand, "\n")

        # eval each in the list
        lst = []
        for each in new_cand:
            each = conv2var(each, size_interval, f_range[0])
            fn = f(each, size_interval, f_range[0])
            lst.append(fn)
        print("Gen {} Evaluated for fitness".format(count), lst, "\n")

        #resort the list, re identify the elites, set up for next iter
        ord_lst = sorted(lst) #sorted from max to min
        print("resorted list", ord_lst, "\n")
        e1 = ord_lst[len(lst)-1]
        print("max", e1)

        #roulette
        den = sum([(ord_lst[i]-fmin) for i in range(z)])
        num_J_1 = []
        num_J = []
        print("MATING POOL generation", "\n")
        for i in range(z):
            print("Candidate Design", i+1)
            wk = ord_lst[i] - fmin
            num_J.append(wk)
            if i != (z-1):
                num_J_1.append(wk)
            r = random.uniform(0,1)
            print("r", r)
            lownum = sum(num_J_1)
            hinum = sum(num_J)
            low = lownum/den
            hi = hinum/den
            if low <= r and r >= hi:
                print("low ({}) is lower than r = {} and high ({}) is higher than r --> ACCEPT".format(low,r,hi), "\n")
                continue
            else:
                #insert elite if reject the candidate
                print("REJECT candidate and replace with elite", "\n")
                del ord_lst[i]
                ord_lst.insert(0, e1)
                
        print("Gen {} Y Values (dec)".format(count), ord_lst)

        ord_cand = [pop_d[ord_lst[i]] for i in range(z)]
        print("Gen {}: X Value Candidates (bin)".format(count), ord_cand, "\n")
        
        ord_cand_val = [conv2var(ord_cand[i], size_interval, f_range[0]) for i in range(z)]
        print("Gen {}: X Value (dec)".format(count), ord_cand_val, "\n")

        ord_v = heapq.nlargest(len(ord_lst), ord_lst)
        ord_cand = [pop_d[ord_v[i]] for i in range(z)]
        e1 = ord_cand[0]
        e2 = ord_cand[1]
        el_cand = [e1, e2]
        print("elites cand", el_cand, "\n")
        print("Gen {}: RANKED X Values (bin)".format(count), ord_cand, "\n")
        ord_cand_val = [conv2var(ord_cand[i], size_interval, f_range[0]) for i in range(z)]
        print("Gen {}: RANKED X Values (dec)".format(count), ord_cand_val, "\n")




        #iterate
        count += 1

    print("FINAL: RANKED X Values (bin)".format(count), ord_cand, "\n")
    print("FINAL: RANKED X Values (dec)".format(count), ord_cand_val, "\n")

main()
