'''odds or even'''
user_input = int(input('what number are you looking for\n'))
if user_input%2 == 0:
    print('the number you entered is an even number ')
else:
    print('The number entered is an odd number')

'''Mad libs game'''
name = input('Enter name: ')
colour = input('Enter colour: ')
club = input('Enter club: ')
player= input('Enter player: ')
coach = input('Enter coach: ')
league= input('Enter league')
top_scorer = input('Enter topscorer')
print(f'my name is '+ name,'my favourite colour is '+colour,'my favourite club is'+club,f'my best player in {club } is {player} due to {coach} influence oh him,{top_scorer} is now the topscorer in the {league}')
