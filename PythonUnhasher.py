#Created by David Teo, July 15, 2014
#GNU license or whatever can govern this script
import hashlib, os, sys
we_all_good = True
print("""         ############################################################
         #############  Welcome to Python Decrypter #################
         ############################################################
         #############  Place your wordlist.txt &   #################
         #############  hashlist.txt in the same    #################
         #############  directory as this program   #################
         ############################################################""" )
type_of_hash = input("Which hash do you want to use?\nmd5\nsha1\nsha224\nsha256\nsha284\nsha512?")
hash_to_encrypt_list = "hasher", type_of_hash
hash_to_encrypt = "".join(hash_to_encrypt_list)
location = (os.path.dirname(os.path.abspath(sys.argv[0])))
def hashermd5(word):
    word = word.encode("utf-8")
    generated_hash = hashlib.md5(word).hexdigest()
    return generated_hash
def hashersha1(word):
    word = word.encode("utf-8")
    generated_hash = hashlib.sha1(word).hexdigest()
    return generated_hash
def hashersha224(word):
    word = word.encode("utf-8")
    generated_hash = hashlib.sha224(word).hexdigest()
    return generated_hash
def hashersha256(word):
    word = word.encode("utf-8")
    generated_hash = hashlib.sha256(word).hexdigest()
    return generated_hash
def hashersha512(word):
    word = word.encode("utf-8")
    generated_hash = hashlib.sha512(word).hexdigest()
    return generated_hash

#Forming wordlist list, then closing the file
location_of_wordlist = location,"/wordlist.txt"
directory_of_wordlist = "".join(location_of_wordlist)
fob = open(directory_of_wordlist, "r")
with open(directory_of_wordlist) as f:
     word_list = f.read().splitlines()
fob.close()

#Forming the hashlist, but keeping it open
location_of_hashlist = location,"/hashlist.txt"
directory_of_hashlist = "".join(location_of_hashlist)
fob = open(directory_of_hashlist, "r")
with open(directory_of_hashlist) as opendir:
     hash_list = opendir.read().splitlines()

#Hashes a word in the wordlist and compares it to the list of hashes to be decrypted
#if the hash of the word is the same to a hash in the dictionary, the results ar printed
hash_type = "hasher",type_of_hash,"()"
hash_type = "".join(hash_type)
print(hash_type)

#indexing through input and pointing to connection function. Could be done better, but I dont know how.
if type_of_hash == "md5":
    for word in word_list:
        hashed_word = hashermd5(word)
        if hashed_word in hash_list:
            print("Hash Decoded!", hashed_word, " = ", word)
        else:
            print("'",word,"'", "not in dictionary")
    else:
        fob.close()
        input("Known hashes have been decrypted, press the enter key to exit")
elif type_of_hash == "sha1":
    for word in word_list:
        hashed_word = hashersha1(word)
        if hashed_word in hash_list:
            print("Hash Decoded!", hashed_word, " = ", word)
        else:
            print("'",word,"'", "not in dictionary")
    else:
        fob.close()
        input("Known hashes have been decrypted, press the enter key to exit")
elif type_of_hash == "sha224":
    for word in word_list:
        hashed_word = hashersha224(word)
        if hashed_word in hash_list:
            print("Hash Decoded!", hashed_word, " = ", word)
        else:
            print("'",word,"'", "not in dictionary")
    else:
        fob.close()
        input("Known hashes have been decrypted, press the enter key to exit")
elif type_of_hash == "sha256":
    for word in word_list:
        hashed_word = hashersha256(word)
        if hashed_word in hash_list:
            print("Hash Decoded!", hashed_word, " = ", word)
        else:
            print("'",word,"'", "not in dictionary")
    else:
        fob.close()
        input("Known hashes have been decrypted, press the enter key to exit")
elif type_of_hash == "sha2512":
    for word in word_list:
        hashed_word = hashersha512(word)
        if hashed_word in hash_list:
            print("Hash Decoded!", hashed_word, " = ", word)
        else:
            print("'",word,"'", "not in dictionary")
    else:
        fob.close()
        input("Known hashes have been decrypted, press the enter key to exit")
else:
     input("\nInvalid hash type it can only be\nmd5\nsha1\nsha224\nsha256\nsha284\nsha512\nPlease restart the program")
