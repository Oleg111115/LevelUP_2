

x = 10

def multiply_x_by_y():
    y = 5
    global x
    x *= y
    return x

result = multiply_x_by_y()
print(x)

# assert multiply_x_by_y() == 50
