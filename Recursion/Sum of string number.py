"""Sum of string number"""
def myfunc(li):
    if len(li)==1:
        return int(li[0])
    return int(li[0])+myfunc(li[1:])
def str_sum(s):
    a=" ".join(s).split()
    return myfunc(a)

print(myfunc("123"))
