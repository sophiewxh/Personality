from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import os

def example():
    #Load boston housing dataset as an example
    boston = load_boston()
    X = boston["data"]
    Y = boston["target"]
    print X 
    print Y 
    
    names = boston["feature_names"]
    rf = RandomForestRegressor()
    rf.fit(X, Y)
    print "Features sorted by their score:"
    print sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names), 
                 reverse=True)
def test():
    fp = os.path.join('result', 'feature', 'all_features_extra.csv')
    #data = np.genfromtxt(fp, delimiter=",", dtype=float, skip_header=1)
    data = np.genfromtxt(fp, delimiter=",", dtype=float, names=True)

    print data.dtype.names
    slice = data[['len_var_oncampus', 'end_time_var_oncampus']]
    print slice

    
    

#     x = data[:, 1:-1]
#     y = data[:,-1]
#     rf = RandomForestRegressor()
#     rf.fit(x, y)
#     print rf.feature_importances_

def tune_parameters():
    
if __name__ == '__main__':
    #example()
    test()

