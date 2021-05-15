def big(a):
    ind=0
    for i in range (len(a)):
        if i > 0:
            i='Big'
            a[ind]=i
            ind+= 1
    return(a)
print(big([1,-8]))



def count(a):
    counter=0
    for i in range(len(a)):
        if i>0:
            counter +=1
    a[-1]=counter

    return(a)

print(count([-1,1,1,1]))



def totalsum(a):
    sum=0
    for i in range(len(a)+1):
        sum=sum+i
    return(sum)
 
print(totalsum([1,2,3,4]))


def avg(a):
    num=len(a)
    sum=0
    for i in range(num+1):
        sum=sum+i
        print(i)
    return(sum/num)

print(avg([10,25,3,4]))


def length(a):
    return(len(a))

print(length([]))



def min(a):
    if len(a)==0:
        
        return False
    else:
        minum=a[0]
        for i in a:
            if i<minum:
                minum=i
    return(minum)

print(min([]))


def max(a):
    if len(a)==0:
        return False
    else:
        big=a[0]
        for i in a:
            if i>big:
                big=i
        return (big)

print(max([]))



def ultimatedic(a):
    if len(a)==0:
        return False
    else:
        max=a[0]
        min=a[0]
        leng=len(a)
        sum=0
        for i in a:
            if i>max:
                max=i
            else:
                min=i
            sum=sum+i
        avg=sum/leng
    ultimate={
        "sumTotal":sum,
        "average":avg,
        "minimum":min,
        "maximum":max,
        "length":leng,
    }

    return(ultimate)

print(ultimatedic([1,2,3,4,5]))




def revlist(a):
    counter=len(a)//2
    rev=-1
    for i in range (counter):
        extra=a[i]
        a[i]=a[rev]
        a[rev]=extra
        rev-=1
    return(a)

print(revlist([1,2,3,-8]))