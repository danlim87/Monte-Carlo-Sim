#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:39:39 2020

@author: daniellim
"""
#Next steps:
    #Generating a report
    #Use plotly's online function and create a more interactive way to view graph


import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
import math

import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser'

import seaborn as sns


def balance_updater(balance, pct):
    '''returns final balance assuming pct is an array that tracks changes in percentage terms'''
    balance_list = []
    for i in range(len(pct)):
        balance = (balance + balance * pct[i] / 100).round(2)
        balance_list.append(balance)
    return balance_list

def df_creator(avg, std, balance = 100000, num_sim = 500, num_length = 50):
    
    """
    Returns dataframe ran by monte-carlo.  Assumes normal distribution when selecting samples. 
    
    Paramters
    ----------
    - balance(int): Starting balance of investment
    - avg(float): Known historical mean yearly/monthly/weekly historical return (denoted in %)
    - std(float): Known historical standard deviation (denoted in %)
    - num_sim(int): Number of simulations to be run
    - num_length(int): Desired length of projection duration.  Keep in mind this unit should be the same as the previous 'avg' (monthly = monthly)
    
    Returns: 
    Pandas Dataframe of num_length rows and num_sim columns. 
    """
    
    df = pd.DataFrame()
    df.index += 1 #Accounts for Month 1, 2, 3 instead of 0, 1, 2, etc.
    for i in range(1, num_sim+1): 
        pct = np.random.normal(avg, std, num_length)
        sim_list = balance_updater(balance, pct)
        df['Simulation_' + str(i)] = sim_list
    return df

def log_final_balance_creator(df):
    '''Creates log version of final balance results. 
    Input: pd.DataFrame
    Returns: pd.Series
    '''
    return df.iloc[-1].apply(lambda x: math.log(x))

def log_ci_retriever(log_df, CI):
    '''
    Retrieve upper and lower bounds of desired confidence interval. CI denotes how many standard deviations away from mean.
    
    Parameters
    --------------------------
    - df (Series): Assumes pd.Series
    - CI (int): Desired std deviation.  Either 1, 2, 3 (corresponds to 68, 95, 99.7)
    '''
    log_mean = log_df.mean()
    log_std = log_df.std()
    low_bound = log_mean - log_std * CI
    high_bound = log_mean + log_std * CI
    converted_low_bound = math.exp(low_bound)
    converted_mean = math.exp(log_mean)
    converted_high_bound = math.exp(high_bound)
    return converted_low_bound, converted_mean, converted_high_bound, log_std

def ci_plotter(df, unit, m, log_std):
    '''
    Uses plotly to plot distribution plot with appropriate confidence intervals (+/- 1, 2 std).  Input assumes Series.
    '''
    fig = px.histogram(df, nbins=50, title = "Final balance over a " + unit + str(df.name+1) + ' ' + ' period. N_sims = ' + str(len(df)))
    fig.update_layout(
        autosize=False,
        xaxis = dict(
            title_text = "Balance"),
        shapes = [
            dict(
                type = 'line',
                yref = 'paper', y0 = 0, y1 = 1,
                xref = 'x', x0=m, x1 = m,
                line = dict(
                color = 'Red', width = 4)
                ),
            dict(
                type = 'line',
                yref = 'paper', y0 = 0, y1 = 1,
                xref = 'x', x0=(m/math.exp(log_std)), x1 = (m/math.exp(log_std)),
                line = dict(
                color = 'Red', width = 4, dash = 'dash')
                ),
            dict(
                type = 'line',
                yref = 'paper', y0 = 0, y1 = 1,
                xref = 'x', x0=(m*math.exp(log_std)), x1 = (m*math.exp(log_std)),
                line = dict(
                color = 'Red', width = 4, dash = 'dash')),
            dict(
                type = 'line',
                yref = 'paper', y0 = 0, y1 = 1,
                xref = 'x', x0=(m/math.exp(2*log_std)), x1 = (m/math.exp(2*log_std)),
                line = dict(
                color = 'Red', width = 4, dash = 'dot')),
            dict(
                type = 'line',
                yref = 'paper', y0 = 0, y1 = 1,
                xref = 'x', x0=(m*math.exp(2*log_std)), x1 = (m*math.exp(2*log_std)),
                line = dict(
                color = 'Red', width = 4, dash = 'dot'))
        ])
    fig.show()



if __name__ == '__main__':
    unit_dict = {'y': 'year', 'm': 'month', 'd': 'day'}
    unit = unit_dict[input('Will you be using y/m/w for this analysis: ')]
    balance = float(input('Enter starting balance: '))
    avg = float(input('Enter known mean ' + unit + 'ly historical return (denoted in %): '))
    std = float(input('Enter known standard deviation (denoted in %): '))
    num_sim = int(input('Enter number of simulations you would like to run: '))
    num_length = int(input('Enter length of desired projection duration in ' + unit + 's: '))
    CI = int(input('Enter desired confidence interval (1 for 68%, 2 for 95%, 3 for 99.7%): '))


    df = pd.DataFrame()
    df.index += 1

    df = df_creator(avg, std, balance, num_sim, num_length)
    
    log_df = log_final_balance_creator(df)
    low_bound, mean, high_bound, log_std = log_ci_retriever(log_df, CI)
    ci_plotter(df.iloc[-1], unit, mean, log_std)
    ci_dict = {1: 68, 2: 95, 3: 99.7}
    print(str(ci_dict[CI]) + '% confidence = between $' + str(low_bound) + ' and $' + str(high_bound) + ' with a mean of $' + str(mean))

