# ===
# CSV
# ===

import csv

# Writer
# ======

outputFile = open('test.csv', 'w', newline='')

outputWriter = csv.writer(outputFile)

outputWriter.writerow(['text1', 'text2', 'text3'])
outputWriter.writerow([1.23, 4.56, 7.898])
outputWriter.writerow([1, 2, 3])

outputFile.close()

# Reader
# ======

inputFile = open('test.csv', 'r')

inputReader = csv.reader(inputFile)

csvData = list(inputReader)

print(csvData)

inputFile.close()
