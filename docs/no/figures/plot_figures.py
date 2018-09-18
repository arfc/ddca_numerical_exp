"""
Plots for Report:
Numerical Experiments for Verifying Demand Driven Deployment Algorithms
Non-Optimizing Algorithm
"""

from matplotlib import pyplot as plt
import numpy as np


def demand_curve_type(x_vals, type, input1, input2, input3):
    """ Y value calculation based on demand curve type and input values

    Parameters
    ----------
    x_vals: list of timestep values
    type: string of type of demand curve (i.e. linear, exponential, step-wise)
    input 1: exponential -- initial demand, linear -- gradient,
             stepwise -- y-value of first segment
    input 2: exponential -- growth rate, linear -- y intercept,
             stepwise -- y-value of second segment
    input 3: stepwise -- timestep it changes from first to second segment

    Returns
    -------
    returns a plot of demand and acceptable supply range amount for a
    specified commodity

    """

    if type == 'exponential':
        initial_demand = input1
        growth_rate = input2
        y_vals = [(initial_demand * (1 + growth_rate)**(x / 12))
                  for x in x_vals]

    elif type == "linear":
        gradient = input1
        intercept = input2
        y_vals = [(gradient * x + intercept) for x in x_vals]

    elif type == "stepwise":
        first_y = input1
        second_y = input2
        timestep_change = input3
        x_vals_1 = x_vals[:timestep_change + 1]
        x_vals_1 = list(x_vals_1)
        x_vals_2 = x_vals[timestep_change:]
        x_vals_2 = list(x_vals_2)
        x_vals = x_vals_1 + x_vals_2
        y_vals_1 = [first_y] * (timestep_change + 1)
        timesteps_2 = (x_vals[-1] - timestep_change + 1)
        timesteps_2 = int(timesteps_2)
        y_vals_2 = [second_y] * timesteps_2
        y_vals = y_vals_1 + y_vals_2

    return y_vals, x_vals


def plot_demand_supply(duration, demand_curve, input1,
                       input2, input3, commodity, test_name, demand_driving):
    """ Plots demand and acceptable supply range amount for a commodity

    Parameters
    ----------
    duration: int of number of timesteps in scenario
    demand_curve: string of type of demand curve (i.e. linear, exponential,
                  step-wise)
    input 1: int, depending on which demand_curve, see func demand_curve_type
    input 2: int, depending on which demand_curve, see func demand_curve_type
    input 3: int, depending on which demand_curve, see func demand_curve_type
    commodity: string of tracked commodity
    test_name: string of test name
    demand_driving: True/False boolean, True if the commodity is the
                    demand-driving commodity

    Returns
    -------
    returns a plot of demand and acceptable supply range amount for a specified
    commodity

    """
    x_vals = np.linspace(0, duration, duration + 1)
    y_vals, x_vals = demand_curve_type(
        x_vals, demand_curve, input1, input2, input3)
    error_vals = [y * 0.1 for y in y_vals]
    positive_y = [x + y for x, y in zip(y_vals, error_vals)]
    negative_y = [x - y for x, y in zip(y_vals, error_vals)]

    fig, ax = plt.subplots(figsize=(15, 7))
    ax.plot(x_vals, y_vals, 'k-', label='Demand')
    ax.fill_between(x_vals, positive_y, negative_y,
                    label='Acceptable Supply Range')
    ax.grid()
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height, box.width, box.height * 1])
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(
        handles,
        labels,
        fontsize=13,
        loc='upper center',
        bbox_to_anchor=(
            0.85,
            1.2),
        fancybox=True)
    ax.set_xlim(0, duration)
    ax.set_ylim(0, y_vals[-1] * 1.2)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    ax.set_xlabel('Timestep (month)', fontsize=14)
    ax.set_ylabel('%s Amount (kg)' % commodity, fontsize=14)
    if demand_driving:
        ax.set_title(
            'Test %s : %s (Demand-driving Commodity) demand and acceptable range for its supply' %
            (test_name, commodity), fontsize=16)
    else:
        ax.set_title(
            'Test %s : %s demand and acceptable range for its supply' %
            (test_name, commodity), fontsize=16)
    plt.savefig(
        '%s_%s_demand_supply' %
        (commodity, test_name), bbox_inches="tight")

    return fig
