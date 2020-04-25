class Enemy:  # or we can write class Enemy(object) both mean same

    def __init__(self, name="Gotame", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_point = self.hit_points - damage
        if remaining_point >= 0:
            self.hit_points = remaining_point
            print("I took {} points damage and have {} left.".format(damage, self.hit_points))
        else:
            self.lives -= 1
            self.hit_points = 0

    def __str__(self):
        return "Name: {0.name}, Hit Points: {0.hit_points}, Lives: {0.lives}.".format(self)

class Troll(Enemy):
    pass  # In Python, pass keyword is used to execute nothing; it means, when we don't want to execute code,
  # the pass can be used to execute empty.
