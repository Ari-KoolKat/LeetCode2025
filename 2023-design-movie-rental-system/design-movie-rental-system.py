from bisect import bisect_left, bisect_right, insort
from collections import defaultdict

class MovieRentingSystem:
    def __init__(self, n, entries):
        self.n = n
        self.unrented = defaultdict(list)  # movie -> sorted list of (price, shop, movie)
        self.rented = []                   # sorted list of (price, shop, movie)
        self.price = {}                    # (shop, movie) -> price
        for shop, movie, p in entries:
            self.price[(shop, movie)] = p
            insort(self.unrented[movie], (p, shop, movie))

    def search(self, movie):
        res = []
        arr = self.unrented.get(movie, [])
        for i in range(min(5, len(arr))):
            res.append(arr[i][1])
        return res

    def rent(self, shop, movie):
        p = self.price[(shop, movie)]
        arr = self.unrented[movie]
        idx = bisect_left(arr, (p, shop, movie))
        if idx < len(arr) and arr[idx] == (p, shop, movie):
            arr.pop(idx)
        insort(self.rented, (p, shop, movie))

    def drop(self, shop, movie):
        p = self.price[(shop, movie)]
        idx = bisect_left(self.rented, (p, shop, movie))
        if idx < len(self.rented) and self.rented[idx] == (p, shop, movie):
            self.rented.pop(idx)
        insort(self.unrented[movie], (p, shop, movie))

    def report(self):
        res = []
        for i in range(min(5, len(self.rented))):
            res.append([self.rented[i][1], self.rented[i][2]])
        return res