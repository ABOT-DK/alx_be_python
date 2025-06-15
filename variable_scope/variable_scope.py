x = "Global X"

def local_scope():
    y = "y is a Local Scope"
    print(y)
    
local_scope()
print(x)