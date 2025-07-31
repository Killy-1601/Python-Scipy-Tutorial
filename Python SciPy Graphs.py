"""working with graphs: we have a module name scipy.sparce.csgraph
#adjacency matrix: nxn matrix where n is the number of element in the graph.
# connected component:
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
data = np.array([[0,1,2],[1,0,0],[2,0,0]])
newdata = csr_matrix(data)
print(connected_components(newdata))


# Dijkstra method: for finding the shortest path in a graph from one element to another 
#it take 3 arg: return_predecessors, indices , limit
#here we will find the shortest path from element 1 to 2
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
data = np.array([[0,1,2],[1,0,0],[2,0,0]])
newdata = csr_matrix(data)
print(dijkstra(newdata, return_predecessors=True, indices=0))


#floyd warshall() method: it is for finding the shortest path between all the pairs of element
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
data = np.array([[0,1,2],[1,0,0],[2,0,0]])
newdata = csr_matrix(data)
print(floyd_warshall(newdata,return_predecessors=True))


# Bellman_ford() method: it is for finding the shortest path between all the pairs of element but this method can handle negative weight as well:
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
data = np.array([[0,1,2],[1,0,0],[2,0,0]])
newdata = csr_matrix(data)
print(bellman_ford(newdata, return_predecessors=True,indices=0))"""


# depth first order: it returns a depth first traversal from a node: it has 2 argu: the fraph, starting element
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix
data = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
newdata = csr_matrix(data)
print(depth_first_order(newdata,1))


# breadth_first_order() method: it returns the breath from a node:it has 2 argu: the fraph, starting element
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
data = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
newdata = csr_matrix(data)
print(breadth_first_order(newdata,1))



