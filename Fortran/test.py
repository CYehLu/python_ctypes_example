import ctypes as ct
import numpy as np


def fsub(arr, x):
    """
    Wrapper of subroutine `sub`
    arr : 1-d array
    x : scalar
    """
    n = arr.size
    
    dll = ct.CDLL('./ftest.so')
    
    # Fortran is pass-by-reference
    # thus the arguments will be pointers
    
    sub = dll.sub
    sub.argtypes = [
        ct.POINTER(ct.c_int),
        np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, shape=(n,)),
        ct.POINTER(ct.c_float),
        ct.POINTER(ct.c_float)
    ]
    sub.restype = None     # fortran subroutine has no return value
    
    
    # Remember to check the types of input argmuments
    # `arr` must be single precision float!
    
    if arr.dtype != np.float32:
        arr = arr.astype(np.float32, copy=False)
        
        
    # Finally
    # Again, remember that Fortran is pass-by-reference, so we need `ct.byref`.
    # `ct.byref()` only allows ctype instances.
    n = ct.c_int(n)
    x = ct.c_float(x)
    ans = ct.c_float(0) 
    
    sub(
        ct.byref(n), 
        arr, 
        ct.byref(x), 
        ct.byref(ans)     # `ans` will be modified here
    )    
    
    # `ans` is an updated-ctype instance. Use `.value` to obtain its value.
    return ans.value


def ffunc(arr, x):
    """
    Wrapper of function `func`
    arr : 1-d array
    x : scalar
    """
    n = arr.size
    
    dll = ct.CDLL('./ftest.so')
    
    # Fortran is pass-by-reference
    # thus the arguments will be pointers
    
    f = dll.func
    f.argtypes = [
        ct.POINTER(ct.c_int),
        np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, shape=(n,)),
        ct.POINTER(ct.c_float)
    ]
    f.restype = ct.c_float
    
    
    # Remember to check the types of input argmuments
    # `arr` must be single precision float!
    
    if arr.dtype != np.float32:
        arr = arr.astype(np.float32, copy=False)
        
        
    # Finally
    # Again, remember that Fortran is pass-by-reference, so we need `ct.byref`.
    # `ct.byref()` only allows ctype instances.
    n = ct.c_int(n)
    x = ct.c_float(x)
    
    ans = f(
        ct.byref(n), 
        arr, 
        ct.byref(x), 
    )    
    
    return ans


if __name__ == '__main__':
    arr = np.arange(10, dtype=np.float32)
    x = 2.0
    ans = fsub(arr, x)
    
    print('----- Using subroutine -----')
    print('arr = ', arr)
    print('x   = ', x)
    print('x * sum(arr) = ', ans)    # 90.0
    print()
    
    
    arr = np.arange(10, dtype=np.float32)
    x = 2.0
    ans = ffunc(arr, x)
    
    print('----- Using function -----')
    print('arr = ', arr)
    print('x   = ', x)
    print('x * sum(arr) = ', ans)    # 90.0
    
    