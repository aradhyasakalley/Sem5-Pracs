import random

def generate_individual(length):
    arr = []
    for _ in range(length):
        arr.append(random.choice([0, 1]))
    return arr

def calculate_fitness(individual, target):
    count = 0
    for i in range(len(target)):
        if individual[i] == target[i]:
            count += 1
    return count

def crossover(parent1, parent2):
    split_point = random.randint(0, len(parent1) - 1)
    child = parent1[:split_point] + parent2[split_point:]
    return child

def mutate(individual, mutation_rate):
    child = []
    for bit in individual:
        child.append(bit ^ (random.random() < mutation_rate))
    return child

def genetic_algorithm(target, population_size, mutation_rate, generations):
    individual_length = len(target)
    population = []
    for _ in range(population_size):
        individual = generate_individual(individual_length)
        population.append(individual)

    for generation in range(generations):
        population = sorted(
            population,
            key=lambda individual: calculate_fitness(individual, target),
            reverse=True,
        )
        best_individual = population[0]

        if calculate_fitness(best_individual, target) == individual_length:
            print(f"Target reached in generation {generation + 1}!")
            break

        new_population = [best_individual]

        while len(new_population) < population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    return population[0]

target_binary = [1, 0, 1, 0, 0, 0, 0, 1]
population_size = 100
mutation_rate = 0.01
generations = 1000

result = genetic_algorithm(target_binary, population_size, mutation_rate, generations)

print(f"Best individual of the evolved population: {result}")
