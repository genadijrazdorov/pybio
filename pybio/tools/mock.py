import functools
import warnings


def mock(function):
    @functools.wraps(function)
    def mock_wrapper(*args, **kwargs):
        warnings.warn("'{}' is a mock (stub).".format(function.__name__))
        return function(*args, **kwargs)

    return mock_wrapper
