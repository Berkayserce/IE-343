from City import City
from Song import Song
import csv
class CSVParser:
    @staticmethod
    def parse_cities(file_name):
        cities = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                city = City(row[0].strip(), float(row[2].strip()), float(row[3].strip()), float(row[4].strip()))
                cities.append(city)
        return cities

    @staticmethod
    
    def parse_songs(file_name):
        songs = []
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                try:
                    if len(row) == 3:
                        song_name = row[0].strip()
                        popularity = float(row[1].strip())
                        duration = float(row[2].strip())
                        songs.append(Song(song_name, popularity, duration))
                    else:
                        pass
                   
                except ValueError as e:
                    print(f"Error processing row {row}: {e}")
        return songs

