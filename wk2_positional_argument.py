# -- more examples in the positional argument

def division_op(x, y=1):                     # x = pos. argument, y = 1 keyword's value (optional)
    ret = 0
    if y:
        print("x = ", x, "y = ", y)
        ret = x/y
    else:   # if y == 0
        print("x = ", x)
        ret = x
    return ret

result = division_op(4,10)  # positional arguments
result = division_op(4)     # positional arguments
result = division_op(y=4, x=10) # positional arguemnts, it's ok
#result - division_op(y=4, x)    # not allowed default aurgument before keyword
# this last example will be a syntax error : positional argument follows keyword argument

# let's try more no arbitrary arguments on computing area of different shapes by passing a tuple
# compare and contrast how they pass a tuple

#def compute_area(dim): result = compute_area((3, 2))

#def compute_area(*dim): result = compute_area(3, 2)

def compute_area(*dim):
    result = 0
    if (len(dim) == 1):     # x and pi for 2d circle
        result = 3.14 * dim[0] ** 2
    elif (len(dim) == 2):   # x and y for 2d rectangle
        result = dim[0] * dim[1]
    elif (len(dim) == 3):   # x, y, and z for 3d volume
        result = dim[0] * dim[1] * dim[2]
    else:
        print("invalid input parameters")
    return result

result = compute_area(2)
print("result is: ", result)

result = compute_area(3,2)
print("result is: ", result)

result = compute_area(3, 2, 9.2)
print("result is: ", result)

i = [2,3]
result = compute_area(*i)
print("result is:", result)