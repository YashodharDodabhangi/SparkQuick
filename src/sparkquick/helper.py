import functools
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union, Callable, List, Dict
from time import time
from typing import Callable


def time_it(func: Callable)->Callable:
    '''
    Why Use time_it?
    Performance Measurement: It helps to measure how long a function takes to run, which is crucial in identifying bottlenecks in code performance.
    Debugging: You can quickly instrument critical sections of your code to monitor how they perform under different conditions or inputs.
    Profiling: It can be used as a lightweight profiler to gather execution times for multiple functions.
    
    Benefits of Using the time_it Decorator:
    Reusability: Once defined, the time_it decorator can be applied to any function you want to time, without modifying the function itself.
    Clean Code: The decorator abstracts the timing logic, so your original functions remain clean and focused on their main purpose.
    Easy to Apply: By simply adding @time_it before any function definition, you can immediately start tracking the execution time.
    
    When to Use It:
    When optimizing code performance.
    During development to ensure that critical functions run within an acceptable time frame.
    For debugging and testing performance degradation when code changes.
    
    '''
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time()
        function_result=func(*args,**kwargs)
        end_time=time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")  # Print the time taken
        return function_result
    return wrapper






