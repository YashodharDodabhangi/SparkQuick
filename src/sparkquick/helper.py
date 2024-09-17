import functools
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union, Callable, List, Dict
from time import time
from typing import Callable


def time_it(func: Callable)->Callable:
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        srt_time=time()
        function_result=func(*args,**kwargs)
        end_time=time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")  # Print the time taken
        return function_result
    return wrapper





