songs = "The Edge Band","Pokhara",2010,((1,"Mero Aashu"),(2,"Tashbir"),(3,"Nachhodnu Yo Saath"))

# print(songs)
band, city, founded, tracks = songs
print(band)
print(city)
print(founded)

# Aafule bujheko kura hai guyz
track1, track2, track3 = tracks

print(track1)
print(track2)
print(track3)

#Video ko concept
for song in tracks:
    track, name = song
    print("Track: {0}, Name: {1}".format(track,name))
