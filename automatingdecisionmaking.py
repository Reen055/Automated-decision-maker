from random import choice


movies = {'me time': 2, 'maid in manhattan': 3, 'tall girl': 1.5, 'heartbreak high': 2}

movies_list = list(movies.keys())
print(movies_list)

duration_list = list(movies.values())
print(duration_list)

mood = input("What mood are you in: ")
freetime = int(input("How many minutes do you want to watch: "))


if mood == "happy" and freetime  < 3:
    print(f"Watch {movies_list[0]} or {movies_list[2]}")
elif mood == "sad" and freetime > 3:
    print(f"Watch {movies_list[1]}")
elif mood == "heartbroken" and freetime < 3:
    print(f"Watch  {movies_list[3]}" )


