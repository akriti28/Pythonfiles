import math

def gaincalc(gainlist,n,data,attnames,distinctvaluesoftarget,targetlist,target):
    infodic={}
    for i in gainlist:
        distinct=[]
        for j in range(n):
            distinct.append(data[j][attnames.index(i)])
        distinct=list(set(distinct))
        discount={}
        infoDatt=0
        for j in distinct:
            discount[j]=0
            entropy=0
            countofdistincttarget={}
            for k in distinctvaluesoftarget:
                countofdistincttarget[k]=0
            for k in range(n):
                if data[k][attnames.index(i)]==j:
                    discount[j]=discount[j]+1
                    for p in distinctvaluesoftarget:
                        if data[k][attnames.index(target)]==p:
                            countofdistincttarget[p]=countofdistincttarget[p]+1
            #print(countofdistincttarget)
            for k in distinctvaluesoftarget:
                #print("k:",k,"\n",countofdistincttarget[k],discount[j])
                if countofdistincttarget[k]!=0:
                    entropy=entropy-(countofdistincttarget[k]/discount[j])*math.log(countofdistincttarget[k]/discount[j],2)
                
            infoDatt=infoDatt+entropy*discount[j]/n          
        infodic[i]=infoDatt
        #print("Discount:",discount)
    return infodic

def expandcalc(tree,data,n,m,attnames,target,maxgain,lst):
    if maxgain==0:
        targetlist=[]
        ind=attnames.index(target)
        for i in range(n):
            targetlist.append(data[i][ind])
        distinctvaluesoftarget=list(set(targetlist))
        infoD=0
        x=0
        for i in range(len(distinctvaluesoftarget)):
            x=targetlist.count(distinctvaluesoftarget[i])
            infoD=infoD-(x/n)*(math.log(x/n,2))
        #print("Info(D) :",infoD)
        gainlist=attnames[::]
        gainlist.remove(target)
        gaindic=gaincalc(gainlist,n,data,attnames,distinctvaluesoftarget,targetlist,target)
        for i in gainlist:
            gaindic[i]=infoD-gaindic[i]
        #print(gaindic)
        maxgain1=max(gaindic.values())
        for i,j in gaindic.items():
            if j==maxgain1:
                maxgain=i
        #print("MaxGain :",maxgain)
        lst.append(maxgain)
        tree=expandcalc(tree,data,n,m,attnames,target,maxgain,lst)
        #print(tree)
    else:
        a=[]
        subsets={}
        for i in range(len(data)):
            a.append(data[i][attnames.index(maxgain)])
        a=list(set(a))
        for i in a:
            b=[]
            for j in range(len(data)):
                if data[j][attnames.index(maxgain)]==i:
                    b.append(data[j])
            subsets[i]=b
        #print(subsets)
        subsets=list(subsets.items())
        for i,j in subsets:
            flag=0
            targetlist=[]
            ind=attnames.index(target)
            for b in range(len(j)):
                targetlist.append(j[b][ind])
            distinctvaluesoftarget=list(set(targetlist))
            if len(distinctvaluesoftarget)==1:
                flag=1
            if flag==1:
                temp=lst[::]
                temp.append(i)
                temp.append(distinctvaluesoftarget[0])
                tree.append(temp)
                #print(tree)
            else:
                temp=lst[::]
                temp.append(i)
                maxgain=0
                data=j
                n=len(data)
                tree=expandcalc(tree,data,n,m,attnames,target,maxgain,temp)
                #print(tree)
        
    return tree


n=int(input("Enter no of transactions:\n"))
m=int(input("Enter no of attributes:\n"))
attnames=list(map(str,input().split()))
if len(attnames)!=m:
    print("no of attributes "+str(len(attnames))+" is not equal to ",m)
    exit(0)
data=[]
for i in range(n):
    print("Enter the values of all attributes:")
    data.append(list(map(str,input().split())))
target=input("Enter the target label: ")
######################################################################
##########################--PRINTING DATASET--########################
######################################################################
print("\n\n****************************\n---PRINTING DATASET---\n****************************\n\n")
print(attnames)
for i in range(n):
    print(data[i])
print("Target Label is :",target)
##############################################################################
##########################--PERFORMING DECISION TREE--########################
##############################################################################
print("\n\n*******************************\n--PERFORMING DECISION TREE--\n*******************************\n\n")
#################################RECURSIVE FUNCTION CALL###########################
tree=['root']
maxgain=0
lst=[]
tree=expandcalc(tree,data,n,m,attnames,target,maxgain,lst)
print(tree)
print("\n\n*******************************\n----------DONE!!!!------------\n*******************************\n\n")
