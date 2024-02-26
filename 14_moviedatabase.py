scifi = ["Alien", "Solaris", "Inception", "Moon"]
comedy = ["Borat", "Idiocracy", "Superbad", "Bridesmaids"]

movie = input("Enter the name of a movie: ")

if movie in scifi:
    print("The genre of the movie is Science Fiction.")
elif movie in comedy:
    print("The genre of the movie is Comedy.")
else:
    print("The genre of the movie is unknown.")

loop = True
while loop == True:
    movie = input("Enter the name of another movie (STOP to end): ")
    if movie in scifi:
        print("The genre of the movie is Science Fiction.")
    elif movie in comedy:
        print("The genre of the movie is Comedy.")
    elif movie.upper() == "STOP":
        loop = False
    else:
        print("The genre of the movie is unknown.")

for i in range(10, -1, -2):
    print(i)

movies = {"The Wizard of Oz": 1939,
        "The Godfather": 1972,
        "Lawrence of Arabia": 1962,
        "Raging Bull": 1980}

for movie, year in sorted(movies.items()):
    print(f"{movie} was made in {year}.")

'''Expected results:
Enter the name of a movie: Moon
The genre of the movie is Science Fiction.
Enter the name of another movie (STOP to end): Superbad
The genre of the movie is Comedy.
Enter the name of another movie (STOP to end): Dunkirk
The genre of the movie is unknown.
Enter the name of another movie (STOP to end): STOP
10
8
6
4
2
0
Lawrence of Arabia was made in 1962.
Raging Bull was made in 1980.
The Godfather was made in 1972.
The Wizard of Oz was made in 1939.'''

print("end of program.")