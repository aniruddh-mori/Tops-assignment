
titles = ["3 Idiots", "Dangal", "Jawan"]
genres = ["Comedy", "Drama", "Action"]
ratings = [8.4, 8.3, 7.0]

print(list(zip(titles,genres,ratings)))
movies = []
for title, genre,rating in zip(titles,genres,ratings):
    info = {
        "title" : title,
        "genere" : genre,
        "ratting" : rating
    }
    movies.append(info)
print(movies)
