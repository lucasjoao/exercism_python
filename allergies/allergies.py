db = {1: 'eggs',
      2: 'peanuts',
      4: 'shellfish',
      8: 'strawberries',
      16: 'tomatoes',
      32: 'chocolate',
      64: 'pollen',
      128: 'cats'}


class Allergies:
    def __init__(self, score):
        self.lst = self.define_allergies(score)

    def is_allergic_to(self, thing):
        return thing in self.lst

    def define_allergies(self, score):
        values = []
        for i in range(0, score+1):
            if 2 ** i > score and 2 ** (i-1) <= 128 and i != 0:
                values.append(db[2 ** (i-1)])
                score -= 2 ** (i-1)
                j = 2
                while score != 0:
                    if 2 ** (i-j) <= score:
                        values.append(db[2 ** (i-j)])
                        score -= 2 ** (i-j)
                    j += 1
                break
        return values
