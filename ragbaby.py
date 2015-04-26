import sys
plaintext_alphabet = [letter for letter in "abcdefghiklmnopqrstuvwyz".upper()]

def array_get_wrapping(array, index):
    return array[index % len(array)]

def get_cypher_alphabet(key):
    cypher_alphabet = [letter for letter in plaintext_alphabet]
    key_set = set()
    key_unique = ""

    try:
        for letter in key:
            if letter not in key_set:
                key_unique += letter
                key_set.add(letter)
                cypher_alphabet.remove(letter)
    except ValueError:
        pass

    cypher_alphabet = [letter for letter in key_unique] + cypher_alphabet
    return cypher_alphabet

def encrypt(key, plaintext):
    cyphertext = ""
    cypher_alphabet = get_cypher_alphabet(key)
    cypher_search = {letter : letter_index for
                    (letter_index, letter) in enumerate(cypher_alphabet)}

    for word_index, word in enumerate(plaintext.split(" ")):
        for letter_index, letter in enumerate(word):
            cypher_index = cypher_search[letter] + word_index + letter_index + 1
            cyphertext += array_get_wrapping(cypher_alphabet, cypher_index)
        cyphertext += " "

    return cyphertext.strip()

def decrypt(key, cyphertext):
    plaintext = ""
    cypher_alphabet = get_cypher_alphabet(key)
    cypher_search = {letter : letter_index for
                    (letter_index, letter) in enumerate(cypher_alphabet)}

    for word_index, word in enumerate(cyphertext.split(" ")):
        for letter_index, letter in enumerate(word.strip()):
            plain_index = cypher_search[letter] - word_index - (letter_index + 1)
            plaintext += array_get_wrapping(cypher_alphabet, plain_index)
        plaintext += " "

    return plaintext

plaintext = sys.stdin.readline().strip().upper()

for key in sys.stdin:
    key = key.strip().upper().replace("'", "")
    if encrypt(key, plaintext) == "NACZ":
        print key
        print decrypt(key, """
NACZ AOGIOUK CNMPB ZOGONMM CVH VSZK HTSUC NMHIZYZHQF MDMEGQ MMOBNL RZBET QYV FTET QLIQZ NTWO
""")

