import sys
from importlib.metadata import version

print("Python:", sys.version.split()[0])
print("Flask:", version("flask"))
print("Setup OK!")