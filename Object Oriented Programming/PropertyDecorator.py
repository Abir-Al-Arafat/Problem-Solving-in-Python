# declare a movie class which will have two instance attributes title and rating.
# the rating attribute will be non-public.
# use property decorator to get and set the rating attribute. the rating has to be between 0 to 5.

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    # using property decorator to get the rating instance
    @property
    def rating(self):
        return self._rating

    # using property decorator to set the rating instance
    @rating.setter
    def rating(self, new_rating):
        self.new_rating = new_rating
        if 0 <= self.new_rating <= 5:
            self._rating = self.new_rating
        else:
            print("rating has to be between 0 and 5")
            return


movie = Movie("abc", 4.5)

print(movie.rating)

movie.rating = -7

print(movie.rating)
