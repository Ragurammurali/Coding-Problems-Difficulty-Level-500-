- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SLEEP 
- Difficulty: 348

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X<7):
        print("YES")
    elif(X>7):
        print("NO")
    elif(X==7):
        print("NO")
