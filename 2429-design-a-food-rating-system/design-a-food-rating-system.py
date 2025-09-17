class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.values=defaultdict(SortedSet)
        self.curr={}
        self.mappings={}
        for food,cuisine,rating in izip(foods,cuisines,ratings):
            self.values[cuisine].add((-rating,food))
            self.mappings[food]=cuisine
            self.curr[food]=(-rating,food)
        

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        self.values[self.mappings[food]].discard(self.curr[food])
        self.values[self.mappings[food]].add((-newRating,food))
        self.curr[food]=(-newRating,food)
        

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        return self.values[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)