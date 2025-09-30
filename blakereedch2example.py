'''A customer in a store is purchasing 3 items. Write a program 
that asks for the price of each item, then displays the subtotal of the
sale, the amount of sales tax, and the total. Assume the sales tax is 10 percent.
'''

# Constant for the sales tax rate.
TAX_RATE = 0.10

# Get the price of each item.
item1 = float(input('Enter the price of item #1: '))
item2 = float(input('Enter the price of item #2: '))
item3 = float(input('Enter the price of item #3: '))

# Calculate the subtotal.
subtotal = item1 + item2 + item3

# Calculate the sales tax.
tax = subtotal * TAX_RATE

# Calculate the total.
total = subtotal + tax

# Print the values.
print (f'Subtotal: {subtotal:.2f}')
print (f'Sales Tax: {tax:.2f}')
print (f'Total: {total:.2f}')
