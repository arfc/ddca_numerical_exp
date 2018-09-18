# Creating of plots for NO report 
import plot_figures

plot_figures.plot_demand_supply(1000,'exponential',10000,0,0,'Fresh_Fuel','A-Constant-1',True)
plot_figures.plot_demand_supply(1000, 'linear', 100, 0, 0, 'Power', 'A-Growth-1', True)
plot_figures.plot_demand_supply(1000,'exponential',10,0.1,0,'Power','A-Growth-2',True)
plot_figures.plot_demand_supply(10, 'stepwise', 10, 20, 5, 'Power', 'A-Growth-3', True)