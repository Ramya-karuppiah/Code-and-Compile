"""INPUT:
china
india
OUTPUT:
3
"""
s1=input()
s2=input()
s1=list(s1)
s2=list(s2)
r=0
for i in range(len(s1)):
    
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            s2[j]='*'
            r+=1
            break
    
print(r)
