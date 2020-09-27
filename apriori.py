t1=set([1,2,3,4])
t2=set([1,2,3,4,5])
t3=set([2,3,4])
t4=set([2,3,5])
t5=set([1,2,4])
t6=set([1,3,4])
t7=set([2,3,4,5])
t8=set([1,3,4,5])
t9=set([3,4,5])
t10=set([1,2,3,5])
li=[]
c=set()
temp1=set()
temp2=set()
ct=0
countl=[]
countc=[]
l1={}
li=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]

import itertools

for i in li:
    c=c|i


for j in c:
    ct=0
    for a in li:
        if j in a:
            ct=ct+1
    
    if ct>4:
        countl.append(ct)
        temp1.add(j)
        
    countc.append(ct)

can1=dict(zip(c,countc))
print(can1)
l1=dict(zip(temp1,countl))
print(l1)

c2=set(itertools.combinations(c,2))

countc2=[]
countl2=[]
for i in c2:
    ct=0
    for j in li:
        if i[0] in j and i[1] in j:
            ct=ct+1
    if ct>=4:
        countl2.append(ct)
        temp2.add(i)

    countc2.append(ct)

can2=dict(zip(c2,countc2))
print(can2)
l2=dict(zip(temp2,countl2))
print(l2)

c3=set(itertools.combinations(c,3))

countc3=[]
countl3=[]
temp3=set()
for i in c3:
    ct=0
    for j in li:
        if i[0] in j and i[1] in j and i[2] in j:
            ct=ct+1
    if ct>=4:
        countl3.append(ct)
        temp3.add(i)

    countc3.append(ct)

can3=dict(zip(c3,countc3))
print(can3)
l3=dict(zip(temp3,countl3))
print(l3)
        
c4=set(itertools.combinations(c,4))
countc4=[]
countl4=[]
temp4=set()
for i in c4:
    ct=0
    for j in li:
        if i[0] in j and i[1] in j and i[2] in j and i[3] in j:
            ct=ct+1
    if ct>=4:
        countl4.append(ct)
        temp4.add(i)

    countc4.append(ct)

can4=dict(zip(c4,countc4))
print(can4)
l4=dict(zip(temp4,countl4))
print(l4)
        


