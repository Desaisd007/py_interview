#  here we convert two lists( list one contains strings anf list two contains numbers ). we converts that both list in
# single dictionary

def list_to_dict():
    list1 = [x for x in  input("enter a list of your favourite 3 foods : ").split(',')]
    list2 = [x for x in  input("enter price of above items : ").split(',')]
    ans =  dict(zip(list1,list2))
    print(ans)

list_to_dict()
