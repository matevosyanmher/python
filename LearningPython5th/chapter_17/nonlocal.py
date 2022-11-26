x = 99


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)


print('main:', x)

outer()
