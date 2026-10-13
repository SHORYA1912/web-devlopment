from numpy import asarray
from numpy import arange
from numpy.random import rand
from matplotlib import pyplot as plt

def objective(x):
    return x**2.0

def derivative(x):
    return 2.0 * x

def gradient_descent(objective, derivative, bounds, n_iter, step_size):
    solutions , scores= list(),list()
    solution = bounds[0] + rand() * (bounds[1] - bounds[0])
    for i in range (n_iter):
        gradient = derivative(solution)
        solution = solution - step_size * derivative(solution)
        solution_eval = objective(solution)
        solutions.append(solution)
        scores.append(solution_eval)
        print('>%d f(%f) = %f' % (i, solution, solution_eval))
    return solutions, scores

bounds = asarray([-1.0, 1.0])
n_iter = 30
step_size = 0.1

solutions, scores = gradient_descent(objective, derivative, bounds, n_iter, step_size)

inputs = arange(bounds[0], bounds[1]+0.1,0.1)
results = objective(inputs)
plt.plot(inputs, results)

plt.plot(solutions, scores, '-', color='red', label='Gradient Descent')
plt.show()
