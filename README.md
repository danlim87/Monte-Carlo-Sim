# Monte-Carlo-Sim

A Monte Carlo simulation script that projects. The goal is to use historical investments with known track record

Prerequisite: Knowing your instrument of choice's historical return and its standard deviation. 

*Note: ***EXTREMELY IMPORTANT - Past performance is no guarantee of future results.***  This is mainly a simulation to highlight how variance could alter investment results even over a period that one deems as a significant sample size.  This is not financial advice and should be taken more from a theoretical point of view. 

The user enters:
- Mean and standard deviation of historical returns of said investment. 
- Duration that user wants projection.  (Should be in the same units as above)
- Number of simulations (the more sims, the more accurate the distribution plot). 
- Save png y/n

Returns:
- Line graph of simulations
- A distribution plot of final balance over projected period of time. 

Assumptions:
- Assumes normal distribution to pick return for set period of time. 
