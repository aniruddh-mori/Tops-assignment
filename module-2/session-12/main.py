
from musicplayer.player import play_song
from foodorder import get_menu, place_order
from shoppingcart import add_to_cart
from instahelpers import format_likes
from ticketbooking import search_event, book_ticket

# Task-1
play_song()

# Task-2
print(get_menu())
place_order("Pizza")

# Task-3
cart = []
add_to_cart(cart, "Shoes")

print(cart)

# Task-4

print(format_likes(1200))
print(format_likes(1500000))
print(format_likes(850))
print(format_likes(25000))

# Task-5

search_event()
book_ticket()
