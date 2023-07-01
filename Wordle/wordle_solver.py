'''
Kyle Ginn
Wordle Solver
'''
def list_start():
    '''
    puts possible wordle answers into a python list
    '''
    word_list = []
    with open('wordle_answers.txt') as file:
        for line in file:
            line = line.strip()
            word_list.append(line)

    return word_list

def update_list(words):
    '''
    updates the list and removes repeating words
    '''
    w_list = []
    for x in words:
        if x not in w_list:
            w_list.append(x)

    return w_list

def grey_letter(letter, w_list):
    '''
    only looks at values in the list that does not have
    the letter
    '''
    n_list = []
    for line in w_list:
        if letter not in line:
            n_list.append(line)
                
    return n_list

def green_letter(letter, position, w_list):
    '''
    removes values from the list that do not have
    the right letter in the right position
    '''
    n_list = []
    for line in w_list:
        if letter == line[position]:
            n_list.append(line)

    return n_list

def yellow_letter(letter, position, w_list):
    '''
    removes values from the list that have the letter in the
    position or that does not have the letter in the value
    '''
    n_list = []
    for line in w_list:
        if letter != line[position] and letter in line:
            n_list.append(line)

    return n_list

def check_guess(guess):
    '''
    checks if the guess is in the wordle library
    '''
    with open('wordle_list.txt') as file:
        for line in file:
            line = line.strip()
            if guess == line:
                return True
    file.close()
    
    return False

def check_win():
    '''
    checks if the answer has been found
    '''
    while True:
        win = input('did you get it right? (y or n): ')
        if win == 'y':
            print('congrats :)')
            return
            break
            
        if win == 'n':
            return False
            break
        
    return False

def print_list(w_list):
    '''
    prints the list of words
    '''
    for line in w_list:
        print(line)

    return

def input_guess():
    '''
    prompts user to input the guess they made
    '''
    guess = input('Enter your five letter word: ')
    guess = str(guess)
    while check_guess(guess) == False:
        guess = input('Please input a valid five letter word: ')
        
    return guess

def input_colors(guess, w_list):
    '''
    inputs the color for letters and returns list of possible words
    '''
    n_list = w_list
    x = -1
    for i in range(5):
        x += 1
        l_color = input(f'enter the color of {guess[x]} (g, y, or w): ')
        if l_color == 'g':
            n_list = green_letter(guess[x], x, n_list)
        elif l_color == 'y':
            n_list = yellow_letter(guess[x], x, n_list)
        elif l_color == 'w':
            n_list = grey_letter(guess[x], n_list)

    return n_list

#letter count section


alphabet = ('a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z')
a_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
          'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
          'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
          'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
          'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}


def word_letter_count(word, letter):
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

def letter_count(w_list, letter):
    '''
    counts how many of a letter is in the
    updated list
    '''
    x = -1
    letter_count = 0
    for word in w_list:
        for l in word:
            if letter == l:
                letter_count += 1

    return letter_count

def all_letter_count(w_list):
    '''
    counts every letter and adds the value to a_dict
    '''
    x = -1
    for v in a_dict:
        x += 1
        a_dict[alphabet[x]] = letter_count(w_list, alphabet[x])
    
    return a_dict

def sort_dict(a_dict):
    '''
    sorts the dictionary by value
    ''' 
    s_dict = dict(sorted(a_dict.items(), key = lambda x: x[1], reverse = True))

    for v in alphabet:
        if s_dict[v] <= 0:
            del s_dict[v]
    
    return s_dict


def word_dict(w_list):
    '''
    puts the words in the list into a dictionary
    '''
    w_dict = {}
    
    for w in w_list:
        w_dict.update({w : 0})

    return w_dict


def word_score(w_list, l_dict):
    '''
    gives a score for each word in the list
    '''
    score_dict = word_dict(w_list)

    x = -1
    for word in w_list:
        for i in range(5):
            x += 1
            for l in word:
                score_dict[word] += l_dict[l]

                if word_letter_count(word, l) > 1:
                    count = word_letter_count(word, l) - 1
                    for i in range(count):
                        score_dict[word] -= l_dict[l]
    
    n_score = sorted(score_dict.items(), key = lambda x: x[1], reverse = True)

    return n_score


def dict_option(w_list):
    '''
    gives the option to show letter counts
    '''
    choice = str(input('show dictionary (y, n): '))
    
    if choice == 'y':
        print(w_list)
    elif choice == 'n':
        return
    else:
        choice = str(input('show dictionary (y, n): '))
    return

#main driver
def main():
    '''
    main driver for solver
    '''
    w_list = list_start()

    guess = input_guess()
    
    n_list = input_colors(guess, w_list)
    print_list(n_list)
    score_dict = word_score(n_list, all_letter_count(n_list))
    dict_option(score_dict)
    
    while check_win() == False:
        n_list = input_colors(input_guess(), n_list)
        print_list(n_list)
        score_dict = word_score(n_list, all_letter_count(n_list))
        dict_option(score_dict)

    return

main()

