import csv
import string
import sys
from time import time

if(len(sys.argv) > 2) :
    with open ('./TotalTime.txt', 'w') as file:
        time = (( (int) (sys.argv[2])-(int) (sys.argv[1])))/1000000
        file.write( (str) (time ) )

