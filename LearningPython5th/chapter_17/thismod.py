var = 99
def local():
    var = 0

def global_var1():
    global var
    var += 1

def global_var2():
    var = 0
    import thismod
    thismod.var += 1
    print('in global_var2:', thismod.var)

#
# def global_var3():
#     var = 0
#     import sys
#     glob = sys.modules[__name__]
#     glob.var += 1
#

def test():
    print(var)
    local(), global_var1(), global_var2(),  # global_var3()
    # print(var)


#
if __name__ == '__main__':
    test()
