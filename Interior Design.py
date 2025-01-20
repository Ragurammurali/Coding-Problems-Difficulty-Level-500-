- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INTRDSGN 
- Difficulty: 373

Code:
T=int(input())
for i in range(T):
    X1,Y1,X2,Y2=map(int,input().split())
    total1=X1+Y1
    total2=X2+Y2
    if(total1<total2):
        print(total1)
    elif(total2<total1):
        print(total2)
    elif(total1==total2):
        print(total1)
