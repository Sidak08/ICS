# Test code for the given questions

street = "Daviselm St."
address = "45"

# 1. street[1]
print("1:", street[1])  # Second character of street
print("Data type:", type(street[1]))  # Data type of the result

# 2. street.upper()
print("2:", street.upper())  # Uppercase version of street
print("Data type:", type(street.upper()))  # Data type of the result

# 3. street + address
print("3:", street + address)  # Concatenation of street and address
print("Data type:", type(street + address))  # Data type of the result

# 4. address + street
print("4:", address + street)  # Concatenation of address and street
print("Data type:", type(address + street))  # Data type of the result

# 5. address.replace('5', '8')
print("5:", address.replace('5', '8'))  # Replace '5' with '8' in address
print("Data type:", type(address.replace('5', '8')))  # Data type of the result

# 6. address.replace('6', '8')
print("6:", address.replace('6', '8'))  # Replace '6' with '8' in address (no '6' in address)
print("Data type:", type(address.replace('6', '8')))  # Data type of the result

# 7. street[:5]
print("7:", street[:5])  # First 5 characters of street
print("Data type:", type(street[:5]))  # Data type of the result

# 8. street[5:]
print("8:", street[5:])  # Characters of street starting from index 5
print("Data type:", type(street[5:]))  # Data type of the result

# 9. street[4:7]
print("9:", street[4:7])  # Characters of street from index 4 to 7 (exclusive)
print("Data type:", type(street[4:7]))  # Data type of the result

# 10. address.index('45')
print("10:", address.index('45'))  # Index of substring '45' in address
print("Data type:", type(address.index('45')))  # Data type of the result

# 11. address.index('5')
print("11:", address.index('5'))  # Index of character '5' in address
print("Data type:", type(address.index('5')))  # Data type of the result

# 12. address.find('5')
print("12:", address.find('5'))  # Index of character '5' in address (same as index but doesn't raise error)
print("Data type:", type(address.find('5')))  # Data type of the result

# 13. address.find('7')
print("13:", address.find('7'))  # Find '7' in address (returns -1 as '7' doesn't exist)
print("Data type:", type(address.find('7')))  # Data type of the result

# 14. len(street)
print("14:", len(street))  # Length of the street string
print("Data type:", type(len(street)))  # Data type of the result

# 15. street[0:2] + " hat"
print("15:", street[0:2] + " hat")  # Concatenates the first 2 characters of street with " hat"
print("Data type:", type(street[0:2] + " hat"))  # Data type of the result

# 16. street.split(" ", 1)
print("16:", street.split(" ", 1))  # Split street into two parts at the first space
print("Data type:", type(street.split(" ", 1)))  # Data type of the result

# 17. ord(street[0])
print("17:", ord("h"))  # ASCII value of the first character in street
print("Data type:", type(ord(street[0])))  # Data type of the result

# 18. chr(ord(street[0]))
print("18:", chr(ord(street[0])))  # Convert the ASCII value of the first character back to character
print("Data type:", type(chr(ord(street[0]))))  # Data type of the result
