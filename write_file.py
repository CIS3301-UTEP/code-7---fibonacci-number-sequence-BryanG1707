filename = 'my_first_file.txt'

file = open(filename, mode = 'a')

movies = ['Scream', 'IT', 'The Nun', 'Annabelle', 'Jason']

for movie in movies:
    # print(movie)
    file.write(movie)
    file.write('\n')