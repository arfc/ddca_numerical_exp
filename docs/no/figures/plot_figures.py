"""
Plots for Numerical Experiments for Verifying Demand Driven Deployment Algorithms
Non-Optimizing Algorithm Report 
"""

from matplotlib import pyplot as plt
import numpy as np

def demand_curve_type(x_vals,type,input1,input2): 

    if type == 'exponential':
        initial_demand = input1
        growth_rate = input2
        y_vals = [(initial_demand*(1+growth_rate)**(x/12)) for x in x_vals]

    elif type =="linear":
        gradient = input1
        intercept = input2
        y_vals = [(gradient*x+intercept) for x in x_vals]

    return y_vals


def plot_demand_supply(duration,demand_curve,input1,input2,commodity,test_name): 
    """ Plots demand and acceptable supply range amount for a commodity 
    
    Parameters 
    ----------
    duration: int of number of timesteps in scenario 
    gradient: int of gradient of demand curve (m of y = mx+c)
    intercept: int of intercept of demand curve (c of y = mx+c)
    
    Returns 
    -------
    returns a plot of demand and acceptable supply range amount for a specified commodity 
    
    """
    x_vals = np.linspace(0, duration, duration+1)
    y_vals = demand_curve_type(x_vals,demand_curve,input1,input2)
    error_vals = [y * 0.1 for y in y_vals]
    positive_y = [x + y for x,y in zip(y_vals,error_vals)]
    negative_y = [x - y for x,y in zip(y_vals,error_vals)]

    fig, ax = plt.subplots(figsize=(15,7))
    ax.plot(x_vals, y_vals, 'k-',label='Demand')
    ax.fill_between(x_vals, positive_y, negative_y,label='Acceptable Supply Range')
    ax.grid()
    box = ax.get_position()
    ax.set_position([box.x0,box.y0 + box.height,box.width,box.height*1])
    handles,labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, fontsize=13,loc='upper center',bbox_to_anchor=(0.85,1.2),fancybox=True)
    ax.set_xlim(0,duration)
    ax.set_ylim(0,(y_vals[-1]*1.2))
    ax.set_xlabel('Timestep (month)',fontsize=13)
    ax.set_ylabel('%s Amount (kg)' % commodity,fontsize=13)
    ax.set_title('Test %s : %s (Demand-driving Commodity) demand and acceptable range for its supply' %(test_name,commodity) ,fontsize=14)
    plt.savefig('demand_supply_%s' %test_name, bbox_inches="tight")

    return 

plot_demand_supply(1000,'exponential',10000,0,'Fresh Fuel','A-Constant-1')
plot_demand_supply(10,'linear',1000,0,'Fresh Fuel','A-Growth-1')
