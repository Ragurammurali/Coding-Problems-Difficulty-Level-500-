- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/WATERFLOW 
- Difficulty:  483

Code:
T=int(input())
for i in range(T):
    W,X,Y,Z=map(int,input().split())
    tap_on_filled=Y*Z 
    total_water_in_bucket=W+tap_on_filled
    if(total_water_in_bucket>X):
        print("overFlow")
    elif(total_water_in_bucket<X):
        print("unfilled")
    elif(total_water_in_bucket==X):
        print("filled")
