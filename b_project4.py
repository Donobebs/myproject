'''Percentage tip'''
def tip_calc():
    tip_percent = float(input('please enter tip percentage(%): '))
    bill_dollars = float(input('please enter the bill amount($): '))
    tip_amount = tip_percent * bill_dollars / 100
    print(f'{tip_percent} tip is {tip_amount} which brings your total to {tip_amount + bill_dollars}')
    users_involved = int(input('number of people involved'))
    print(f'each person gets a tip of {tip_amount/users_involved} and a total cost of {tip_amount + bill_dollars/users_involved}')
tip_calc()


'''Email Slicer'''
email = input('Enter your email address: ').strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1: ]
print(f'your username is {username} and your domain is {domain}')
