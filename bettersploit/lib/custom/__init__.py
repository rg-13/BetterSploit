import os, pkgutil

__all__ =  list(name for _, name, _ in pkgutil.iter_modules([glob.glob(/dir/*)]))