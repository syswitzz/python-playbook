# 1. Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"
say_hi = greet  

# 2. Passing a function as an argument
def apply(f, v):
    return f(v)
res = apply(say_hi, "Bob")

# 3. Returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult
dbl = make_mult(2)  # dbl ittself is a function