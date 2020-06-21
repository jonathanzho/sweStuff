numTotalShares = 0
grandTotalCost = 0.0

while True:
    print("\nEnter number of shares purchased for the day. Enter 0 to exit:")
    numDailyShares = int(input())
    numTotalShares = numTotalShares + numDailyShares
    
    if numDailyShares == 0:
        break
    
    print("\nEnter share price for the day:")
    dailySharePrice = float(input())
    dailyTotalCost = numDailyShares * dailySharePrice
    
    print("\n==========Daily total cost = " + str(dailyTotalCost))
    
    grandTotalCost = grandTotalCost + dailyTotalCost
    
print("\n==========Grand total cost = " + str(grandTotalCost))

averageSharePrice = grandTotalCost / numTotalShares
print("\n==========Average share price = " + str(averageSharePrice))
          
    
