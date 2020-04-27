class Enemy:  # or we can write class Enemy(object) both mean same

    def __init__(self, name="Gotame", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_point = self._hit_points - damage
        if remaining_point >= 0:
            self._hit_points = remaining_point
            print("I took {} points damage and have {} left.".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name}, you have {0._lives} life left.".format(self))
            else:
                print("{0._name}, you're dead now.".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Hit Points: {0._hit_points}, Lives: {0._lives}.".format(self)


class Troll(Enemy):
    # In Python, pass keyword is used to execute nothing; it means, when we don't want to execute code,
    # the pass can be used to execute empty.

    
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def test(self):
        print("I am {0._name}".format(self))


class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        import random
        if random.randint(1, 3) == 3:
            print("**** {0._name} dodges ****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


# Challenge part...
class VampyreKing(Vampyre):

    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140
        self._lives = 14

    def take_damage(self, damage):
        super().take_damage(damage // 4)