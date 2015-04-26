sentence = "NACZ AOGIOUK CNMPB ZOGONMM CVH VSZK HTSUC NMHIZYZHQF MDMEGQ MMOBNL RZBET QYV FTET QLIQZ NTWO"

must_match = {}

for word_index, word in enumerate(sentence.split(" ")):
    word_index = word_index + 1
    for letter_index, letter in enumerate(word):
        letter_index = letter_index + 1
        shift = letter_index + word_index
        unique_pair = (shift, letter)
        if unique_pair in must_match:
            must_match[unique_pair].append((word, letter_index))
        else:
            must_match[unique_pair] = [(word, letter_index)]

for key, value in must_match.items():
    if len(value) > 2:
        print "key %s value %s" % (key, value)
