x = 'global x'

m = min([2, 6, 8, 4, 6, 8, 2, 5, 8, 3])
print(m)


def test():
    y = 'local y'
    x = 'local x'
    print(y)
    print(x)

    print(x)


test()
print(x)
