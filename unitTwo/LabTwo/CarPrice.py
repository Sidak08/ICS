'''
File: CarPrice.py
Author: Sidak Singh
Date: Nov 23, 2024

Description:
Calculates the total price of a car based on the base price, PDI rate and HST rate

Function List:
    calcAddedPercentage(percentage, value):
        -devides the percentage by 100 and multiplies it by the value
        -pramters requires: percentage: the percentage value, value as the base number
        -returns the total value
'''
carMake = str(input("Enter the make of the car: "))
carModel = str(input("Enter the model of the car: "))
carPrice = float(input("Enter the price of the car: "))
carPDIRate = float(input("Enter the PDI rate of the car: "))
hstRate = float(input("Enter the HST rate of the car: "))

def calcAddedPercentage(percentage, value):
    return (percentage / 100) * value

pdiCharge = calcAddedPercentage(carPDIRate, carPrice)
taxCharge = calcAddedPercentage(hstRate, carPrice + pdiCharge)

print("You car is a {} {} model and the total price is\
 ${:.2f} which includes ${:.2f} base\
price ${:.2f} for PDI and ${:.2f} for HST.".format(carMake, carModel,
    carPrice + pdiCharge + taxCharge, carPrice, pdiCharge, taxCharge))
