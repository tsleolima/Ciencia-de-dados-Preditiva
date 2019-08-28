import numpy as np

import time

N = 100000

# Usando uma lista python e depois convertendo para numpy
def time_to_create_vector_py():
    start = time.time()
    
    l = []
    for i in range(N):
        l.append(i)
        
    l = np.array(l)
    return time.time() - start

# Usando um vetor numpy desde o inicio pq sou teimoso
def time_to_create_vector_np():
    start = time.time()
    
    l = np.array([])
    for i in range(N):
        l = np.append(l, i)
        
    l = np.array(l, dtype=int)
    return time.time() - start
    
    
print('Tempo utilizando lista: %.3f (s)' % time_to_create_vector_py())
print('Tempo utilizando numpy: %.3f (s)' % time_to_create_vector_np())
