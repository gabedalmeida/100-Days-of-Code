'''welcome to the tip calculator!
What was the total bill?
How many people to split the bill?
What percentage tip would you like to give?
'''
# 123_456 == 123456
#number = 123
#print('I cant ' +number+ 'do this') str+int+str

print('Welcome to the tip calculator!')
bill = float(input('What the total bill?\n'))
people = int(input('How many people to split the bill?\n'))
tip = int(input('What percentage tip would you like to give?10,12 or 15\n'))
bill_with_tip = round((tip / 100) * bill + bill)
bill_per_person = bill_with_tip / people
final_bill_per_person = round(bill_per_person, 2)
final_bill_per_person = "{:.2f}".format(bill_per_person)

print(f'Each person should pay: {final_bill_per_person}$')