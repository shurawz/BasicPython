from player import Player

suraj = Player("Suraj")

print(suraj.name)
print(suraj)

suraj.lives -= 1
print(suraj)

suraj.lives -= 1
print(suraj)

suraj.lives -= 1
print(suraj)

suraj.level = 3
print(suraj)

suraj.level += 4
print(suraj)

suraj.level = 2
print(suraj)
