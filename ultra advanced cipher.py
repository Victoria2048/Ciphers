from random import randint

def encrypt(plaintext:str, loopthroughs:int=1):
    plaintext = [letter for letter in plaintext.upper() if letter.isalpha()] # Removes anything that's not a letter and puts it in a list. Plaintext is by default upper incase loopthroughs = 0
    len_plaintext = len(plaintext)
    for n in range(loopthroughs):
        count = 0
        plaintext = [letter.lower() for letter in plaintext]
        if len_plaintext % 2 == 0: # cipher one
            for char in plaintext:
                if char == 'e': plaintext[count] = 'U'
                elif char == 'a': plaintext[count] = 'G'
                elif char == 'i': plaintext[count] = 'S'
                elif char == 'o': plaintext[count] = 'D'
                elif char == 'u': plaintext[count] = 'A'
                elif char == 'b': plaintext[count] = 'W'
                elif char == 'c': plaintext[count] = 'M'
                elif char == 'd': plaintext[count] = 'J'
                elif char == 'f': plaintext[count] = 'K'
                elif char == 'g': plaintext[count] = 'L'
                elif char == 'h': plaintext[count] = 'Z'
                elif char == 'j': plaintext[count] = 'X'
                elif char == 'k': plaintext[count] = 'C'
                elif char == 'l': plaintext[count] = 'V'
                elif char == 'm': plaintext[count] = 'R'
                elif char == 'n': plaintext[count] = 'E'
                elif char == 'p': plaintext[count] = 'F'
                elif char == 'q': plaintext[count] = 'T'
                elif char == 'r': plaintext[count] = 'I'
                elif char == 's': plaintext[count] = 'H'
                elif char == 't': plaintext[count] = 'O'
                elif char == 'v': plaintext[count] = 'Q'
                elif char == 'w': plaintext[count] = 'Y'
                elif char == 'x': plaintext[count] = 'N'
                elif char == 'y': plaintext[count] = 'P'
                elif char == 'z': plaintext[count] = 'B'
                else: plaintext[count] = '?'
                count += 1
        else: #cipher two
            for char in plaintext:    
                if char == 'e': plaintext[count] = 'B'
                elif char == 'a': plaintext[count] = 'X'
                elif char == 'i': plaintext[count] = 'F'
                elif char == 'o': plaintext[count] = 'L'
                elif char == 'u': plaintext[count] = 'R'
                elif char == 'b': plaintext[count] = 'Y'
                elif char == 'c': plaintext[count] = 'Z'
                elif char == 'd': plaintext[count] = 'A'
                elif char == 'f': plaintext[count] = 'C'
                elif char == 'g': plaintext[count] = 'D'
                elif char == 'h': plaintext[count] = 'E'
                elif char == 'j': plaintext[count] = 'G'
                elif char == 'k': plaintext[count] = 'H'
                elif char == 'l': plaintext[count] = 'I'
                elif char == 'm': plaintext[count] = 'J'
                elif char == 'n': plaintext[count] = 'K'
                elif char == 'p': plaintext[count] = 'M'
                elif char == 'q': plaintext[count] = 'N'
                elif char == 'r': plaintext[count] = 'O'
                elif char == 's': plaintext[count] = 'P'
                elif char == 't': plaintext[count] = 'Q'
                elif char == 'v': plaintext[count] = 'S'
                elif char == 'w': plaintext[count] = 'T'
                elif char == 'x': plaintext[count] = 'U'
                elif char == 'y': plaintext[count] = 'V'
                elif char == 'z': plaintext[count] = 'W'
                else: plaintext[count] = '?'
                count += 1

        # This whole section is for shuffling
        if len_plaintext >= 5:
            for i in range(len_plaintext // 5):
                change = i * 5
                plaintext[0 + change], plaintext[4 + change] = plaintext[4 + change], plaintext[0 + change]
                plaintext[1 + change], plaintext[3 + change] = plaintext[3 + change], plaintext[1 + change]

        if len_plaintext >= 2:
            for i in range(len_plaintext // 2):
                change = i * 2
                plaintext[0 + change], plaintext[1 + change] = plaintext[1 + change], plaintext[0 + change]
            plaintext = plaintext[len_plaintext // 2:] + plaintext[:len_plaintext // 2] # This statement "cuts the deck" so to speak


        # Adds a random character to the beginning of the list to shift everythintg over and make the repititions different
        if loopthroughs > 1:
            if n % 2 == 0:
                plaintext.insert(0, chr(randint(65, 90)))
            else:
                plaintext.append(chr(randint(65, 90)))
            len_plaintext += 1
    
# This section is for the salt, just a little spice added at the end.
    # Adds an extra partial cipher 50% of the time
    if randint(1, 10) > 5:
        count = 0
        for char in plaintext:    
            if char == 'O': plaintext[count] = ','
            elif char == 'U': plaintext[count] = '.'
            elif char == 'B': plaintext[count] = '_'
            elif char == 'C': plaintext[count] = '='
            elif char == 'D': plaintext[count] = '+'
            elif char == 'F': plaintext[count] = '-'
            elif char == 'G': plaintext[count] = '~'
            elif char == 'H': plaintext[count] = '`'
            elif char == 'J': plaintext[count] = '0'
            elif char == 'K': plaintext[count] = '9'
            elif char == 'L': plaintext[count] = '8'
            elif char == 'Y': plaintext[count] = '7'
            elif char == 'N': plaintext[count] = '6'
            elif char == 'P': plaintext[count] = '5'
            elif char == 'Q': plaintext[count] = '4'
            elif char == 'R': plaintext[count] = '3'
            elif char == 'S': plaintext[count] = '2'
            elif char == 'X': plaintext[count] = '1'
            count += 1
    else: # 50% of the time inverts every other letter in alphabetical order and then reverses the whole text
        count = 0
        for char in plaintext:
            if count % 2 == 0:
                if char == 'A': plaintext[count] = 'Z'
                elif char == 'B': plaintext[count] = 'Y'
                elif char == 'C': plaintext[count] = 'X'
                elif char == 'D': plaintext[count] = 'W'
                elif char == 'E': plaintext[count] = 'V'
                elif char == 'F': plaintext[count] = 'U'
                elif char == 'G': plaintext[count] = 'T'
                elif char == 'H': plaintext[count] = 'S'
                elif char == 'I': plaintext[count] = 'R'
                elif char == 'J': plaintext[count] = 'Q'
                elif char == 'K': plaintext[count] = 'P'
                elif char == 'L': plaintext[count] = 'O'
                elif char == 'M': plaintext[count] = 'N'
                elif char == 'N': plaintext[count] = 'M'
                elif char == 'O': plaintext[count] = 'L'
                elif char == 'P': plaintext[count] = 'K'
                elif char == 'Q': plaintext[count] = 'J'
                elif char == 'R': plaintext[count] = 'I'
                elif char == 'S': plaintext[count] = 'H'
                elif char == 'T': plaintext[count] = 'G'
                elif char == 'U': plaintext[count] = 'F'
                elif char == 'V': plaintext[count] = 'E'
                elif char == 'W': plaintext[count] = 'D'
                elif char == 'X': plaintext[count] = 'C'
                elif char == 'Y': plaintext[count] = 'B'
                elif char == 'Z': plaintext[count] = 'A'
            count += 1
        plaintext.reverse()

    return("".join(plaintext))


def decrypt(ciphertext:str, loopthroughs:int=1): # Inverse function of encrypt()
    ciphertext = list(ciphertext.lower()) # puts characters into a list
    len_ciphertext = len(ciphertext)

    # This section is for reversing the salt
    count = 0
    if any(char in ciphertext for char in (',', '.', '_', '=', '+', '-', '~', '`', '0', '9', '8', '7', '6', '5', '4', '3', '2', '1')): # Checks for the partial cipher and reverses it
        for char in ciphertext:    
            if ',' == char: ciphertext[count] = 'o'
            elif '.' == char: ciphertext[count] = 'u'
            elif '_' == char: ciphertext[count] = 'b'
            elif '=' == char: ciphertext[count] = 'c'
            elif '+' == char: ciphertext[count] = 'd'
            elif '-' == char: ciphertext[count] = 'f'
            elif '~' == char: ciphertext[count] = 'g'
            elif '`' == char: ciphertext[count] = 'h'
            elif '0' == char: ciphertext[count] = 'j'
            elif '9' == char: ciphertext[count] = 'k'
            elif '8' == char: ciphertext[count] = 'l'
            elif '7' == char: ciphertext[count] = 'y'
            elif '6' == char: ciphertext[count] = 'n'
            elif '5' == char: ciphertext[count] = 'p'
            elif '4' == char: ciphertext[count] = 'q'
            elif '3' == char: ciphertext[count] = 'r'
            elif '2' == char: ciphertext[count] = 's'
            elif '1' == char: ciphertext[count] = 'x'
            count += 1
    else: # if no partial cipher, then it's a partial inversion, this code reverses that
        ciphertext.reverse()
        for char in ciphertext:
            if count % 2 == 0:
                if char == 'a': ciphertext[count] = 'z'
                elif char == 'b': ciphertext[count] = 'y'
                elif char == 'c': ciphertext[count] = 'x'
                elif char == 'd': ciphertext[count] = 'w'
                elif char == 'e': ciphertext[count] = 'v'
                elif char == 'f': ciphertext[count] = 'u'
                elif char == 'g': ciphertext[count] = 't'
                elif char == 'h': ciphertext[count] = 's'
                elif char == 'i': ciphertext[count] = 'r'
                elif char == 'j': ciphertext[count] = 'q'
                elif char == 'k': ciphertext[count] = 'p'
                elif char == 'l': ciphertext[count] = 'o'
                elif char == 'm': ciphertext[count] = 'n'
                elif char == 'n': ciphertext[count] = 'm'
                elif char == 'o': ciphertext[count] = 'l'
                elif char == 'p': ciphertext[count] = 'k'
                elif char == 'q': ciphertext[count] = 'j'
                elif char == 'r': ciphertext[count] = 'i'
                elif char == 's': ciphertext[count] = 'h'
                elif char == 't': ciphertext[count] = 'g'
                elif char == 'u': ciphertext[count] = 'f'
                elif char == 'v': ciphertext[count] = 'e'
                elif char == 'w': ciphertext[count] = 'd'
                elif char == 'x': ciphertext[count] = 'c'
                elif char == 'y': ciphertext[count] = 'b'
                elif char == 'z': ciphertext[count] = 'a'
            count += 1

    for n in range(loopthroughs):
        if loopthroughs > 1: # Removes the nonsense character at the beginning
            if (loopthroughs - n - 1) % 2 == 0:
                ciphertext.pop(0)
            else:
                ciphertext.pop(-1)
            len_ciphertext -= 1

        # Reverses the scramblings
        if len_ciphertext >= 2:
            if len_ciphertext % 2 == 0: # uncuts the deck if even cards
                ciphertext = ciphertext[len_ciphertext // 2:] + ciphertext[:len_ciphertext // 2]
            else: # uncuts the deck if odd cards
                ciphertext = ciphertext[len_ciphertext // 2 + 1:] + ciphertext[:len_ciphertext // 2 + 1]
            for i in range(len_ciphertext // 2):
                change = i * 2
                ciphertext[0 + change], ciphertext[1 + change] = ciphertext[1 + change], ciphertext[0 + change]

        if len_ciphertext >= 5:
            for i in range(len_ciphertext // 5):
                change = i * 5
                ciphertext[0 + change], ciphertext[4 + change] = ciphertext[4 + change], ciphertext[0 + change]
                ciphertext[1 + change], ciphertext[3 + change] = ciphertext[3 + change], ciphertext[1 + change]

        count = 0
        ciphertext = [letter.lower() for letter in ciphertext]
        for char in ciphertext:
            if len_ciphertext % 2 == 0: # Cipher one backwards
                if char == 'u': ciphertext[count] = 'E'
                elif char == 'g': ciphertext[count] = 'A'
                elif char == 's': ciphertext[count] = 'I'
                elif char == 'd': ciphertext[count] = 'O'
                elif char == 'a': ciphertext[count] = 'U'
                elif char == 'w': ciphertext[count] = 'B'
                elif char == 'm': ciphertext[count] = 'C'
                elif char == 'j': ciphertext[count] = 'D'
                elif char == 'k': ciphertext[count] = 'F'
                elif char == 'l': ciphertext[count] = 'G'
                elif char == 'z': ciphertext[count] = 'H'
                elif char == 'x': ciphertext[count] = 'J'
                elif char == 'c': ciphertext[count] = 'K'
                elif char == 'v': ciphertext[count] = 'L'
                elif char == 'r': ciphertext[count] = 'M'
                elif char == 'e': ciphertext[count] = 'N'
                elif char == 'f': ciphertext[count] = 'P'
                elif char == 't': ciphertext[count] = 'Q'
                elif char == 'i': ciphertext[count] = 'R'
                elif char == 'h': ciphertext[count] = 'S'
                elif char == 'o': ciphertext[count] = 'T'
                elif char == 'q': ciphertext[count] = 'V'
                elif char == 'y': ciphertext[count] = 'W'
                elif char == 'n': ciphertext[count] = 'X'
                elif char == 'p': ciphertext[count] = 'Y'
                elif char == 'b': ciphertext[count] = 'Z'
                else: ciphertext[count] = '?'
            else: # cipher two backwards
                if char == 'b': ciphertext[count] = 'E'
                elif char == 'x': ciphertext[count] = 'A'
                elif char == 'f': ciphertext[count] = 'I'
                elif char == 'l': ciphertext[count] = 'O'
                elif char == 'r': ciphertext[count] = 'U'
                elif char == 'y': ciphertext[count] = 'B'
                elif char == 'z': ciphertext[count] = 'C'
                elif char == 'a': ciphertext[count] = 'D'
                elif char == 'c': ciphertext[count] = 'F'
                elif char == 'd': ciphertext[count] = 'G'
                elif char == 'e': ciphertext[count] = 'H'
                elif char == 'g': ciphertext[count] = 'J'
                elif char == 'h': ciphertext[count] = 'K'
                elif char == 'i': ciphertext[count] = 'L'
                elif char == 'j': ciphertext[count] = 'M'
                elif char == 'k': ciphertext[count] = 'N'
                elif char == 'm': ciphertext[count] = 'P'
                elif char == 'n': ciphertext[count] = 'Q'
                elif char == 'o': ciphertext[count] = 'R'
                elif char == 'p': ciphertext[count] = 'S'
                elif char == 'q': ciphertext[count] = 'T'
                elif char == 's': ciphertext[count] = 'V'
                elif char == 't': ciphertext[count] = 'W'
                elif char == 'u': ciphertext[count] = 'X'
                elif char == 'v': ciphertext[count] = 'Y'
                elif char == 'w': ciphertext[count] = 'Z'
                else: ciphertext[count] = '?'

            count += 1

    return("".join(letter.upper() for letter in ciphertext)) # Turns ciphertext into upper incase loopthroughs = 0. This is for formatting purposes only


def nonzero_input(prompt:str):
    while True:    
        entry = input(prompt)
        entry = ''.join(letter for letter in entry if letter.isalpha() or letter in (',', '.', '_', '=', '+', '-', '~', '`', '0', '9', '8', '7', '6', '5', '4', '3', '2', '1'))
        if entry:
            return entry
        else:
            print('Please input something.')


while True:
    user_input = input('Would you like to encrypt or decrypt?("exit" to exit): ').upper().strip()
    if 'D' in user_input:
        print('Decrypted text: ', decrypt(nonzero_input('Ciphertext: '), int(nonzero_input('Cipher repititions: '))))
    elif 'N' in user_input:
        print('Encrypted text: ', encrypt(nonzero_input('Plaintext: '), int(nonzero_input('Cipher repititions: '))))
    elif 'EXIT' in user_input:
        quit()
    else:
        print('That is not a valid input.')