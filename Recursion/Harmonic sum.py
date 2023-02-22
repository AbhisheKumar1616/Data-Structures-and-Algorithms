"""Harmonic sum ==> 1+(1/2)+(1/3)+......(1/n-1)"""
def myfun(n):
    if n==1:
        return 1
    return 1/n + myfun(n-1)
print(f"{myfun(3):.2f}")
