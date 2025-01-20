- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/HOTCOLD 
- Difficulty: 410

Code:
T=int(input())
for i in range(T):
    C=int(input())
    if(C>20):
        print("HOT")
    elif(C<20):
        print("COLD")
    elif(C==20):
        print("COLD")
