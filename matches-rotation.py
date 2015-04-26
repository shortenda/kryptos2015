# Check whether a string in stdin matches any possible rotation of the encrypted string
import sys

string_original = "---....--.--.---.-.-..-.---...-."
string_inverted = "....----..-..-...-.-..--.-...--.-.-"

string_flipped = string_original[::-1]

string = string_original

for line in sys.stdin:
    for i in range(0, len(string) - 1):
        rearranged = string[i : ] + string[0:i]
        if line.strip() == rearranged.strip():
            print line
