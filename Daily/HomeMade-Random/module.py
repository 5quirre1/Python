import time

class HomemadeRandom:
    def __init__(self, seed_value=None):
        self.seed(seed_value if seed_value is not None else int(time.time_ns()))

    def seed(self, seed_value):
        self._seed = (seed_value ^ 0xDEADBEEF) & 0xFFFFFFFF

    def _next(self):
        self._seed = (self._seed * 1664525 + 1013904223) & 0xFFFFFFFF
        return self._seed

    def randint(self, a, b):
        return a + (self._next() % (b - a + 1))

    def random(self):
        return self._next() / 0xFFFFFFFF

    def uniform(self, a, b):
        return a + (b - a) * self.random()

    def randrange(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        if step <= 0:
            raise ValueError("Step must be positive")
        return start + step * (self._next() % ((stop - start) // step))

    def choice(self, seq):
        if not seq:
            raise ValueError("Cannot choose from an empty sequence")
        return seq[self.randint(0, len(seq) - 1)]

    def shuffle(self, seq):
        for i in range(len(seq) - 1, 0, -1):
            j = self.randint(0, i)
            seq[i], seq[j] = seq[j], seq[i]


rand = HomemadeRandom()
