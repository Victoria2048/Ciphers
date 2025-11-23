def encrypt():
    plaintext = list(input('Plaintext: ').strip().lower().replace(' ', '').replace(',', '').replace("'", '').replace('.', ''))
    len_plaintext = len(plaintext)

    def encryption_bit():
        count = 0
        for char in plaintext:
            if count % 4 == 0:
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
            elif count % 4 == 1:
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
            elif count % 4 == 2:
                if char == 'a': plaintext[count] = 'Z'
                elif char == 'b': plaintext[count] = 'Y'
                elif char == 'c': plaintext[count] = 'X'
                elif char == 'd': plaintext[count] = 'W'
                elif char == 'e': plaintext[count] = 'V'
                elif char == 'f': plaintext[count] = 'U'
                elif char == 'g': plaintext[count] = 'T'
                elif char == 'h': plaintext[count] = 'S'
                elif char == 'i': plaintext[count] = 'R'
                elif char == 'j': plaintext[count] = 'Q'
                elif char == 'k': plaintext[count] = 'P'
                elif char == 'l': plaintext[count] = 'O'
                elif char == 'm': plaintext[count] = 'N'
                elif char == 'n': plaintext[count] = 'M'
                elif char == 'o': plaintext[count] = 'L'
                elif char == 'p': plaintext[count] = 'K'
                elif char == 'q': plaintext[count] = 'J'
                elif char == 'r': plaintext[count] = 'I'
                elif char == 's': plaintext[count] = 'H'
                elif char == 't': plaintext[count] = 'G'
                elif char == 'u': plaintext[count] = 'F'
                elif char == 'v': plaintext[count] = 'E'
                elif char == 'w': plaintext[count] = 'D'
                elif char == 'x': plaintext[count] = 'C'
                elif char == 'y': plaintext[count] = 'B'
                elif char == 'z': plaintext[count] = 'A'
                else: plaintext[count] = '?'
            else:
                if char == 'a': plaintext[count] = 'Y'
                elif char == 'b': plaintext[count] = 'X'
                elif char == 'c': plaintext[count] = 'W'
                elif char == 'd': plaintext[count] = 'V'
                elif char == 'e': plaintext[count] = 'U'
                elif char == 'f': plaintext[count] = 'T'
                elif char == 'g': plaintext[count] = 'S'
                elif char == 'h': plaintext[count] = 'R'
                elif char == 'i': plaintext[count] = 'Q'
                elif char == 'j': plaintext[count] = 'P'
                elif char == 'k': plaintext[count] = 'O'
                elif char == 'l': plaintext[count] = 'N'
                elif char == 'n': plaintext[count] = 'L'
                elif char == 'o': plaintext[count] = 'K'
                elif char == 'p': plaintext[count] = 'J'
                elif char == 'q': plaintext[count] = 'I'
                elif char == 'r': plaintext[count] = 'H'
                elif char == 's': plaintext[count] = 'G'
                elif char == 't': plaintext[count] = 'F'
                elif char == 'u': plaintext[count] = 'E'
                elif char == 'v': plaintext[count] = 'D'
                elif char == 'w': plaintext[count] = 'C'
                elif char == 'x': plaintext[count] = 'B'
                elif char == 'y': plaintext[count] = 'A'
                else: plaintext[count] = '?'
            count += 1

        if len_plaintext >= 5:
            for i in range(len_plaintext // 5):
                change = i * 5
                plaintext[0 + change], plaintext[4 + change] = plaintext[4 + change], plaintext[0 + change]
                plaintext[1 + change], plaintext[3 + change] = plaintext[3 + change], plaintext[1 + change]

        if len_plaintext >= 2:
            for i in range(len_plaintext // 2):
                change = i * 2
                plaintext[0 + change], plaintext[1 + change] = plaintext[1 + change], plaintext[0 + change]

        if len_plaintext >= 3:
            plaintext[0], plaintext[-1] = plaintext[-1], plaintext[0]

    encryption_bit()
    slicy_chunk = len_plaintext + 1
    double_plaintext = 2 * plaintext
    plaintext = list("".join(double_plaintext[1:slicy_chunk]).lower())
    encryption_bit()

    plaintext = list("".join(plaintext).lower())
    count = 0
    for char in plaintext:
        if char == 'e': plaintext[count] = 'A'
        elif char == 'a': plaintext[count] = 'N'
        elif char == 'i': plaintext[count] = 'H'
        elif char == 'o': plaintext[count] = 'J'
        elif char == 'u': plaintext[count] = 'G'
        elif char == 'b': plaintext[count] = 'R'
        elif char == 'c': plaintext[count] = 'W'
        elif char == 'd': plaintext[count] = 'Z'
        elif char == 'f': plaintext[count] = 'X'
        elif char == 'g': plaintext[count] = 'C'
        elif char == 'h': plaintext[count] = 'V'
        elif char == 'j': plaintext[count] = 'B'
        elif char == 'k': plaintext[count] = 'I'
        elif char == 'l': plaintext[count] = 'O'
        elif char == 'm': plaintext[count] = 'Y'
        elif char == 'n': plaintext[count] = 'T'
        elif char == 'p': plaintext[count] = 'U'
        elif char == 'q': plaintext[count] = 'K'
        elif char == 'r': plaintext[count] = 'S'
        elif char == 's': plaintext[count] = 'M'
        elif char == 't': plaintext[count] = 'D'
        elif char == 'v': plaintext[count] = 'E'
        elif char == 'w': plaintext[count] = 'L'
        elif char == 'x': plaintext[count] = 'Q'
        elif char == 'y': plaintext[count] = 'F'
        elif char == 'z': plaintext[count] = 'P'
        count += 1

    plaintext = "".join(plaintext)
    print('Ciphertext: ', plaintext.upper())


def decrypt():
    ciphertext = list(input('Ciphertext: ').strip().lower())
    len_ciphertext = len(ciphertext)

    def decryption_bit():
        if len_ciphertext >= 3:
            ciphertext[0], ciphertext[-1] = ciphertext[-1], ciphertext[0]

        if len_ciphertext >= 2:
            for i in range(len_ciphertext // 2):
                change = i * 2
                ciphertext[0 + change], ciphertext[1 + change] = ciphertext[1 + change], ciphertext[0 + change]

        if len_ciphertext >= 5:
            for i in range(len_ciphertext // 5):
                change = i * 5
                ciphertext[0 + change], ciphertext[4 + change] = ciphertext[4 + change], ciphertext[0 + change]
                ciphertext[1 + change], ciphertext[3 + change] = ciphertext[3 + change], ciphertext[1 + change]

        count = 0
        for char in ciphertext:
            if count % 4 == 0:
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
            elif count % 4 == 1:
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
            elif count % 4 == 2:
                if char == 'a': ciphertext[count] = 'Z'
                elif char == 'b': ciphertext[count] = 'Y'
                elif char == 'c': ciphertext[count] = 'X'
                elif char == 'd': ciphertext[count] = 'W'
                elif char == 'e': ciphertext[count] = 'V'
                elif char == 'f': ciphertext[count] = 'U'
                elif char == 'g': ciphertext[count] = 'T'
                elif char == 'h': ciphertext[count] = 'S'
                elif char == 'i': ciphertext[count] = 'R'
                elif char == 'j': ciphertext[count] = 'Q'
                elif char == 'k': ciphertext[count] = 'P'
                elif char == 'l': ciphertext[count] = 'O'
                elif char == 'm': ciphertext[count] = 'N'
                elif char == 'n': ciphertext[count] = 'M'
                elif char == 'o': ciphertext[count] = 'L'
                elif char == 'p': ciphertext[count] = 'K'
                elif char == 'q': ciphertext[count] = 'J'
                elif char == 'r': ciphertext[count] = 'I'
                elif char == 's': ciphertext[count] = 'H'
                elif char == 't': ciphertext[count] = 'G'
                elif char == 'u': ciphertext[count] = 'F'
                elif char == 'v': ciphertext[count] = 'E'
                elif char == 'w': ciphertext[count] = 'D'
                elif char == 'x': ciphertext[count] = 'C'
                elif char == 'y': ciphertext[count] = 'B'
                elif char == 'z': ciphertext[count] = 'A'
            else:
                if char == 'a': ciphertext[count] = 'Y'
                elif char == 'b': ciphertext[count] = 'X'
                elif char == 'c': ciphertext[count] = 'W'
                elif char == 'd': ciphertext[count] = 'V'
                elif char == 'e': ciphertext[count] = 'U'
                elif char == 'f': ciphertext[count] = 'T'
                elif char == 'g': ciphertext[count] = 'S'
                elif char == 'h': ciphertext[count] = 'R'
                elif char == 'i': ciphertext[count] = 'Q'
                elif char == 'j': ciphertext[count] = 'P'
                elif char == 'k': ciphertext[count] = 'O'
                elif char == 'l': ciphertext[count] = 'N'
                elif char == 'n': ciphertext[count] = 'L'
                elif char == 'o': ciphertext[count] = 'K'
                elif char == 'p': ciphertext[count] = 'J'
                elif char == 'q': ciphertext[count] = 'I'
                elif char == 'r': ciphertext[count] = 'H'
                elif char == 's': ciphertext[count] = 'G'
                elif char == 't': ciphertext[count] = 'F'
                elif char == 'u': ciphertext[count] = 'E'
                elif char == 'v': ciphertext[count] = 'D'
                elif char == 'w': ciphertext[count] = 'C'
                elif char == 'x': ciphertext[count] = 'B'
                elif char == 'y': ciphertext[count] = 'A'
                else: ciphertext[count] = '?'
            count += 1

    count = 0
    for char in ciphertext:
        if char == 'a': ciphertext[count] = 'E'
        elif char == 'n': ciphertext[count] = 'A'
        elif char == 'h': ciphertext[count] = 'I'
        elif char == 'j': ciphertext[count] = 'O'
        elif char == 'g': ciphertext[count] = 'U'
        elif char == 'r': ciphertext[count] = 'B'
        elif char == 'w': ciphertext[count] = 'C'
        elif char == 'z': ciphertext[count] = 'D'
        elif char == 'x': ciphertext[count] = 'F'
        elif char == 'c': ciphertext[count] = 'G'
        elif char == 'v': ciphertext[count] = 'H'
        elif char == 'b': ciphertext[count] = 'J'
        elif char == 'i': ciphertext[count] = 'K'
        elif char == 'o': ciphertext[count] = 'L'
        elif char == 'y': ciphertext[count] = 'M'
        elif char == 't': ciphertext[count] = 'N'
        elif char == 'u': ciphertext[count] = 'P'
        elif char == 'k': ciphertext[count] = 'Q'
        elif char == 's': ciphertext[count] = 'R'
        elif char == 'm': ciphertext[count] = 'S'
        elif char == 'd': ciphertext[count] = 'T'
        elif char == 'e': ciphertext[count] = 'V'
        elif char == 'l': ciphertext[count] = 'W'
        elif char == 'q': ciphertext[count] = 'X'
        elif char == 'f': ciphertext[count] = 'Y'
        elif char == 'p': ciphertext[count] = 'Z'
        count += 1

    ciphertext = list("".join(ciphertext).lower())
    decryption_bit()
    slicy_chunk = len_ciphertext - 1
    double_ciphertext = 2 * ciphertext
    ciphertext = list("".join(double_ciphertext[slicy_chunk:-1]).lower())
    decryption_bit()



    ciphertext = "".join(ciphertext)
    print('Decrypted text: ', ciphertext.upper())


while True:
    decryptencrypt = input('Would you like to encrypt or decrypt?("exit" to exit): ').upper().strip()
    if 'D' in decryptencrypt:
        decrypt()
    elif 'N' in decryptencrypt:
        encrypt()
    elif 'EXIT' in decryptencrypt:
        quit()
    else:
        print('That is not a valid input.')
