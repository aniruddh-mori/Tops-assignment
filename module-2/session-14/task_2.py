

def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    if user not in playlists:
        playlists[user] = {}

    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    song = {
        "title": song_title,
        "artist": artist
    }

    playlists[user][playlist_name].append(song)

playlists = {}

while True:
    user = input("Enter username: ")
    playlist_name = input("Enter playlist name: ")
    song_title = input("Enter song title: ")
    artist = input("Enter artist name: ")

    add_song_to_playlist(
        playlists, user, playlist_name, song_title, artist
    )

    print("Song added successfully!")

    choice = input("Add another song? (yes/no): ").lower()
    if choice != "yes":
        break

print(playlists)

