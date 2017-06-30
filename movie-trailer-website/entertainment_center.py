import fresh_tomatoes
import media
# Toy story movie: movie title, storyline, poster image, and trailer
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar movie: movie title, storyline, poster image, and trailer
avatar = media.Movie(
    "Avatar",
    "A story of marine",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# Lords of the rings movie: movie title, storyline, poster image, and trailer
lor = media.Movie(
    "Lord of the Rings",
    "A story of a powerful ring",
    "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Pki6jbSbXIY")

# Forest Gump movie: movie title, storyline, poster image, and trailer
forest = media.Movie(
    "Forest Gump",
    "A story of a different guy!",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=bLvqoHBptjg")

# Pursuit of happyness movie: movie title, storyline, poster image, and trailer
happiness = media.Movie(
    "Pursuit of happyness",
    "An inspiring story",
    "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",  # NOQA
    "https://www.youtube.com/watch?v=bTJ-0zVAsEA")

# Swades movie: movie title, storyline, poster image, and trailer
swadees = media.Movie(
    "Swadees",
    "A story of a true Indian",
    "https://upload.wikimedia.org/wikipedia/en/8/85/Swades_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=x6QOtayfj-0")

# List of Movie objects
movies = [toy_story, avatar, lor, forest, happiness, swadees]

# calling open_movies_page() from fresh_tomatoes module/file
fresh_tomatoes.open_movies_page(movies)
