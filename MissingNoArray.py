# find the missing number in array(using summation and XOR operation)

def summation(a):
    n = len(a)+1
    sum1=(n*(n+1))//2
    sum2=sum(a)
    ans = sum1-sum2
    print( 'missing number is : ', ans)


def xor_list(b):
    m = len(b)+1

    #XOR all the numbers from 1 to n
    xor_all= 0
    for i in range (1, m+1):
        xor_all ^= i

    # XOR all the numbers in the given list
    xor_list = 0
    for num in b:
        xor_list ^= num

    # The missing number is the XOR of the two results
    missing_number = xor_all ^ xor_list
    print("Missing number is:", missing_number)

a= [int(x) for x in input('Enter numbers : ').split(',')]
summation(a)
xor_list(a)