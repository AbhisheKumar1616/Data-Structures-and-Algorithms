"""Sum of digits of a number"""
def myfun(n):
    if n<=9 and n>=0:
        return n
    return n%10 + myfun(n//10)
print(myfun(333))