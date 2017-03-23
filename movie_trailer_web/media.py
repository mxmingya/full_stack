import webbrowser as wb

class Movie():
    def __init__(self, title, storyline, poster_image_url, trailer_youtube__url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube__url


    def show_trailer(self):
        wb.open(self.trailer_youtube_url)