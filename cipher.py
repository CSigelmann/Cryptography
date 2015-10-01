import sys

__author__ = 'Casey Sigelmann'

ARG_CIPHER_TYPE = 1
ARG_TEXT = 4
ARG_ADDITIVE_KEY = 3
ARG_MULTIPLICATIVE_KEY = 2
multiplicative_inverses = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 23, 23: 17, 25: 25}
alphabet_to_int = {}
int_to_alphabet = {}
usage = "Usage: python cipher.py <cipher_type> [<multiplicative_key> <additive_key>] <text>\n" \
        "Options for cypher_type:\n" \
        "    encipher_affine\n" \
        "    decipher_affine\n"
affine_usage = "Usage for *_affine: python cipher.py encipher_affine <multiplicative_key> <additive_key> <text>"
print_all_usage = "Usage for print_all_affine: python cipher.py print_all_affine <text>"

# Initialize alphabet_mapping by converting characters to numerical representations.
# Iterate over lowercase characters.
# Should result in 'a': 1, 'b': 2, ..., 'y': 25, 'z': 0
for i in range(1, 27):
    alphabet_to_int[chr(i + 96)] = i % 26
    int_to_alphabet[i % 26] = chr(i + 96)


############################################
#          ENCIPHERING FUNCTIONS           #
############################################


##
# encipher_affine
#
# Description: Monoalphabetic cipher that is a combination of multiplicative and
#     additive ciphers. This does not check validity of inputs.
#
# Parameters:
#     multiplicative_key - An integer key for the multiplicative part of the cipher
#     additive_key - An integer key for the additive part of the cipher
#     text - the plain text that is to be enciphered
#
# Returns: A string of the cipher text
##

def encipher_affine(multiplicative_key, additive_key, text):
    current_cipher_text = ""
    for char in text:
        char_rep = alphabet_to_int[char]
        char_rep += additive_key
        char_rep *= multiplicative_key
        char_rep %= 26
        current_cipher_text += int_to_alphabet[char_rep]
    return current_cipher_text


##
# decipher_affine
#
# Description: Deciphers text that was encrypted using an affine cipher. This
#     does not check validity of inputs.
#
# Parameters:
#     multiplicative_key - An integer key that was used to encipher the message
#     additive_key - An integer key that was used to encipher the message
#     text - The cipher text to be deciphered
#
# Returns: A string of the plain text resulting from deciphering
##
def decipher_affine(multiplicative_key, additive_key, text):
    current_plain_text = ""
    for char in text:
        char_rep = alphabet_to_int[char]
        char_rep *= multiplicative_inverses[multiplicative_key]
        char_rep -= additive_key
        char_rep %= 26
        current_plain_text += int_to_alphabet[char_rep]
    return current_plain_text


##
# print_all_affine
#
# Description: Prints the results of decrypting an affine cipher for all possible keys.
#
# Parameters:
#     text - The cipher text to be deciphered
##
def print_all_affine(text):
    for s in range(1, 26, 2):
        if s == 13:
            continue
        for r in range(0, 26):
            print decipher_affine(s, r, text), s, r, "\n"
            

############################################
#             CODE EXECUTION               #
############################################


# decide which cipher to use
if sys.argv[ARG_CIPHER_TYPE] == "encipher_affine":
    if len(sys.argv) != 5:
        print affine_usage
        exit()
    mKey = int(sys.argv[ARG_MULTIPLICATIVE_KEY])
    aKey = int(sys.argv[ARG_ADDITIVE_KEY])
    plain_text = sys.argv[ARG_TEXT].lower()
    output_text = encipher_affine(mKey, aKey, plain_text)
    print "Output Text: ", output_text
elif sys.argv[ARG_CIPHER_TYPE] == "decipher_affine":
    if len(sys.argv) != 5:
        print affine_usage
        exit()
    mKey = int(sys.argv[ARG_MULTIPLICATIVE_KEY])
    aKey = int(sys.argv[ARG_ADDITIVE_KEY])
    cipher_text = sys.argv[ARG_TEXT].lower()
    output_text = decipher_affine(mKey, aKey, cipher_text)
    print "Output Text: ", output_text
elif sys.argv[ARG_CIPHER_TYPE] == "print_all_affine":
    if len(sys.argv) != 3:
        print print_all_usage
        exit()
    print_all_affine(sys.argv[2].lower())
else:
    print usage
    exit()
