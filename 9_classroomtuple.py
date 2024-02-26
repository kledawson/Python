triangle_num = [(n * (n + 1)) // 2 for n in range(1, 11)]
print("The first ten triangle numbers are: ", triangle_num)

class1 = set(["Li", "Audry", "Jia", "Migel", "Tanya"])
class2 = set(["Sasha", "Migel", "Tanya", "Hiroto", "Audry"])
class3 = set(["Migel", "Zhang", "Hiroto", "Anita", "Jia"])
all_students = class1 & class2 & class3
print("Students in all classes:", sorted(list(all_students)))
all_students = class1 | class2 | class3
print("All students:", sorted(list(all_students)))
only_class1 = class1 - (class2 | class3)
print("Only in class1:", sorted(list(only_class1)))
only_class2 = {student for student in class2 if student not in class1}
print("Only in class2:", sorted(list(only_class2)))

film = ('Casablanca', 1942, 'romantic drama')
title, year, genre = film
print("The genre of my favorite movie is: ", genre)

from collections import namedtuple
Movie = namedtuple("Movie", ["title", "year", "genre"])
film = Movie("Casablanca", 1942, "romantic drama")
print("My favorite movie is: ", film.title)

MovieStars = namedtuple("MovieStars", ["title", "year", "genre", "stars"])
favorite_movie = MovieStars("Casablanca", 1942, "romantic drama", ["Humphrey Bogart", "Ingrid Bergman"])
favorite_movie.stars.append("Claude Rains")
if "Ingrid Bergman" in favorite_movie.stars:
    print("My favorite star is: Ingrid Bergman")
print(favorite_movie)

'''Execution results:
The first ten triangle numbers are:  [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
Students in all classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Only in class1: ['Li']
Only in class2: ['Hiroto', 'Sasha']
The genre of my favorite movie is:  romantic drama
My favorite movie is:  Casablanca
My favorite star is: Ingrid Bergman
MovieStars(title='Casablanca', year=1942, genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])'''
print("end of program.")