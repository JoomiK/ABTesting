"""Functions for hypothesis testing using bootstrap resampling"""

import numpy as np
from thinkstats2 import HypothesisTest

"""Code from thinkstats found here: https://github.com/AllenDowney/ThinkStats2"""


class DiffMeansPermute(HypothesisTest):
    """
    Model the null hypothesis, which says that the distributions
    for the two groups are the same.
    data: pair of sequences (one for each group)
    """
    def TestStatistic(self, data):
        """
        Calculate the test statistic, the absolute difference in means
        """
        group1, group2 = data
        test_stat = abs(np.mean(group1) - np.mean(group2))
        return test_stat

    def MakeModel(self):
        """
        Record the sizes of the groups, n and m, 
        and combine into one Numpy array, self.pool
        """
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        
        # make group1 and group2 into a single array
        self.pool = np.concatenate((group1, group2))

    def RunModel(self):
        """
        Simulate the null hypothesis- shuffle the pooled values 
        and split into 2 groups with sizes n and m
        """
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data
    
    
def Resample(x):
    """
    Get a bootstrap sample
    """
    return np.random.choice(x, len(x), replace=True)


def FalseNegRate(data, num_runs=100):
    """
    Calculate the false negative rate: the chance that the hypothesis 
    test will fail when the effect is real.
    """
    group1, group2 = data
    count = 0

    for i in range(num_runs):
        sample1 = Resample(group1)
        sample2 = Resample(group2)

        ht = DiffMeansPermute((sample1, sample2))
        pvalue = ht.PValue(iters=101)
        
        if pvalue > 0.05:
            count += 1

    return count / num_runs
    
    