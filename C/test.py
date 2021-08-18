import ctypes as ct
import numpy as np


def cfunc(arr, x):
    """
    arr : 1-d array
    x : scalar
    """
    n = arr.size
    
    dll = ct.CDLL('./ctest.so')
    
    # Recall the function prototype is:
    # int func(int, float[], float) 
    
    f = dll.func
    f.argtypes = [
        ct.c_int,
        np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, shape=(n,)),
        ct.c_float
    ]
    f.restype = ct.c_float     # if there is no return value, use `None`.
    
    
    # Remember to check the types of input argmuments
    # `arr` and `x` must be single precision float!
    # `n` is python int object, it can directly pass into function. No need to 
    # worry it.
    
    if arr.dtype != np.float32:
        arr = arr.astype(np.float32, copy=False)
        
    x = np.array(x, dtype=np.float32)
        
        
    # finally
    ans = f(n, arr, x)
    return ans


if __name__ == '__main__':
    arr = np.arange(10, dtype=np.float32)
    x = 2.0
    ans = cfunc(arr, x)
    
    print('arr = ', arr)
    print('x   = ', x)
    print('x * sum(arr) = ', ans)    # 90.0
    
    