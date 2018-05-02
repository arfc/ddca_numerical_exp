import matplotlib.pyplot as plt
import numpy as np
import os

dirname = os.path.dirname(__file__)

def generate_plot(test_name, x, y):
    plt.plot(x,y)
    plt.xlabel('Timestep')
    plt.ylabel('Demand [kg]')
    plt.title('Test %s Demand' %test_name)
    plt.axis([0, 15, min(y) - 1, max(y) + 1])
    plt.savefig('./docs/do/images/%s' %test_name)


x = np.arange(0, 16, step=1)
y = np.zeros(16)
y = y + 1
generate_plot('A_dep_1', x, y)