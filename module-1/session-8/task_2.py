
def extract_artist(song_title):
    arr_idx = song_title.find("-")
    return song_title[arr_idx+1:].strip()
