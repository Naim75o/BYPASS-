print ("\x1b[32minjecting bypass File")
print ("\x1b[32mPLEASE WAIT")
import os, sys
try:
    __import__("SpYPro").file()
except Exception as e:
    exit(str(e))
