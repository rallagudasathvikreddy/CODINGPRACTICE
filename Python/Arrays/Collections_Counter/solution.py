from collections import Counter

n = int(input())

size_of_shoe = list(map(int, input().split()))

no_of_customers = int(input())

stock = Counter(size_of_shoe)

money = 0

for i in range(no_of_customers):
    size, price = map(int, input().split())

    if stock[size] > 0:
        money += price
        stock[size] -= 1

print(money)
