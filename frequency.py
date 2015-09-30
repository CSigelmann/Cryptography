import sys

__author__ = 'Casey Sigelmann'

letter_frequencies = {}
digraph_frequencies = {}
usage = "Usage: python frequency.py <text>\n"

if len(sys.argv) != 2:
    print usage
    exit()

text = sys.argv[1]
for i in range(0, len(text)):
    char = text[i]
    if char not in letter_frequencies:
        letter_frequencies[char] = 1
    else:
        letter_frequencies[char] += 1

    if i+1 != len(text):
        digraph = text[i] + text[i+1]
        if digraph not in digraph_frequencies:
            digraph_frequencies[digraph] = 1
        else:
            digraph_frequencies[digraph] += 1

print "Letter Frequencies:"
for letter in letter_frequencies:
    print "     ", letter, ": ", letter_frequencies[letter]
print "Digraph Frequencies:"
for digraph in digraph_frequencies:
    print "     ", digraph, ": ", digraph_frequencies[digraph]