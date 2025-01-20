- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SONGS
- Difficulty: 489

Code:
T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    no_of_times_chef_listens_to_song_C_completely=(N/X)/3
    print(int(no_of_times_chef_listens_to_song_C_completely))
