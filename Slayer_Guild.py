import sys

n = sys.stdin.readline()
data = list(map(int, input().split()))
data.sort()

group = 0 # total number of group
count = 0 # People in the group currently

for i in data:
  count += 1 # Adding the adventurer
  if count >= i: # if the adventurer gathered more than their scary
    group += 1
    count = 0

print(int(group))
