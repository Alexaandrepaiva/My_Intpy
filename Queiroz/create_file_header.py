import csv
import sys

if(len(sys.argv) < 2) :
    with open ('./results-host-python.csv', 'a+') as file:
        writer = csv.writer(file)
        header = ['function name', 'avg time','min time','max time', 'std dev'] 
        writer.writerow(header)

else: 
    fileName = './results-' + str(sys.argv[1]) + '-python.csv'
    with open (fileName, 'a+') as file:
        writer = csv.writer(file)
        header = ['function name', 'avg time','min time','max time', 'std dev'] 
        writer.writerow(header)

