# scipy matlab arrays: exporting the data in matlab format
#for converting or export data we use savemat(). here we have 3 parametars: filename, mdict, do_compression 
# example: here now we will export the below array as variable name "vec" to matlab file.

from scipy import io
import numpy as np
data = np.arange(10)
io.savemat('data.mat',{"vec":data})


# here now we will import the existing  matlab file. it have only 1 parameter that is filename:
from scipy import io
import numpy as np
data=np.array([0,1,2,3,4,5,6,7,8,9])
io.savemat('data.mat',{"vec":data})
newdata = io.loadmat('data.mat', squeeze_me = True)
print(newdata['vec'])