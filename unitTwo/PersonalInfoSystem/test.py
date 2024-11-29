# print(eval("134+234"))
# x = 4j

# print(x * x)
x= 1
y = 2

def test():
    global x, y
    print(x, y)

test()
print(str(x), int(x), float(x), eval(f"{x} + {y}"), f"{x} + {y}")
