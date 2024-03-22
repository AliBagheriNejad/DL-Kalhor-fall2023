import numpy as np

# The  W matrix
W = np.array([[1, -1, 1, 1, 1, 1, 1],
              [1, 1, 1, -1, -1, -1, -1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, -1, 1, 1, 1, 1]])/7
             
theta = np.array([6/7,3/7,1,6/7])

def w_num(n):
    
    y = np.dot(W,n.T)
    ans = theta-y
    ans = np.abs(ans)<0.0001
    return ans

