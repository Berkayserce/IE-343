class tsp:
    @staticmethod
    def nearest_neighbor_tsp(cities):
        num_cities = len(cities)
        visited = [False] * num_cities
        tour = [cities[0]]
        visited[0] = True

        current_city = cities[0]

        while len(tour) < num_cities:
            nearest_city = None
            min_distance = float('inf')

            for i in range(num_cities):
                if not visited[i]:
                    distance = current_city.distance_to(cities[i])
                    if distance < min_distance:
                        nearest_city = cities[i]
                        min_distance = distance

            visited[cities.index(nearest_city)] = True
            tour.append(nearest_city)
            current_city = nearest_city

        return tour
