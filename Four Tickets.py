- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FOURTICKETS 
- Difficulty: 302

Code:
T=int(input())
for i in range(T):
    X=int(input())
    total=X*4
    if(total<=1000):
        print("YES")
    elif(total>1000):
        print("NO")
