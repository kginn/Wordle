'''
Kyle Ginn
Wordle Game
'''
import random
import linecache

def generate_word():
    '''
    selects a random 5 letter word for the game
    '''
    word = linecache.getline('wordle_answers.txt', random.randint(1, 2309))
    word = word.strip()

    return word

def check_grey(l, w):
    '''
    checks if the letter is grey
    '''
    if l in w:
        return False

    return True

def check_yellow(l, w):
    '''
    checks if the letter is yellow
    '''
    if l in w:
        return True
    
    return False

def check_green(g, w, x):
    '''
    checks if the letter is green
    '''

    if g[x] == w[x]:
            
        return True
            
    return False

def count_letter(word, letter):
    '''
    counts the number of the letter in the word
    '''
    l_count = 0
    x = -1
    for l in word:
        x += 1
        if word[x] == letter:
            l_count += 1
            
    return l_count

def green_found(guess, word, letter):
    '''
    if there are muiltple of one letter checks if letter should be yellow or grey
    or if a green has not been found
    '''
    x = -1
    for l in guess:
        x += 1
        if check_green(guess, word, x) == True and guess[x] == letter:
            if count_letter(word, letter) > 1:
                return 'yellow'
            else:
                return 'grey'
            
    return 'no green'
            
def check_word(g, w):
    '''
    assigns color to each letter
    '''
    x = -1 #index variable
    
    for l in g:
        x += 1
        if check_yellow(g[x], w) == True:
            if check_green(g, w, x) == True:
                print(f'{g[x]} is green')
            elif green_found(g, w, g[x]) == 'yellow':
                print(f'{g[x]} is yellow')
            elif green_found(g, w, g[x]) == 'grey':
                print(f'{g[x]} is grey')
            elif green_found(g, w, g[x]) == 'no green':
                print(f'{g[x]} is yellow')
        elif check_grey(g[x], w) == True:
            print(f'{g[x]} is grey')
        
    return
            
def check_guess(guess):
    '''
    checks if the guess is in the wordle library
    '''
    with open('wordle_list.txt') as file:
        for line in file:
            line = line.strip()
            if guess == line:
                return True

    return False

def check_win(guess, word):
    '''
    checks if the guess is the right word
    '''
    if guess == word:
        return True

    return False

def enter_guess():
    '''
    promts user to enter wordle guess
    '''
    guess = input('Enter five letter word: ')
    guess = str(guess)

    return guess

def play_again():
    '''
    asks if user wants to play again
    '''
    answer = input('would you like to play again? yes or no: ')
    answer = str(answer)
   
    while answer != 'yes' or answer != 'no':
        if answer == 'yes':
            return True
        if answer == 'no':
            return False
        print(f'sorry I dont understand\n')
        answer = input('would you like to play again? yes or no: ')
        
    return 

def main():
    '''
    main driver for wordle
    '''
    
    x = 0
    word = generate_word()
    
    for i in range(6):
        x += 1
        if x == 1:
            print(f'\nFirst Guess\n')
        elif x == 2:
            print(f'\nSecond Guess\n')
        elif x == 3:
            print(f'\nThird Guess\n')
        elif x == 4:
            print(f'\nFourth Guess\n')
        elif x == 5:
            print(f'\nFifth Guess\n')
        elif x == 6:
            print(f'\nLast Guess\n')
        
        guess = enter_guess()
        while check_guess(guess) == False:
            print(f'This is not a valid word please try again\n')
            guess = enter_guess()
        if check_win(guess, word) == True:
            print('You win!')
            break
        
        check_word(guess, word)

        if x == 6 and check_win(guess, word) == False:
            print(f'\ngame over \nYou lose :(')

    print(f'\nThe word was {word}')

    if play_again() == True:
        main()  

    return

print(f'\nWelcome to the wordle practice game\nYou have six tries to guess the word')
main()


