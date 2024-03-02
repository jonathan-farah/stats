def count_vowels(word):
    counter = 0
    s = "aeiouAEIOU"
    for char in word:
        if char in s:
            counter+=1
    print(counter)

animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for i in animals:
    print(i.upper())
for i in range(1,21):
    if i % 2 == 0:
        print(i, " is even")
    else:
        print (i, " is odd")
def sum_of_integers(a, b):
    return a+b
class book:
        name=None
        author = None
        genre = None
        rating = 0
        def __init__(self,name,author,genre,rating):
            self.name = name
            self.author = author
            self.genre = genre
            self.rating = rating
        def get_rating():
              return rating
        def get_genre():
             return genre
        def get_author():
             return author
def check_rating(book):
    score = book.get_rating()
    if score >= 4.5:
        print("high")
        return True
    elif 4.5 > score > 4.0:
         print("medium")
    else:
        print("low")
        return False
def average_rating_by_genre(books, genre):
     sum = 0
     num = 0
     for book in books:
          if book.get_genre == genre:
               sum+=book.get_rating
               num+=1
     return sum//num
def books_by_author(books, author):
     res = []
     index = 0
     for book in books:
        if (book.get_author() == author):
            res[index] = book
            index+=1
        else:
            raise Exception("No Author named that")


