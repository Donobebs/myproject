'''WORD COUNT'''
mind = input('what is on your mind today?\n')
res_mimd = len(mind.split())
print(f'oh nice,you just told me whats on your mind in {res_mimd} words')

'''WHATS MY ACRONYM'''
user_input = input(' Please enter phrase\n')
fresh_user_input = (user_input.replace('of',''))
new_phrase = fresh_user_input.split()
acronym = ''
for w in new_phrase:
    acronym = acronym + w[0].upper()
print(f'The acronym for {user_input} is {acronym}')