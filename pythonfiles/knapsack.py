class Knapsack:
    @staticmethod
    def knapsack(songs, max_duration):
        songs.sort(key=lambda x: x.popularity / x.duration, reverse=True)

        selected_songs = []
        total_duration = 0

        for song in songs:
            if total_duration + song.duration <= max_duration:
                selected_songs.append(song)
                total_duration += song.duration

        return selected_songs

