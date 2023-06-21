import random
import eightQueens as EightQueens


class EightQueensGeneticAlgorithm:
    def __init__(self, population_size=100, mutation_probability=0.1):
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.population = []
        self.eq = EightQueens.EightQueens()

    def solve(self):
        self.initialize_population()
        best_individual = None
        count = 0
        while (best_individual is None or best_individual["fitness"] > 0) and count < 100:
            count += 1
            new_population = []

            for _ in range(self.population_size):
                x = self.random_selection()
                y = self.random_selection()
                child = self.reproduce(x, y)

                if random.random() < self.mutation_probability:
                    child = self.mutate(child)

                new_population.append(child)

            self.population = new_population
            best_individual = min(self.population, key=lambda x: x["fitness"])
            print("Zustand:", best_individual["state"])
            print("Fitness:", best_individual["fitness"])
            print("Visuelle Darstellung:")
            print(self.eq.visualize_state(best_individual["state"]))
            print("###############")

        return best_individual

    def initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            state = random.sample(range(8), 8)
            fitness = self.calculate_fitness(state)
            self.population.append({"state": state, "fitness": fitness})

    def random_selection(self):
        return random.choice(self.population)["state"]

    def reproduce(self, x, y):
        n = len(x)
        c = random.randint(1, n)
        child_state = x[:c] + y[c:]
        child_fitness = self.calculate_fitness(child_state)
        return {"state": child_state, "fitness": child_fitness}

    def mutate(self, individual):
        state = individual["state"]
        mutated_state = state[:]
        index = random.randint(0, 7)
        new_value = random.randint(0, 7)
        mutated_state[index] = new_value
        fitness = self.calculate_fitness(mutated_state)
        return {"state": mutated_state, "fitness": fitness}

    def calculate_fitness(self, state):
        return self.eq.cost_function(state)


# Beispielanwendung
genetic_algorithm = EightQueensGeneticAlgorithm()
solution = genetic_algorithm.solve()
if (solution["fitness"] != 0):
    print("Lösung nach 100 Durchläufen:")
else:
    print("Beste Lösung:")
print("Zustand:", solution["state"])
print("Fitness:", solution["fitness"])
print("Visuelle Darstellung:")
print(genetic_algorithm.eq.visualize_state(solution["state"]))
