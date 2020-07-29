# Monte-Carlo-Sim

<img width="968" alt="image" src="https://user-images.githubusercontent.com/16807446/88862501-75520880-d1ce-11ea-993b-917cbdb767c6.png">

A Monte Carlo simulation script that projects investment outcomes using ONLY the 1) average and 2) standard deviation of the historical performance of said investment. The goal is to observe the various outcomes for a financial instrument with known historical metrics (mean and standard deviation). 

*Note: ***EXTREMELY IMPORTANT - Past performance is no guarantee of future results.***  And this is a very simplified model. This is mainly a simulation to highlight variance and how it could alter investment results even over a period that one deems as a significant sample size.  This is not financial advice and should be taken more from a theoretical point of view. 

The user enters:
- Mean and standard deviation of historical returns of said investment. 
- Duration that user wants projection.  (Should be in the same units as above)
- Number of simulations (the more sims, the more accurate the distribution plot). 

Returns:
- Line graph of simulations *Still in the works*
- A distribution plot of final balance over projected period of time, saved as 'distplot.png'.

Assumptions:
- Assumes normal distribution when sampling an instance of a % return. 
