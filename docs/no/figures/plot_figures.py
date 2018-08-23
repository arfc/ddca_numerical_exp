from matplotlib import pyplot as plt
import numpy as np

duration = 1000
gradient = 0 
intercept = 1000

x_vals = np.linspace(0, duration, duration+1)
y_vals = [(x * gradient + intercept) for x in x_vals]
error_vals = [y * 0.1 for y in y_vals]
print(error_vals)

def plot_demand_supply(duration,gradient,intercept,commodity,test_name): 
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
    y_vals = [(x * gradient + intercept) for x in x_vals]
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
    ax.set_xlim(0,1000)
    ax.set_ylim(0,12000)
    ax.set_xlabel('Timestep (month)',fontsize=13)
    ax.set_ylabel('%s Amount (kg)' % commodity,fontsize=13)
    ax.set_title('%s : %s (Demand-driving Commodity) demand and acceptable range for its supply' %(test_name,commodity) ,fontsize=14)
    plt.savefig('test.png', bbox_inches="tight")

    return 

plot_demand_supply(1000,0,10000,'Fresh Fuel','Test [A]-[Constant]-[1]')
