"""string Reverse"""
def rev(s):
    if len(s)==0:
        return s
    a=s[len(s)-1]
    return a+rev(s[:len(s)-1])
print(rev("abcd"))
