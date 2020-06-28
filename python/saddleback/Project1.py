# =========
# Project 1
# =========

bestInvestorName = ''
bestInvestorGain = 0.0

for i in range(5):
    investorName = input('Enter inverstor name: ')
    stockPurchasePrice = float(input('Enter stock purchase price: '))
    numStocksPurchased = int(input('Enter number of stocks purchased: '))

    stockSalePrice = float(input('Enter stock sale price: '))
    numStocksSold = int(input('Enter number of stocks sold: '))

    purchaseTotalNoCommission = numStocksPurchased * stockPurchasePrice
    purchaseCommission =  purchaseTotalNoCommission * 0.03
a    purchaseTotal = purchaseTotalNoCommission + purchaseCommission
    saleTotalNoCommission = numStocksSold * stockSalePrice
    saleCommission = saleTotalNoCommission * 0.03
    saleTotal = saleTotalNoCommission - saleCommission
    investorGain = saleTotal - purchaseTotal
    print(investorName, purchaseTotalNoCommission, saleTotalNoCommission, investorGain)

    print(purchaseCommission, saleCommission)

    if (investorGain > bestInvestorGain):
        bestInvestorGain = investorGain
        bestInvestorName = investorName

print(bestInvestorName, bestInvestorGain)




    
    
                                     
                                
                         
