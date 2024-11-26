'''
File: EnhancedCarPrice.py
Author: Sidak Singh
Date: Nov 23, 2024

Description:
Calculates the total price for three cars based on the base price, PDI rate and HST rate

Function List:
    calcAddedPercentage(percentage, value):
        -devides the percentage by 100 and multiplies it by the value
        -pramters requires: percentage: the percentage value, value as the base number
        -returns the total value
'''
def calcAddedPercentage(percentage, value):
    return (percentage / 100) * value

carMake = [""] * 3
carModel = [""] * 3
carPrice = [0.0] * 3
carPrice = [0.0] * 3
carPDIRate = [0.0] * 3
carHstRate = [0.0] * 3
pdiCharge = [0.0] * 3
taxCharge = [0.0] * 3

for i in range(len(carMake)):
    carMake[i] = str(input("Enter the make of the car: "))
    carModel[i] = str(input("Enter the model of the car: "))
    carPrice[i] = float(input("Enter the price of the car: "))
    carPDIRate[i] = float(input("Enter the PDI rate of the car: "))
    carHstRate[i] = float(input("Enter the HST rate of the car: "))

    pdiCharge[i] = calcAddedPercentage(carPDIRate[i], carPrice[i])
    taxCharge[i] = calcAddedPercentage(carHstRate[i], carPrice[i] + pdiCharge[i])

    print("For car {} which is a {} {} the total price is\
 ${:,.2f} which includes ${:,.2f} base\
 price ${:,.2f} for PDI and ${:,.2f} for HST.".format(i+1, carMake[i], carModel[i],
carPrice[i] + pdiCharge[i] + taxCharge[i], carPrice[i], pdiCharge[i], taxCharge[i]))
