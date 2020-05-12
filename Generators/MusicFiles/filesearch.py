import os
import fnmatch


def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
            subdir = os.path.join(path, artist)
            for albums_name, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(albums_name, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song


album_list = find_albums("music", "black*")  # It returns/yields all albums those belong to artist 'Aerosmith'
# song_list = find_songs(album_list)  # It returns/yields songs of all albums sequentially belonging to artist 'Aerosmith'

for s in album_list:
    print(s)
