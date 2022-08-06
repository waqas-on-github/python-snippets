#Light is currently off
# .............If...............
# In keeping with the light switch example, the state of the switch can be stored with a Boolean value of True or False.


current = False

if current:
    current = False
    print('Turning light off')

if not current:
    current = True
    print('Turning light on')


# ...............If else............
# The above code works fine but it can be rewritten more effectively by using another condition called else. The following code is an example:
current = False

if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')

    # ............ elif..........
# Python also has another condition called elif which helps when you have multiple conditions to satisfy. The light switch example is pretty straightforward in that you only have to check for the state of on or off - True or False. In certain conditions, it may not be that easy. Thankfully elif is here to help.
loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))