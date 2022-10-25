import numpy as np
from tabulate import tabulate
table = np.array([["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]])
x=tabulate(table,tablefmt="fancy_grid")
print(x)