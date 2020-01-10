def divisors(integer):
    arr=[]
    for i in range(2, integer-1):
        if integer%i==0:
            arr.append(i)
    if not arr:
        return str(integer)+' is prime'
    else:
        return arr
