import random


class QueenIndividual:
    def __init__(self, genes=None):
        if genes:
            self.genes = genes
        else:
            self.genes = [random.randint(0, 7) for _ in range(8)]
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # calculate the number of conflicts
        conflicts = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if self.genes[i] == self.genes[j]:
                    conflicts += 1
                elif abs(i - j) == abs(self.genes[i] - self.genes[j]):
                    conflicts += 1
        # return the fitness score (lower is better)
        return conflicts

    def __lt__(self, other):
        # define the less than operator for sorting
        return self.fitness < other.fitness


class QueenGA:
    def __init__(self, population_size=50):
        self.population_size = population_size
        self.population = [QueenIndividual() for _ in range(population_size)]
        self.generation = 1

    def selection(self):
        # select the two best individuals using tournament selection
        tournament_size = 5
        tournament = [random.choice(self.population)
                      for _ in range(tournament_size)]
        tournament.sort()
        return tournament[0], tournament[1]

    def crossover(self, parent1, parent2):
        # perform single-point crossover
        crossover_point = random.randint(1, 6)
        child_genes = parent1.genes[:crossover_point] + \
            parent2.genes[crossover_point:]
        return QueenIndividual(child_genes)

    def mutation(self, individual):
        # perform random reset mutation
        mutation_rate = 0.1
        for i in range(8):
            if random.random() < mutation_rate:
                individual.genes[i] = random.randint(0, 7)

    def run(self, max_generations=100):
        while self.generation <= max_generations:
            # select two parents
            parent1, parent2 = self.selection()
            # create a new individual by crossover
            child = self.crossover(parent1, parent2)
            # mutate the child
            self.mutation(child)
            # calculate the fitness of the child
            child.fitness = child.calculate_fitness()
            # replace a random individual in the population with the child
            replace_index = random.randint(0, self.population_size - 1)
            self.population[replace_index] = child
            # print the best individual in this generation
            self.population.sort()
            print(
                f"Generation {self.generation}: Best Fitness = {self.population[0].fitness}, Genes = {self.population[0].genes}")
            # increase the generation counter
            self.generation += 1


if __name__ == '__main__':
    # create a GeneticSolver instance
    solver = GeneticSolver(population_size=100, mutation_rate=0.1)

    # solve the problem for 100 iterations
    for i in range(100):
        best_individual = solver.evolve()
        print(f"Iteration {i+1}: Best individual = {best_individual}")

        # stop if a perfect solution is found
        if solver.fitness(best_individual) == 28:
            print("Found a perfect solution!")
            break
