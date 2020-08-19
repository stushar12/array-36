import sys

n=int(input("Enter number of elements in main array1: "))
print("Enter elements :")
arr1=[]
for i in range(0,n):
        z=int(input())
        arr1.append(z)

k=int(input("Enter value of k: "))

sum=0
length=0
flag=False
maxlength=-sys.maxsize
hash={}
for i in range(0,n):
        sum=sum+arr1[i]
        if sum == k:
                maxlength=i+1
                flag=True
        elif( (sum-k) in hash):
                length=i-hash[sum-k]
                if(maxlength<length):
                        flag=True
                        maxlength=length
        if sum not in hash:
                hash[sum]=i
if(flag):
        print(f"Longest subarray with sum equals to k : {maxlength} ")
