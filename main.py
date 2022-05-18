from math import e, exp, pow
from numpy import arange
import matplotlib.pyplot as plt


def y(x):
    return 2.1 * x ** 2 - 2.1 * x + pow(e, -x) + pow(e, -x) + pow(e, x) - 2


def q(x):
    return 2 * alpha + 2 + alpha * x * (1 - x)


def preciese_solution(n):
    h = (b - a) / n
    x_values = []
    for i in arange(a, b, h):
        x_values.append(i)
    y_values = []
    for x in x_values:
        y_values.append(y(x))
    plt.title(f'Exact solution, n={n}')
    plt.plot(x_values, y_values)
    plt.show()


def forward_sweep(h, n):
    x_values = []
    for i in arange(a, b + h, h):
        x_values.append(i)
    lambdas = [0]

    mu_i_plus_one = [y_from_0]
    for k in range(1, n + 1):
        a_i = 2 + pow(h, 2)
        b_i = pow(h, 2) * q(x_values[k - 1])
        lambda_i = lambdas[k - 1]
        mu_i = mu_i_plus_one[k - 1]
        lambdas.append(1 / (a_i - lambda_i))
        mu_value = (mu_i - b_i) / (a_i - lambda_i)
        mu_i_plus_one.append(mu_value)
    y_values = backward_sweep(lambdas, mu_i_plus_one, n)
    return x_values, y_values


def backward_sweep(lambdas, mus, n):
    y_values = [0] * (n + 1)
    y_values[len(y_values) - 1] = y_from_1
    for k in range(n - 1, 0, -1):
        y_values[k] = lambdas[k + 1] * y_values[k + 1] + mus[k + 1]
    return y_values


def sweep(h, n):
    x_values, y_values = forward_sweep(h, n)
    plt.title(f'Sweep, n = {n}')
    plt.plot(x_values, y_values)
    plt.show()


segment = [0, 1]
a = 0
b = 1
alpha = 2 + 0.1 * 1
y_from_0 = 0
y_from_1 = e + 1 / e - 2
N_1 = 10
N_2 = 20
h_1 = 1 / N_1
h_2 = 1 / N_2

if __name__ == '__main__':
    preciese_solution(100)
    sweep(h_1, N_1)
    sweep(h_2, N_2)
