import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import csv2d


csv2d_0 = csv2d.create((12, 10), 0)

print(csv2d.string(csv2d_0))
print(f"{csv2d.shape(csv2d_0)=:}")
print(f"{csv2d.length(csv2d_0)=:}")

print(f"{csv2d.index_in(csv2d_0, csv2d.length(csv2d_0))=:}")
print(f"{csv2d.index_in(csv2d_0, csv2d.length(csv2d_0) - 1)=:}")
print(f"{csv2d.coord_in(csv2d_0, (csv2d.shape(csv2d_0)[0], 0))=:}")
print(f"{csv2d.coord_in(csv2d_0, (csv2d.shape(csv2d_0)[0] - 1, 0))=:}")
print(f"{csv2d.coord_in(csv2d_0, (0, csv2d.shape(csv2d_0)[1]))=:}")
print(f"{csv2d.coord_in(csv2d_0, (0, csv2d.shape(csv2d_0)[1] - 1))=:}")

csv2d.set_index(csv2d_0, csv2d.length(csv2d_0) - 1, 1)
print(f"{csv2d.get_item(csv2d_0, csv2d.length(csv2d_0) - 1)=:}")

csv2d.save(csv2d_0, "csv2d_0.csv")

csv2d_1 = csv2d.load("csv2d_0.csv")

print(csv2d.string(csv2d_1))

for i, e in enumerate(csv2d.flatten(csv2d_0)):
    print(f"{i} {e}")
