var = True
def func1():
    var = None
    def func2():
        global var
        var = 'Hello there!'
        func2()
       
func1()
print(var)       
