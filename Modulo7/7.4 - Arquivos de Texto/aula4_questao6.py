import csv

most_played_songs = []
yearly_top_song = {}

with open('spotify-2023.csv', encoding='latin-1') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) 

    for row in csvreader:
        try:
            track_name = row[0]
            artists_name = row[1]
            released_year = int(row[3])
            streams = int(row[8])
            
            if 2012 <= released_year <= 2022:
                if released_year in yearly_top_song:
                    if streams > yearly_top_song[released_year][2]: 
                        yearly_top_song[released_year] = [track_name, artists_name, streams]
                else:
                    yearly_top_song[released_year] = [track_name, artists_name, streams]
        except ValueError:
            continue

for year in sorted(yearly_top_song.keys()):
    most_played_songs.append(yearly_top_song[year])

for song in most_played_songs:
    print(song)
