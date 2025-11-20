def mysum(*items):

    if not items:
        return items
    
    output = items[0]

    for item in items[1:]:

        output += item
    
    return output

print(mysum()) ## ()
print(mysum(10, 20, 30, 40))
print(mysum('a', 'b', 'c', 'd')) ## abcd
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))  ## [10, 20, 30, 40, 50, 60, 70, 80] output is this as we have send multiple list as  arguments so it have converted that into a single list 

print(mysum([10, 20, 30], ['a','b','c'], [70, 80]))  ## [10, 20, 30, 'a', 'b', 'c', 70, 80]


print('-'*100)

def mysum_bigger_than(threshold, *items):
    """Sum items, which should be of the same type.
    Ignore any below the value of threshold.
    The arguments should handle the + operator.
    If passed no arguments, then return an empty tuple.
    """
    if not items:
        return items 
    
    output = 0 

    for item in items:
        #print(item)
        if item > threshold:
            output += item

    return output 

print(mysum_bigger_than(10, 20, 30, 40))
print(mysum_bigger_than(3.5, 1.1, 4.0, 3.5, 5.5) )


print('-'*100)

def sum_numeric(items):
    """Sum all items, assuming that they
are integers or can be turned into integers.
"""
    total = 0 

    for item in items:
        try:
            total += int(item)
        
        except ValueError:
            pass 
    
    return total

print(sum_numeric((10, 20, 30, 40)))
print(sum_numeric((10, 20, 30, 40,'50','a')))


print('-' * 100)

def combine_dicts(*args):
    """Return a dict, the result of combining all
    elements of args (which should be dicts). If a key
    occurs in more than one, then the value should be a list
    containing all values from the arguments.
    """
    output = {}

    for d in args:
        for key, value in d.items():
            if key in output:
                try:
                    # Attempt to append if it's already a list (key appeared > 1 time)
                    output[key].append(value)
                except AttributeError:
                    # If it's not a list, it means this is the SECOND time the key appeared.
                    # Convert the existing single value to a list, then append the new value.
                    output[key] = [output[key], value]
            else:
                # First time the key is seen, store the value directly.
                output[key] = value

    return output


d1 = {'A': 'x', 'B': 1}
d2 = {'A': 'y', 'C': 2}
d3 = {'A': 'z', 'B': 3, 'D': 4}

print(combine_dicts(d1,d2,d3))

