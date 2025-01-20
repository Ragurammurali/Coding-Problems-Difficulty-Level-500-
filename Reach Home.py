- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/REACH_HOME 
- Difficulty: 395

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    distance_that_can_be_travelled=X*5
    if(distance_that_can_be_travelled>=Y):
        print("YES")
    elif(distance_that_can_be_travelled<Y):
        print("NO")
