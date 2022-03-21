# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:16:41 2022

@author: arund
"""

from mrjob.job import MRJob
from mrjob.step import MRStep

class MostPopular(MRJob):
        
    def mapper(self, _, lines):
        (userID, movieID, rating, timestamp) = lines.split('\t')
        yield movieID, int(rating)
    
    def reducer(self, key, values):
        yield None, (sum(values), key)
        
    def SecondReducer(self, key, values):
        yield max(values)
        
    def all_steps(self):
        return [MRStep
                (mapper = self.mapper,
                 reducer = self.reducer),
                MRStep(reducer = self.SecondReducer)]
    
if __name__ == '__main__':
    MostPopular.run()