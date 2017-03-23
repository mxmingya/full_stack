
import media
import fresh_tomatoes

avatar = media.Movie("Avatar", "A marain traveling at Alien planet", "http://cdn2-www.comingsoon.net/assets/uploads/gallery/batman-v-superman-dawn-of-justice-1400694960/batmanvsupermanposter.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
batman = media.Movie("BatmanvsSuperman", "A Marvel hero movie", "https://s-media-cache-ak0.pinimg.com/originals/f7/bc/7b/f7bc7b19e7f8555ba0f36aa3f2bc5dcd.jpg", "https://www.youtube.com/watch?v=0WWzgGyAH6Y")
darkknight = media.Movie("Dark Knight", "Batman movieII", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY&t=2s")
# print avatar.storyline
# print batman.storyline
#batman.show_trailer()
movies = [avatar, batman, darkknight]
fresh_tomatoes.open_movies_page(movies)