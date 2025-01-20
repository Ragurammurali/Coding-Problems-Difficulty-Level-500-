- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SIXFRIENDS 
- Difficulty: 382

Code:
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    double_room_cost=3*x 
    triple_room_cost=2*y  
    if(double_room_cost<triple_room_cost):
        print(double_room_cost)
    elif(triple_room_cost<double_room_cost):
        print(triple_room_cost)
    elif(double_room_cost==triple_room_cost):
        print(double_room_cost)
