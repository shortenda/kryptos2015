#tries to find a brute force solution to problem 2
import sys

string_original = "---....--.--.---.-.-..-.---...-."

morsetab = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        ' ': ' ',
}

morse_to_letter = {value: key for key, value in morsetab.items()}

worked = []

def letterify(sequence, string):
    if len(string) == 0:
        worked.append(sequence)

    for morse, letter in morse_to_letter.items():
        if string.startswith(morse):
            seq_copy = str([letter for letter in sequence])
            seq_copy += letter
            letterify(seq_copy, string[len(morse) : ])

    return False

letterify("", string_original)
