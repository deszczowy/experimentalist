import datetime as dt
import random as rn

class RandomMachine:

    def __init__(self):
        now = int(dt.datetime.now(dt.UTC).timestamp())
        rn.seed(now)

    def random_frame(self) -> float:
        sign = -1.0 if rn.random() < 0.5 else 1.0
        return rn.random() * sign

#
# r = RandomMachine()
# for i in range(0,100):
#    print(r.random_frame())
#
