def dictkwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
dictkwargs(name="valli",age=40)
print()


def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s"%(key,value))
myFun(first='Geeks',mid='for',last='Geeks')
print()





