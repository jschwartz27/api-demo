import random


class RandomNumbers:

    @staticmethod
    def get_random_gaussian(sigma: int = 15) -> int:
        return int(random.gauss(mu=50, sigma=sigma))

    @staticmethod
    def get_random_number(n: int = 100) -> int:
        assert n >= 1, "Integer range value must be great than 1"
        return random.randint(a=1, b=n)
