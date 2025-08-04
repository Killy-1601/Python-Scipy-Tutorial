# working with spatial data: it refers to data that is represented in a geometrio space
# triangulation: one method to generate these triangulation through the point is delaunay() triangulation

"""#gere now we will create a triangulation from some points:
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

data = np.array([[2,4],[3,4],[3,0],[2,2],[4,1]])
simplices = Delaunay(data).simplices
plt.triplot(data[:,0], data[:,1], simplices)
plt.scatter(data[:,0], data[:,1], color="r")
plt.show()


# Convex  HUll : it is the smallest polygon that covers all of the given point:
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
data = np.array([[2,4],[3,4],[3,0],[2,2],[4,1],[1,2],[5,0],[3,1],[1,2],[0,2]])
hull = ConvexHull(data)
hull_points = hull.simplices
plt.scatter(data[:,0],data[:,1])
for simplex in hull_points:
    plt.plot(data[simplex,0],data[simplex,1],'k-')
plt.show()


# KDTrees: they are a data structures optimized for the nearest neighbour queries
from scipy.spatial import KDTree
data = [(1,-1),(2,3),(-2,3),[2,-3]]
yash = KDTree(data)
res = yash.query((1,1))
print(res)"""


# Distance matrix: it is used to find the various types of distance between 2 points there are basically 2 type : fuclidean distance cosine distance
# Euclidean distance:
from scipy.spatial.distance import euclidean
p1 = (1,0)
p2 = (10,2)
data = euclidean(p1,p2)
print(data)

#cosine distance
from scipy.spatial.distance import cosine
p1 = (1,0)
p2 = (10,2)
data = cosine(p1,p2)
print(data)