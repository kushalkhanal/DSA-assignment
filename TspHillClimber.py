import numpy as np
import random

class TspHillClimber:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.distances = np.zeros((num_cities, num_cities))
        self.visited = np.zeros((num_cities, num_cities), dtype=bool)
        self.fitness = 0.0

    def set_distances(self, distances):
        self.distances = distances

    def solve(self):
        # Initialize solution with random order
        order = list(range(self.num_cities))
        random.shuffle(order)

        # Calculate initial fitness value
        self.fitness = self.calculate_fitness(order)

        # Hill climbing algorithm
        while True:
            new_order = self.get_neighbor(order)
            new_fitness = self.calculate_fitness(new_order)

            if new_fitness < self.fitness:  # Improvement found (minimization)
                order = new_order
                self.fitness = new_fitness
            else:  # No improvement, stop
                break

        print("Optimal tour:", order)
        print("Total distance:", self.fitness)

    def get_neighbor(self, order):
        # Randomly swap two cities in the order
        i, j = random.sample(range(self.num_cities), 2)

        new_order = order[:]
        new_order[i], new_order[j] = new_order[j], new_order[i]

        return new_order

    def calculate_fitness(self, order):
        total_distance = 0.0

        for i in range(self.num_cities - 1):
            total_distance += self.distances[order[i]][order[i + 1]]

        # Add distance from last city back to the first city
        total_distance += self.distances[order[-1]][order[0]]

        return total_distance

# Example usage
if __name__ == "__main__":
    # Example TSP instance
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 25, 18],
        [15, 25, 0, 22],
        [20, 18, 22, 0]
    ])

    tsp = TspHillClimber(4)
    tsp.set_distances(distances)
    tsp.solve()
