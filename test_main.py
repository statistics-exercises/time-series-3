import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_percentiles(self) : 
        self.assertTrue( percentile10==np.percentiles(samples,10), "the 10th percentile is computed incorrectly" )
        self.assertTrue( percentile25==np.percentiles(samples,25), "the 25th percentile is computed incorrectly" )
        self.assertTrue( median==np.percentiles(samples,50), "the median is computed incorrectly"" )
        self.assertTrue( percentile75==np.percentiles(samples,75), "the 75th percentile is computed incorrectly" )
        self.assertTrue( percentile90==np.percentiles(samples,90), "the 90th percentile is computed incorrectly" )
        
   def test_exponential(self) : 
       for i in range(1,10) : 
           lam, mean=2*i, 0 
           for j in range(100) : mean = mean + exponential(lam)
           mean = mean / 100

           bar = np.sqrt(1/(lam*lam)/100)*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( mean - 1/lam )<bar, "your function appears to be generating exponential random variables incorrectly" )
    
