"""задача про фермерское хозяйство черники"""

countBush = int(input('Введите количество кустов: '))
berries = [int(berries) for berries in input().split()][:countBush]
print(berries)
maxSumBerries = 0
for bush in range(0, len(berries) - 1):
    if maxSumBerries < berries[bush - 1] + berries[bush] + berries[bush + 1]:
        maxSumBerries = berries[bush - 1] + berries[bush] + berries[bush + 1]
if maxSumBerries < berries[0] + berries[-2] + berries[-1]:
   maxSumBerries = berries[0] + berries[-2] + berries[-1]  
print(maxSumBerries)           