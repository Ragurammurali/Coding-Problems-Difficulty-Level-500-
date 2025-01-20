- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/F1RULE
- Difficulty: 487

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    Z=(Y/X)*100
    if(Z<107):
        print("YES")
    elif(Z==107):
        print("YES")
    elif(Z>107):
        print("NO")
