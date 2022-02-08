# lesson 61

import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    # print(csvReader)
    # print(list(csvReader))
    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])
print(names)
print(stats)
index = names.index('Joe')
loanStatus = stats[index]
print('loan status is '+loanStatus)

with open('utilities/loanapp.csv','a') as wFile: # 'w' to rewrite whole data, 'a' to append data
    write = csv.writer(wFile)
    write.writerow([\n'Bob','Rejected'])


