# Monte-Carlo-Sim

<img width="968" alt="image" src="https://user-images.githubusercontent.com/16807446/88862501-75520880-d1ce-11ea-993b-917cbdb767c6.png">

A Monte Carlo simulation script that projects investment outcomes using ONLY the 1) average and 2) standard deviation of the historical performance of said investment. The goal is to observe the various outcomes for a financial instrument with known historical metrics (mean and standard deviation). 

*Note: ***EXTREMELY IMPORTANT - Past performance is no guarantee of future results.***  And this is a very simplified model. This is mainly a simulation to highlight variance and how it could alter investment results even over a period that one deems as a significant sample size.  This is not financial advice and should be taken more from a theoretical point of view. 

This repository can be used in 1 of 2 ways:
1. Run monte_carlo.py.  It will ask user to input certain parameters (mean, standard deviation, etc.).  Then the script will run and 2 files named 'montecarlo.png' and 'distplot.png' will be saved to the forked repository for review.
2. For a more exploranatory analysis using jupyter notebook, one can simply import the module (ex. import monte_carlo as mc) and use the function "df_creator" to create a dataframe of time x simulations. 


Assumptions:
- Assumes normal distribution when sampling an instance of a % return. 
