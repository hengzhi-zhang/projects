# File: Project3.py
# Student: Hengzhi Zhang
# UT EID: hz6984
# Course Name: CS303E
#
# Date: 11/21/2022
# Description of Program: This program allows the user to encrypt a text file of their choosing.

import random
import os.path

# A global constant defining the alphabet.
LETTERS = "abcdefghijklmnopqrstuvwxyz"

# You are welcome to use the following two auxiliary functions, or
# define your own.   They use some constructs we haven't covered.

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LETTERS.
    key = key.lower()
    return ( len(key) == 26 and all( [ ch in key for ch in LETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LETTERS.
    lst = list( LETTERS )    # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

def makeConversionDictionary( key1, key2 ):

    dict1 = {}
    x = 0
    for character in key1:
        dict1[character] = key2[x]
        x += 1

    return dict1

def makeDecryptionDictionary(key1, key2):

    dict2 = {}
    x = 0
    for char in key2:
        dict2[char] = key1[x]
        x += 1

    return dict2

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        """Create an instance of the cipher with stored key, which
        defaults to a randomly generated key."""
        ...
        self.key = key

    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)

    def getKey( self ):
        """Getter for the stored key."""
        ...
        return self.key

    def setKey( self, newKey ):
        """Setter for the stored key.  Check that it's a legal
        key."""
        ...
        if isLegalKey(newKey):
            self.key = newKey.lower()

    def encryptFile( self, inFile, outFile ):
        """Encrypt the contents of inFile using the stored key
        and write the results into outFile.  Assume inFile exists.
        """
        inf = open(inFile, "r")
        outf = open(outFile, "x")
        dic = makeConversionDictionary(LETTERS,self.getKey())

        l = inf.readline()
        while l:
            line = []
            for char in l:
                    if char.lower() in LETTERS:
                        if char.islower():
                            temp = dic[char]
                            line.append(temp)
                        else:
                            temp = dic[char.lower()].upper()
                            line.append(temp)
                    else:
                        temp = char
                        line.append(temp)
            outf.write("".join(line))
            l = inf.readline()
        inf.close()




    def decryptFile( self, inFile, outFile ):

        inf = open(inFile, "r")
        outf = open(outFile, "x")
        dic2 = makeDecryptionDictionary(LETTERS, self.getKey())

        l = inf.readline()
        while l:
            line = []
            for char in l:
                    if char.lower() in LETTERS:
                        if char.isupper():
                            temp = dic2[char.lower()].upper()
                            line.append(temp)
                        else:
                            temp = dic2[char]
                            line.append(temp)
                    else:
                        temp = char
                        line.append(temp)
            outf.write("".join(line))
            l = inf.readline()
        inf.close()

def main():

   cipher = SubstitutionCipher()

   while 1:
       query = input("Enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ")
       if query.lower() != "getkey" and query.lower() != "changekey" and query.lower() != "encryptfile" and query.lower() != "decryptfile" and query.lower() != "quit":
           print("Command not recognized. Try again! ")
           continue
       if query.lower() == "quit":
           print("Thanks for visiting!")
           break
       if query.lower() == "getkey":
            print("Current cipher key: " + cipher.getKey())

       if query.lower() == "changekey":
           change = input("Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
           if change.lower() == "quit":
               continue
           if change.lower() == "random":
               newKey = makeRandomKey()
               cipher.setKey(newKey)
               print("New cipher key: " + cipher.getKey())

           if change.lower() != "random" and change.lower() != "quit":
               if isLegalKey(change):
                    cipher.setKey(change)
                    print("New cipher key: " + cipher.getKey())
               if not isLegalKey(change):
                   flag = True
                   while flag:
                       print("Illegal key entered. Try again! ")
                       change = input("Enter a valid cypher key, 'random' for a random key, or 'quit' to quit: ")
                       if change.lower() == "quit":
                           flag = False
                           continue
                       if change.lower() == "random":
                           flag = False
                           newKey = makeRandomKey()
                           cipher.setKey(newKey)
                           print("New cipher key: " + cipher.getKey())
                       if isLegalKey(change):
                           flag = False
                           cipher.setKey(change)
                           print("New cipher key: " + cipher.getKey())



       if query.lower() == "encryptfile":
           filename = input("Enter a filename: ")
           fileExt = filename + ".txt"
           if os.path.isfile(fileExt):
               outfile = filename + "-Enc.txt"
               cipher.encryptFile(fileExt, outfile)
               print("The encrypted output filename is " + outfile)
           if not os.path.isfile(filename + ".txt"):
               print("File does not exist")
               continue


       if query.lower() == "decryptfile":
           newFileName = input("Enter a filename: ")
           fileExt2 = newFileName + ".txt"
           if not os.path.isfile(fileExt2):
               print("File does not exist")
               continue
           if os.path.isfile(fileExt2):
               outfile2 = newFileName + "-Dec.txt"
               cipher.decryptFile(fileExt2,outfile2)
               print("The decrypted output filename is " + outfile2)


main()