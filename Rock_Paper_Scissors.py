#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import shuffle


# In[4]:


def bot_shuf():

    botlist = ['rock', 'paper', 'scissors']

    shuffle(botlist)
    
    return botlist[0]


# In[5]:


def user_pick():
    
    userlist = ['rock','paper','scissors']
    
    pick = input('Your pick: ')
    
    if pick == 'rock':
        return pick
    if pick == 'paper':
        return pick
    if pick == 'scissors':
        return pick
    else:
        print("You didn't select a proper answer, one has been chosen at random for you")
        shuffle(userlist)
        return(userlist[0])


# In[6]:


def game(a,b):
    
    if a == 'rock':
        if b == 'rock':
            print('Bot pick: ' + b + ' DRAW')
            return 'DRAW'
        if b == 'scissors':
            print('Bot pick: ' + b + ' YOU WIN')
            return 'WIN'
        if b == 'paper':
            print('Bot pick: ' + b + ' YOU LOSE')
            return 'LOSE'
    if a == 'paper':
        if b == 'rock':
            print('Bot pick: ' + b + ' YOU WIN')
            return 'WIN'
        if b == 'scissors':
            print('Bot pick: ' + b + ' YOU LOSE')
            return 'LOSE'
        if b == 'paper':
            print('Bot pick: ' + b + ' DRAW')
            return 'DRAW'
        
    if a == 'scissors':
        if b == 'rock':
            print('Bot pick: ' + b + ' YOU LOSE')
            return 'LOSE'
        if b == 'scissors':
            print('Bot pick: ' + b + ' DRAW')
            return 'DRAW'
        if b == 'paper':
            print('Bot pick: ' + b + ' YOU WIN')
            return 'WIN'
            
            


# In[9]:


print('Welcome to rock, paper, scissors. If you win or draw you keep playing, if you lose you restart')
select = input('Would you like to play? Enter yes or no: ')

if select.lower()[0] == 'y':
    game_on = True

else:
    game_on = False
    
total = []

while game_on:
    
    x = game(user_pick(), bot_shuf())
    if x == 'WIN':
        total.append('w')
        continue
    if x == 'DRAW':
        continue
    elif x == 'LOSE':
        game_on = False
        
while not game_on:
    wins = len(total)
    if wins > 0:
        print(f'Thanks for playing! You won {wins} times!')
    else:
        print('Wow, you suck!')
    break


