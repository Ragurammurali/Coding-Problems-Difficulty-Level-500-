- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CARTRIP 
- Difficulty: 374

Code:
T=int(input())
for i in range(T):
    X=int(input())
    cost_per_km=10 
    max_range=300 
    default_price=max_range*cost_per_km 
    if(X>max_range):
        print(X*10)
    elif(X<max_range):
        print(default_price)
    elif(X==max_range):
        print(X*10)
