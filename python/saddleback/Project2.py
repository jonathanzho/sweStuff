# ========
# Project2
# ========

# Read US presidents from a text file,
# Then output US presidents in a given range:
def main():
    usPresidents = [];
    file = open('USPres.txt', 'r')

    while True:
        president = file.readline()
        if not president:
            break
        usPresidents.append(president)

    file.close()

    print('Number of lines read: ' + str(len(usPresidents)))

    findPres(usPresidents)

# Output US presidents in a given range:
def findPres(usPresidents):
    lowerNumber = int(input('Enter the lower number for the range: '))
    upperNumber = int(input('Enter the upper number for the range: '))

    print('\n\tPresidents:\n')
    
    for i in range(lowerNumber-1, upperNumber):
        print('\t\t' + str(i+1) + '\t' + usPresidents[i])

main()
