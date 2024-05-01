# Job Shop Scheduling Problem (JSSP) Solver Using Particle Swarm Optimization (PSO)

## Project Overview

This project explores the application of Particle Swarm Optimization (PSO) to solve the Job Shop Scheduling Problem (JSSP). Our objective is to develop an efficient scheduling system that minimizes the overall delay of jobs while adhering to specific order constraints and deadlines.

## Problem Statement

The JSSP involves scheduling a set of jobs, each consisting of a sequence of tasks, which must be performed on predefined machines in a specific order. The challenge is to schedule these jobs in a way that minimizes the total completion time without violating the order of operations.

## Approach

We utilize PSO with a discrete model where each particle represents a potential solution to the scheduling problem. The adaptation involves:

- **Solution Representation**: Discrete representation of particles, where each particle is a sequence of job operations.
- **Objective Function**: Minimize the total delay, calculated as the time a job exceeds its deadline. The fitness function evaluates the effectiveness of the job sequences.
- **Algorithm Design**: Particles adjust their positions in the solution space based on their own experience and their neighbors' best solutions, striving to find an optimal scheduling sequence with minimal delay.

## Key Results

- **Effective Optimization**: Our PSO approach adapted for discrete optimization demonstrates superior performance in generating high-quality solutions quickly and efficiently.
- **Benchmarking**: Compared against traditional scheduling methods, our PSO implementation shows faster convergence to optimal solutions.
- **Flexibility**: The algorithm is robust across various test cases with different complexity levels, showing consistent improvements in scheduling efficiency.

## Conclusion

The PSO-based solver for JSSP significantly enhances the scheduling efficiency by optimizing job sequences to minimize total delays. This project not only demonstrates PSO's adaptability to discrete optimization problems like JSSP but also highlights its potential in complex industrial scheduling tasks.
