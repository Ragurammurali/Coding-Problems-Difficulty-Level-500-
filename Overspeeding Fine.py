- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FINE 
- Difficulty: 335

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X<=70):
        print(0)
    elif(X>70 and X<=100):
        print(500)
    elif(X>100):
        print(2000)
