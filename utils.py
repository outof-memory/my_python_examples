from functools import wraps
def time_func(func):
    ''' wrapper for a function, get elapse time: func.elapse_time()'''
    elapse_time = 0.
    @wraps(func)
    def newfunc(*args, **kwargs):
        nonlocal elapse_time
        startTime = time.time()
        result = func(*args, **kwargs)
        elapse_time += time.time() - startTime
        return result
    newfunc.elapse_time = lambda: elapse_time
    return newfunc
