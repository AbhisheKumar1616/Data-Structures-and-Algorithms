#Palindrom String
def rev(s,i=0,f=True):
    if i>=len(s)//2:
        return f
    if s[i]!=s[len(s)-i-1]:
        return False
    i+=1
    return rev(s,i,True)
print(rev("ababaca"))