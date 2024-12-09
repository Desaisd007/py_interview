# we take two string as input and answer common charactes between them.

def common_letter():
    str1=input('enter first string : ')
    str2=input('enter second strig : ')
    s1=set(str1)
    s2=set(str2)
    # & etracting common letter from strings
    ans= s1 & s2
    print(ans)

common_letter()