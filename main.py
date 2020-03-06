import pdb

X = 1
limit = 100
fizz = 3
buzz = 5
fizzbuzz = [fizz, buzz]
output = {}

while X != limit:
    f_modulo = X % fizzbuzz[0]
    b_modulo = X % fizzbuzz[1]
    if f_modulo == 0 and b_modulo == 0:
        output[X] = "fizzbuzz"
    elif f_modulo != 0 and b_modulo != 0:
        output[X] = "NA"
    else:
        output[X] = "Not managed"
    X += 1

print output
