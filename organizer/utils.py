import time
import io
import logging
import sys
from functools import wraps
from tqdm import tqdm

def timing(func):
    """Decorator to measure the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper


def with_progress_and_logs(desc="Processing"):
    """
    Decorator to manage a progress bar and buffer logs during the execution of a function.
    Args:
        desc (str): Description for the progress bar.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            file_groups = kwargs.get("file_groups", {})
            total_items = sum(len(files) for files in file_groups.values())
            logger = kwargs.get("logger", None)
            # Create a log buffer
            log_stream = io.StringIO()
            stream_handler = logging.StreamHandler(log_stream)
            if logger:
                logger.addHandler(stream_handler)
            
            with tqdm(total=total_items, desc=desc, position=1, leave=True, file=sys.stderr) as progress_bar:
                try:
                    result = func(*args, **kwargs, progress_bar=progress_bar)
                finally:
                    if logger:
                        logger.removeHandler(stream_handler)

                print(log_stream.getvalue(), end="")

            return result

        return wrapper
    return decorator
