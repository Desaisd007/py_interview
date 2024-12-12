# Find out pairs with given sum in array of time complexity O(n log n)
# Meta,Amazon,Google
from astropy.time.utils import two_sum

def Pairsum(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1

    while left < right :
        current_sum = arr[left] + arr[right]
        if  current_sum >sum:
            right-=1
        elif current_sum <sum:
            left+=1
        else:
            print('values of pair are : ',arr[left],arr[right])
            right-=1
            left+=1


print("Enter integers separated by spaces: ")
arr=[int(x) for x in input().split()]
sum=int(input('enter amount of sum : '))
Pairsum(arr,sum)





