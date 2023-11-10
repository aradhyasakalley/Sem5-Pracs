import time
from bplustree import BPlusTree

# Initialize the B+ tree
tree = BPlusTree('D:/ab.db', order=32)

# Generate some data
data = range(1000000)

# Insert data into the B+ tree
start_time = time.time()
for i in data:
    tree[i] = i.to_bytes(4, 'big')
end_time = time.time()
print(f"Time taken to insert data into B+ Tree: {end_time - start_time} seconds")

# Search data in the B+ tree
start_time = time.time()
for i in data:
    _ = tree.get(i)
end_time = time.time()
print(f"Time taken to search data in B+ Tree: {end_time - start_time} seconds")
