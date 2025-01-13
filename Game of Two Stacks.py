def twoStacks(maxSum,a,b):
    sum_val,count1,i,j=0,0,0,0

    while i<len(a) and sum_val+a[i]<=maxSum:
        sum_val+=a[i]
        i+=1

    count1=i

    while j<len(b):
        sum_val+=b[j]
        j+=1

        while sum_val>maxSum and i>0:
            i-=1
            sum_val-=a[i]

        if sum_val<=maxSum:
            count1=max(count1,i+j)

    return count1

if __name__=="__main__":
    g=int(input())
    for _ in range(g):
        _, _, maxSum=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(twoStacks(maxSum,a,b))
