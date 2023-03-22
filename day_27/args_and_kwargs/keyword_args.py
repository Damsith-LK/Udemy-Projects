# Here is how to make a function that can accept any number of keyword arguments. ** is needed

def func(**kwargs):
    for (key, value) in kwargs.items():
        print(key, value)


func(a="sfd", o=["fast", "ffd"])
print('\n\n\n\n')


def math(number, **kwargs):
    number += kwargs["add"]
    number -= kwargs["subtract"]
    number *= kwargs["multi"]
    number /= kwargs["divide"]
    print(number)


math(500, add=4, subtract=234, multi=34, divide=5.43)
print('\n\n\n')

# Similarly we can do the same thing with a class


class Song:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.album = kwargs.get("album")
        self.artist = kwargs.get("artist")
        self.year = kwargs.get("year")

    def info(self):
        print(f"The song '{self.name}' in album {self.album} was a song by {self.artist} in the year {self.year}")


slim_shady = Song(name="The Real Slim Shady", album="Marshell Mathers LP", artist="Eminem", year=2000)
slim_shady.info()