# def hashing(lst):

lst=[31,79,61,2,36,75,96,25,60,44]
myDict=dict()
for i in range (len(lst)):
    hf=lst[i]%10
    while(hf in myDict and hf<(len(lst)-1)):
        hf+=1
        if(hf>=10):
            hf%=10  
    myDict.update({hf:lst[i]})
    i+=1
print(myDict)
ls=sorted(myDict)
odict=dict()
for j in ls:
    odict.update({j:myDict[j]})

print(odict)
    
# hashing(lst1)