import fresh_tomatoes
import media
# creating objects of class Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                  "A story of marine",
                  "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                  "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


lor = media.Movie("Lord of the Rings",
                  "A story of a powerful ring",
                  "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
                  "https://www.youtube.com/watch?v=Pki6jbSbXIY")

forest = media.Movie("Forest Gump",
                  "A story of a different guy!",
                  "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                  "https://www.youtube.com/watch?v=bLvqoHBptjg")

happiness = media.Movie("Pursuit of happyness",
                  "An inspiring story",
                  "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                  "https://www.youtube.com/watch?v=bTJ-0zVAsEA")

swadees = media.Movie("Swadees",
                  "A story of a true Indian",
                  "https://upload.wikimedia.org/wikipedia/en/8/85/Swades_poster.jpg",
                  "https://www.youtube.com/watch?v=x6QOtayfj-0")

#List of Movie objects
movies = [toy_story, avatar, lor, forest,happiness,swadees]

#calling open_movies_page() from fresh_tomatoes module/file
fresh_tomatoes.open_movies_page(movies)
