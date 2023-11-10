import time
from bintrees import FastRBTree

bplustree = FastRBTree()
data = range(10000)

start_time = time.time()
for i in data:
    bplustree[i] = (i.to_bytes(4,'big'))
end_time = time.time()
print(f"Time taken to insert data into B plus Tree: {end_time - start_time} seconds")

start_time = time.time()
for i in data:
    _=bplustree.get(i)
end_time = time.time()
print(f"Time taken to search data in B plus Tree: {end_time - start_time} seconds")