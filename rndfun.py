import random
c=0
n=int(input("Enter no.:"))
while True:
    c+=1
    ans=random.randint(100,200)
    if n==ans:
        print("success after:",c,"tries")
        break
