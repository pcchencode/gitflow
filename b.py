import os
import sys
from a import func

print("start calling function from a.py")
print("AAA")
func()
print("BBB")
print("done")

os._exit(0)
