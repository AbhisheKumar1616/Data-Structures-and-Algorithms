"""Reverse an array"""
def rev(li,i):
    if i>=len(li)//2:
        return
    li[i],li[len(li)-i-1]=li[len(li)-i-1],li[i]
    rev(li,i+1)

li=[1,2,3,4,5,6]
rev(li,0)
print(li)

def rev(li):
    if len(li)==1:
        return li
    a=[li[len(li)-1]]
    return a + rev(li[:len(li)-1])

li=[1,2,3,4]
print(rev(li))