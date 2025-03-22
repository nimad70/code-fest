import time


def timeIt(func):
    """
    Compute and display the time of execution in milliseconds of a function
    
    Args:
        func: function to time
    """
    start = time.time()
    func()
    end = time.time()
    exe_time = (end - start) * 10**3
    print(f"The time of execution is: {exe_time} ms")