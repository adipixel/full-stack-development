import webbrowser

#super class Video
class Video():
    def __init__(self, title):
        self.title = title


#class Movie which is inherited from class Video        
class Movie(Video):
    def __init__(self, title, storyline,poster,trailer):
        Video.__init__(self, title)
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
