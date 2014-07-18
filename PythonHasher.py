#Created by David Teo, July 14, 2014
#GNU license or whatever can govern this script
import hashlib
directory_of_hashes = "/Users/Zephyrus/Desktop/Python_Hasher/wordlist.txt" #input("Where is the password dictionary?")
fob = open("/Users/Zephyrus/Desktop/Python_Hasher/hash_dic.txt", "w")
with open(directory_of_hashes) as f:
    password_list = f.read().splitlines()

for word in password_list:
    write_word = word
    word = word.encode("utf-8")
    generated_hash = hashlib.md5(word).hexdigest()
    print(generated_hash," = ", write_word)
    fob.write(generated_hash)
    fob.write(" = ")
    fob.write(write_word)
    fob.write("\n")
else:
    fob.close()
    input("End of file")

#http://docs.python.org/2/library/hashlib.html#module-hashlib
