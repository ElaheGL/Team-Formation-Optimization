player_count = int(input())
game_lis = [ int(x) for x in input().split()]
correct_lis = game_lis[:player_count]
team_lis = []
for num in correct_lis:
    if ((num == 0) or (num == 1) or (num == 2)):
        team_lis.append(num)
        x = len(team_lis) // 3

print(x)