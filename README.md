# Calculating the median and percentiles

You should have seen that mean computed from multiple exponential random converges on the expectation as the sample size increases as you have seen for all the other types of random variables.  In this exercise we are going to revise another computer programming approach that we have covered elsewhere in this course; namely, the process via which we compute the median and various percentiles for a data set.  With that in mind to complete the programming task for this week you will need to:

1. Write a function called `exponential` that takes a parameter called `lam` and that returns an exponential random variable from a distribution with parameter `lam`.
2. Write a loop that calls your exponential function 151 times and that stores the 151 values that this function returns in a list called `samples`.
3. Having generated your list of samples I then want you to compute the `median`, and the 10th, 25th, 75th and 90th percentiles for the distribution.  These values should be stored in the variables called `median`, `percentile10`, `percentile25`, `percentile75` and `percentile90`.
 
