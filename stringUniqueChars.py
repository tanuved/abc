'''
Problem: Determine if a string has all unique chars

Tanay Ved
2014

'''

def addAndTestStringWithDictionary(stringToTest):
    dictionary = {}
    for char in stringToTest:
        cint = ord(char)
        if char in d.values():
            print False
            break
        d[cint] = char
    print True

def main():
    userString = raw_input ("Enter a string to test: ")
    addAndTestStringWithDictionary(userString)
main()
