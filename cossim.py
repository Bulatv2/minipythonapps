import math

class CosSim:
    """класс вычисления косинусной близости"""
    def __init__(self, vect1, vect2):
        self.vect1 = vect1
        self.vect2 = vect2

    def cossim(self):
        scalarProduct = moduloV1 = moduloV2 = 0
        if len(self.vect1) > len(self.vect2):
            self.vect2.extend(0 for _ in range(len(self.vect1) - len(self.vect2)))
        else:
            self.vect2.extend(0 for _ in range(len(self.vect2) - len(self.vect1)))
        for i in range(len(self.vect1)):
            scalarProduct += self.vect1[i] * self.vect2[i]
            moduloV1 += self.vect1[i] * self.vect1[i]
            moduloV2 += self.vect2[i] * self.vect2[i]
            if scalarProduct != 0:
                return round(scalarProduct/(math.sqrt(moduloV1) * math.sqrt(moduloV2)), 3)
            else:
                return False
