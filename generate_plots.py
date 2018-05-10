import matplotlib.pyplot as plt
import numpy as np
import os

dirname = os.path.dirname(__file__)

def generate_plot(test_name, x, y):
    plt.plot(x,y)
    plt.xlabel('Timestep')
    plt.ylabel('Fuel Demand [kg]')
    plt.title('Test %s Demand' %test_name)
    plt.axis([0, 15, min(y) - 1, max(y) + 1])
    fn = os.path.join(os.path.dirname(__file__),
                      './docs/do/images/%s' %test_name)
    plt.savefig(fn)

test_name = 'A-dep-1'
x = np.arange(0, 16, step=1)
y = np.zeros(16)
y = y + 1
plt.plot(x,y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Fuel Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'A-dep-2'
x = np.arange(0, 16, step=1)
y = np.zeros(16)
y = y + 2
plt.plot(x,y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Fuel Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'A-dep-3'
x = np.arange(0, 16, step=1)
y = 0.1 * x
plt.plot(x,y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Power Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'A-dec-1'
x = np.arange(0, 16, step=1)
y = 2 - 0.1 * x
plt.plot(x,y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Power Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.grid()
plt.close()

test_name = 'A-mix-1'
x = np.arange(0, 16, step=1)
y = np.zeros(16)
y[0] = 1
y[1] = 1
y[2] = 1
plt.step(x,y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Fuel Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'A-mix-2'
x = np.arange(0, 16, step=1)
y = 0.5 * x
y[7:] = 3 - 0.2 * (x[7:]-6)
plt.plot(x,y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Fuel Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'B-dep-1'
x = np.arange(0, 16, step=1)
y = np.zeros(16)
y = y + 1
plt.plot(x,y)
plt.xlabel('Timestep')
plt.ylabel('Power Demand [kg]')
plt.title('Test %s Power Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'B-dep-2'
x = np.arange(0, 16, step=1)
y = 0.1 * x
plt.plot(x,y)
plt.xlabel('Timestep')
plt.ylabel('Power Demand [kg]')
plt.title('Test %s Power Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'B-dep-3'
x = np.arange(0, 16, step=1)
y = 2- 0.1 * x
plt.plot(x,y)
plt.xlabel('Timestep')
plt.ylabel('Power Demand [kg]')
plt.title('Test %s Power Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'B-mix-1'
x = np.arange(0, 16, step=1)
y = 0.5 * x
y[7:] = 3 - 0.2 * (x[7:]-6)
plt.plot(x,y)
plt.xlabel('Timestep')
plt.ylabel('Power Demand [kg]')
plt.title('Test %s Power Demand' %test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' %test_name )
plt.grid()
plt.savefig(fn)
plt.close()

