#n_comp  is number of products
#cap is capacity of sacj
#cpuw_dict is a dictionary with cost per unit weight as key and weight of the same available as value
'''the cost would be calculated by multiplying key, value pair of cpuw_dict if remaining capacity is greater
than that available of the maximum key and multiplying key, remaining if remaining capacity is lesser than that
available of the maximum key'''
n_comp, cap = map(int, input().split())
cpuw_dict = {}
for j in range (n_comp):
    cost, weight = map(float, input().split())
    cost_per_unit_weight = cost/weight
    cpuw_dict[cost_per_unit_weight] = weight

def fill_sack(d, capacity):
    total_cost = 0
    remaining = capacity
    if capacity == 0:
        return 0
    while remaining > 0 and len(d)>0 :
        max_cpuw = max(d)
        key = d[max_cpuw]
        if key <= remaining:
            cost = max_cpuw*key
            del d[max_cpuw]
            remaining -= key
            total_cost += cost
        else:
            cost = max_cpuw*remaining
            total_cost += cost
            remaining = 0
            
    return total_cost
result = fill_sack(cpuw_dict, cap)
print(f"{result:.4f}")
   
        
        
        
        
        
    

