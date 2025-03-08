n, money = map(int,input().split())
wallet = []
count = 0
i = 0
for i in range(n):
  a = int(input())
  wallet.append(a)

wallet.sort(reverse = True)

while money != 0:
  if wallet[i] > money:
    i += 1
  elif wallet[i] == money:
    money = 0
    count = 1
  elif wallet[i] <= money:
    money = money - wallet[i]
    count +=1
  print(money)
  print(count)

print('---------------------------')
print(count)
  