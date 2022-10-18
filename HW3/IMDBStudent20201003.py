#/user/bin/python3

 

import sys

movie_elements=[]

genre_list={}

with open(sys.argv[1], "rt") as f:

    data = f.read()

    

    rows = data.split("\n")

    for row in rows:

        movie=row.split('::')

        movie_element = [movie[0], movie[1], movie[2]]

        movie_elements.append(movie_element)

        genres=movie[2].split('|')

        for genre in genres:

            if genre in genre_list:

                genre_list[genre] += 1

            else:

                genre_list[genre] = 1  

with open(sys.argv[2], 'w') as fp:

    for row in genre_list:

        fp.write(row+ ' ' + str(genre_list[row]) + '\n')

