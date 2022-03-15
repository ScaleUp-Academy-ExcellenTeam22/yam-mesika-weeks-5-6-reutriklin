def join(*lists,sep='-'):
    if lists==None:
        return  None
    newList=[]
    for l in lists:
        for element in l:
            newList=newList+[element]
        if  l != lists[-1]:
            newList+=sep
    print (newList)
    return newList