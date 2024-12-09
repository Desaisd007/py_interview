# write a program to count frequency of words appearing in a string

def countwords():
    str1=input('enter a sentence : ')
    # here we convert that sentence to list of words
    l1=str1.split()
    d={}

    for i in l1:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)

countwords()


# d[i] = 0
# This line adds the word i to the dictionary d with an initial value of 0. This is done when the word is first encountered,
# indicating that its count starts at zero.

# d[i] = d[i] + 1
# After ensuring that the word i exists in the dictionary, this line increments the count of that word by 1.
# For example, if the word i is already in the dictionary, this line will increase its value by 1 each time the word is encountered.
