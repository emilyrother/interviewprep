#main function
# n is the number of vertices
# weights is a list of their weights, v_1, ..., v_n
def mwis (n, weights):
    #
    #FILL IN CODE HERE
    
    #base cases
    opt = [-100000000] * n
    sol_items = []
    sol_tot_weight = 0
    
    opt[0] = weights[0]
    
    if(weights[1] > weights[0]):
        opt[1] = weights[1]
    else:
        opt[1] = opt[0]
      
    #add all max values
    for i in range(2,n):
        opt[i] = max(weights[i] + opt[i-2], opt[i-1])
    
    sol_tot_weight = max(opt[n-1], opt[n-2])
     
    #find positions
    x=n-1;
    while(x>=2):
        if(weights[x] + opt[x-2] > opt[x-1]):
            sol_items.append(x)
            x-=2
        else:
            x-=1
    
    #append base cases positions
    nums = len(sol_items)
    temp = opt[x]
    while(temp>0):
        temp -= weights[sol_items[x]]
        x-=1
    sol_items.append(x+1)
    
    #return at end
    return (opt, sol_tot_weight, sorted(sol_items))


#YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE    

#Read input
f = open("input.txt", "r")
weights = [int(x) for x in f.readline().split()] 
n = len (weights)

#call mwis
(opt, sol_tot_weight, sol_items) = mwis(n, weights)

#output solution
print ' '.join(map(str, opt))
print sol_tot_weight
print ' '.join(map(str, sol_items))


