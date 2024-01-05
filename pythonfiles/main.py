from csv_parser import CSVParser
from Knapsack import knapsack
from Tsp import tsp


def main():
    songs = CSVParser.parse_songs("adele_songs_data.csv")
    cities = CSVParser.parse_cities("begum_berkay_cities.csv")

    tour = tsp.nearest_neighbor_tsp(cities)

    for city in tour:
        max_duration = city.concert_duration
        selected_songs = knapsack.greedy_knapsack(songs, int(max_duration))
        print(f"City: {city.name}")
        for song in selected_songs:
            print(f"- {song.name}, Popularity: {song.popularity}, Duration: {song.duration}")
        print("\n")

if __name__ == "__main__":
    main()
