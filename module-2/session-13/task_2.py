
new_playlist = []
playlists = [[210, 180, 240], [150, 200], [300, 120, 90]]
for playlist in playlists:
    for duration in playlist:
        if (duration>=200):
            new_playlist.append(duration)
print(new_playlist)
