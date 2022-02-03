var = True
def func1():
    var = None
    def func2():
        global var
        var = 'hello there!'
        func2()
       
func1()
print(var)       
