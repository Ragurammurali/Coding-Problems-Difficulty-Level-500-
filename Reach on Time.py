- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TIMELY 
- Difficulty: 279 

Code:
T=int(input())
for i in range(T):
    X=int(input())
    time=30
    if(X>=time):
        print("YES")
    elif(X<time):
        print("NO")
