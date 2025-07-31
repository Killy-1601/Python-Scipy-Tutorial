# what is sparse data: sparse data is the data that has mostly unused elements.like the elements that dont carry any info.[1,0,2,0,4,5,0,2,3,5,2]
# sparse data example [1,0,2,0,0,3,0,0,0,0,0,4]
# dense array: [2,5,6,,8,9,7,1,2,3,6]
# how to work with sparse data.
# scipy has a module scipy.sparce function. there are 2 metrics in this sparse: CSC(compressed sparse column) and CSR(compresses sparce row)

# CSR matrics: here we will create a CSR matrics from an array
import numpy as np
from scipy.sparse import csr_matrix
data = np.array([0,0,0,0,0,0,1,1,0,2])
print(csr_matrix(data))


#sparse matrix methods 
import numpy as np
from scipy.sparse import csr_matrix
data = np.array([[0,0,0],[0,0,1],[1,0,2,]])
print(csr_matrix(data).data)


# what if we want to count nonzeros, we can do this via count_nonzero() method
import numpy as np
from scipy.sparse import csr_matrix
data = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(data).count_nonzero)


# for removing the zero elements from the metrix we will yse eliminate_zeros().
import numpy as np
from scipy.sparse import csr_matrix
data = np.array([[0,0,0],[0,0,1],[1,0,2]])
newdata= csr_matrix(data)
newdata.eliminate_zeros()
print(newdata)


# eliminating duplicate entries with the sum_duplicates() method
import numpy as np
from scipy.sparse import csr_matrix
data = np.array([[0,0,0],[0,0,1],[1,0,2]])
newdata= csr_matrix(data)
newdata.sum_duplicates()
print(newdata)


# here we will convert csr to csc with the tocsc():
import numpy as np
from scipy.sparse import csr_matrix
data = np.array([[0,0,0],[0,0,1],[1,0,2]])
newdata= csr_matrix(data).tocsc()
print(newdata)
