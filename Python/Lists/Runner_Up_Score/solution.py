n = int(input())
scores = list(map(int, input().split()))

highest = scores[0]

for x in scores:
    if x > highest:
        highest = x

runner_up = -1

for x in scores:
    if x < highest and x > runner_up:
        runner_up = x

print(runner_up)
