# ==========
# Code Lab 2
# ==========

# Purchse:

numSharesPurchased = int(input('Enter number of shares purchased: '))

sharePurchasePrice = float(input('Enter share purchase price: '))

purchaseCommissionRate = float(input('Enter purchase commission rate: '))

# Sale

numSharesSold = int(input('Enter number of shares sold: '))

shareSalePrice = float(input('Enter share sale price: '))

saleCommissionRate = float(input('Enter sale commission rate: '))

# Gain or loss

totalPurchaseNoCommission = numSharesPurchased * sharePurchasePrice
print('\n>>>Total cost without commission: ' + str(totalPurchaseNoCommission))

totalPurchaseCommission = totalPurchaseNoCommission * purchaseCommissionRate
print('\n>>>Commission for the purchase: ' + str(totalPurchaseCommission))

totalSaleNoCommission  = numSharesSold * shareSalePrice
print('\n>>>Total sale without commission: ' + str(totalSaleNoCommission))

totalSaleCommission = totalSaleNoCommission * saleCommissionRate
print('\n>>>Commission for the sale: ' + str(totalSaleCommission))

totalPurchaseWithCommission = totalPurchaseNoCommission + totalPurchaseCommission
print('\n>>>Total cost: ' + str(totalPurchaseWithCommission))

totalSaleWithCommission = totalSaleNoCommission - totalSaleCommission
print('\n>>>Total sale: ' + str(totalSaleWithCommission))

difference = totalSaleWithCommission - totalPurchaseWithCommission

print('\n>>>Difference (gain or loss if negative): ' + str(difference))                         
