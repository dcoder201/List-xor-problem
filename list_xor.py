def list_xor(n,list1,list2):
    k=list(set(list1))+list(set(list2))
    if k.count(n)==0 or k.count(n)==2:
        return False 
    else:
        return True
        
print(list_xor(1, [1, 2, 3], [4, 5, 6]))
