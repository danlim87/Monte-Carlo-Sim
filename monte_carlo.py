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

import seaborn as sns


def balance_updater(balance, pct):
    '''returns final balance assuming pct is an array that tracks changes in percentage terms'''
    balance_list = []
    for i in range(len(pct)):
        balance = (balance + balance * pct[i] / 100).round(2)
        balance_list.append(balance)
    return balance_list

def df_creator(balance = 100000, avg, std, num_sim = 50, num_length = 50):
    
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

if __name__ == '__main__':
    balance = float(input('Enter starting balance: '))
    avg = float(input('Enter known mean yearly/monthly/weekly historical return (denoted in %): '))
    std = float(input('Enter known standard deviation (denoted in %): '))
    num_sim = int(input('Enter number of simulations you would like to run: '))
    num_length = int(input('Enter length of desired projection duration (same yearly/monthly/weekly as the mean): '))

    df = pd.DataFrame()
    df.index += 1

    df = df_creator(balance, avg, std, num_sim, num_length)
    fig = df.plot()
    fig.figure.savefig('montecarlo.png')
    fig2 = sns.distplot(df.iloc[-1], bins=100)
    fig2.figure.savefig('distplot.png')

                 

