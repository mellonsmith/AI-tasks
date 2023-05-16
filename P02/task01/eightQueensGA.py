import random

from eightQueens import EightQueens


class EightQueensGA:
    def __init__(self, population_size=100, iterations=100):
        self.population_size = population_size
        self.iterations = iterations
        self.problem = EightQueens()
        self.population = self.generate_initial_population()

    def generate_random_individual(self):
        state = list(range(8))
        random.shuffle(state)
        return state

    def generate_initial_population(self):
        return [self.generate_random_individual() for _ in range(self.population_size)]

    def fitness_function(self, individual):
        return self.problem.cost_function(individual)

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, 6)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutation(self, individual):
        mutation_point1 = random.randint(0, 7)
        mutation_point2 = random.randint(0, 7)
        individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]
        return individual

    def solve_eight_queens_ga(self):
        for iteration in range(self.iterations):
            fitness_scores = [self.fitness_function(
                individual) for individual in self.population]
            best_individual_index = fitness_scores.index(min(fitness_scores))
            best_individual = self.population[best_individual_index]
            print("Iteration:", iteration + 1)
            print("Best Individual:", best_individual)
            print("Fitness Score:", self.fitness_function(best_individual))
            if self.fitness_function(best_individual) == 0:
                break

            new_population = [best_individual]
            while len(new_population) < self.population_size:
                parent1 = random.choice(self.population)
                parent2 = random.choice(self.population)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutation(child1)
                child2 = self.mutation(child2)
                new_population.extend([child1, child2])

            self.population = new_population


if __name__ == '__main__':
    ga = EightQueensGA()
    ga.solve_eight_queens_ga()
