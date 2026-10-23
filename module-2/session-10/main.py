
from playlist import add_song
from playlist import remove_song
from playlist import display_playlist

# Task - 2
songs = ('Kesariya', 'Shape of You', 'Believer')
playlist = []
for song in songs:
    add_song(song,playlist)

print("Final Playlist : ",playlist)
print("Updated List of song : ",remove_song('Shape of You',playlist))
(display_playlist(playlist))