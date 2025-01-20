- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SUBSCRIBE 
- Difficulty: 315 

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X>30):
        print("YES")
    elif(X<30):
        print("NO")
    elif(X==30):
        print("NO")
