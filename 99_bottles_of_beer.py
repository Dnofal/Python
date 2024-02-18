class bottle_num:
    def __init__(self, num):
        self.num = num

    def container(self):
        return "bottle" if self.num == 1 \
        else "bottles"

    def pronoun(self):
        return "it" if self.num == 1 else "one"

    def action(self):
        if self.num == 0:
            return "Go to the store and buy some more"
        else:
            return f"Take {self.pronoun()} down and pass it around"

    def quantity(self):
        return "No more" if self.num == 0 \
        else str(self.num)

    def successor(self):
        return 99 if self.num == 0 \
        else self.num - 1

class Bottles:
    # Constructor
    def __init__(self):
        pass

    @staticmethod
    def create():
        return Bottles()

    # instant method
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return [self.verse(num) for num in range(upper, lower-1, -1)]

    def verse(self, num):
        next_num = self.successor(num)
        return f"{self.quantity(num)} {self.container(num)} of beer on the wall, {self.quantity(num)} {self.container(num)} of beer. {self.action(num)}, {self.quantity(next_num)} {self.container(next_num)} of beer on the wall."

    @staticmethod
    def container(num):
        return bottle_num(num).container()

    @staticmethod
    def pronoun(num):
        return bottle_num(num).pronoun()

    @staticmethod
    def quantity(num):
       return bottle_num(num).quantity()

    @staticmethod
    def successor(num):
       return bottle_num(num).successor()

    @staticmethod
    def action(num):
       return bottle_num(num).container()

# Example usage
bottles = Bottles.create()
print(bottles.song())
