import random
import numpy as np
import matplotlib.pyplot as plt


duration_of_job = []
deadline_of_job = []
fitness_values = []
number_of_jobs = 0
delay = []

class Particle:
    def __init__(self, dimension):
        self.position = np.random.rand(dimension)
        self.velocity = np.random.rand(dimension)
        self.best_position = self.position
        self.fitness = objective_function(self.position)  # Update this line

def read_file():
    global duration_of_job, deadline_of_job, number_of_jobs
    working_list = []
    even_count = 0
    with open("jobshop_schedule.txt") as file:
        for line in file:
            working_list += list(map(int, line.split()))
    print("Job Schedule List: " + str(working_list))
    for x in working_list:
        if even_count % 2 == 0:
            duration_of_job.append(working_list[even_count])
        else:
            deadline_of_job.append(working_list[even_count])
        even_count += 1
    number_of_jobs = len(duration_of_job)
    print("Duration of Job: " + str(duration_of_job))
    print("Deadline of Job: " + str(deadline_of_job))
    print("Numjobs of Job:  " + str(number_of_jobs))
    
def objective_function(given=[]):
    global delay, duration_of_job, deadline_of_job, number_of_jobs
    total_time_taken = 0
    delay_made = 0
    delay = []
    for x in range(number_of_jobs):
        total_time_taken += duration_of_job[given[x] - 1]
        delay_made = total_time_taken - deadline_of_job[given[x] - 1]
        if delay_made < 0:
            delay_made = 0
        delay.append(delay_made)
    
    sum_delay = sum(delay)
    
    if sum_delay > 0:
        return 1 + (1 / sum_delay)
    else:
        return 1

def PSO(num_particles, num_dimensions, max_iterations, inertia_weight, cognitive_coeff, social_coeff):
    global fitness_values  # Add this line to make fitness_values accessible

    particles = [Particle(num_dimensions) for _ in range(num_particles)]
    global_best_position = min(particles, key=lambda p: p.fitness).position

    for iteration in range(max_iterations):
        for particle in particles:
            # Update velocity
            inertia_term = inertia_weight * particle.velocity
            cognitive_term = cognitive_coeff * random.random() * (particle.best_position - particle.position)
            social_term = social_coeff * random.random() * (global_best_position - particle.position)
            particle.velocity = inertia_term + cognitive_term + social_term

            # Update position
            particle.position = particle.position + particle.velocity

            # Update personal best
            if objective_function(particle.position) < objective_function(particle.best_position):
                particle.best_position = particle.position

        # Update global best
        global_best_position = min(particles, key=lambda p: p.fitness).position

        # Print the best fitness value at each iteration
        best_fitness = objective_function(global_best_position)
        print(f"Iteration {iteration + 1}: Best Fitness - {best_fitness}")

        # Append the fitness value to the list
        fitness_values.append(best_fitness)

    return global_best_position


if __name__ == "__main__":
    # PSO parameters
    num_particles = 20
    num_dimensions = 5
    max_iterations = 50
    inertia_weight = 0.5
    cognitive_coeff = 1.5
    social_coeff = 1.5

    # Run PSO
    best_solution = PSO(num_particles, num_dimensions, max_iterations, inertia_weight, cognitive_coeff, social_coeff)

    # Print the final best solution and its fitness value
    print("/nFinal Best Solution:", best_solution)
    print("Final Best Fitness Value:", objective_function(best_solution))
    plt.plot(range(1, max_iterations + 1), fitness_values)
    plt.xlabel('Iteration')
    plt.ylabel('Fitness Value')
    plt.title('Fitness Value Progression')
    plt.show()
