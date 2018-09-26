import datetime

class Transaction:
    def __init__(self):
        self.who = "Herbert"
        self.when = datetime.datetime.now()
        self.amount = 100

    def hashCode(self):
        h = 17
        h = 31*h + hash(self.who)
        h = 31*h + hash(self.when)
        h = 31*h + hash(self.amount)
        return h

    def hash(self, key):
        return abs(hash(key)) % self.M
t = Transaction()
print(t.hashCode())