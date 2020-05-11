import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)

        for f in files:
            song_details = f[:-5].split(' - ')
            # split(' - ') le '1 - Candy Everybody Wants' ko - lai remove garera list maa laidinxa for example
            # ['1', 'Candy Everybody Wants']
            print(song_details)
            print("-" * 40)
