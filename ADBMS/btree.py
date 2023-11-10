import time
from BTrees.OOBTree import OOBTree

btree = OOBTree()
data = range(10000)

start_time = time.time()
for i in data:
    btree[i] = i
end_time = time.time()
print(f"time taken to insert data into B Tree: {end_time - start_time} seconds")

start_time = time.time()
for i in data:
    _=btree.get(i)
end_time = time.time()
print(f"Time taken to search data in B Tree: {end_time - start_time} seconds")