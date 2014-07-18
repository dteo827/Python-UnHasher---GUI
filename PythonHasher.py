#Created by David Teo, July 14, 2014
#GNU license or whatever can govern this script
import hashlib, os, sys
type_of_hash = input("Which hash do you want to use?\nmd5\nsha1\nsha224\nsha256\nsha284\nsha512?")
location = (os.path.dirname(os.path.abspath(sys.argv[0])))
directory_of_hashes = location, "/wordlist.txt" #input("Where is the password dictionary?")
directory_of_hashes = "".join(directory_of_hashes)
#fob = open("/Users/Zephyrus/Desktop/Python_Hasher/hash_dic.txt", "w")

if FileNotFoundError:
    new_file_location = location,"/hash_dic.txt"
    dir_for_new_file = "".join(new_file_location)
    open(dir_for_new_file, 'w')
    fob = open(dir_for_new_file, "w")

with open(directory_of_hashes) as f:
    password_list = f.read().splitlines()
if type_of_hash == "md5":
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
elif type_of_hash == "sha1":
    for word in password_list:
        write_word = word
        word = word.encode("utf-8")
        generated_hash = hashlib.sha1(word).hexdigest()
        print(generated_hash," = ", write_word)
        fob.write(generated_hash)
        fob.write(" = ")
        fob.write(write_word)
        fob.write("\n")
    else:
        fob.close()
        input("End of file")
elif type_of_hash == "sha224":
    for word in password_list:
        write_word = word
        word = word.encode("utf-8")
        generated_hash = hashlib.sha224(word).hexdigest()
        print(generated_hash," = ", write_word)
        fob.write(generated_hash)
        fob.write(" = ")
        fob.write(write_word)
        fob.write("\n")
    else:
        fob.close()
        input("End of file")
elif type_of_hash == "sha256":
    for word in password_list:
        write_word = word
        word = word.encode("utf-8")
        generated_hash = hashlib.sha256(word).hexdigest()
        print(generated_hash," = ", write_word)
        fob.write(generated_hash)
        fob.write(" = ")
        fob.write(write_word)
        fob.write("\n")
    else:
        fob.close()
        input("End of file")
elif type_of_hash == "sha384":
    for word in password_list:
        write_word = word
        word = word.encode("utf-8")
        generated_hash = hashlib.sha384(word).hexdigest()
        print(generated_hash," = ", write_word)
        fob.write(generated_hash)
        fob.write(" = ")
        fob.write(write_word)
        fob.write("\n")
    else:
        fob.close()
        input("End of file")
elif type_of_hash == "sha512":
    for word in password_list:
        write_word = word
        word = word.encode("utf-8")
        generated_hash = hashlib.sha512(word).hexdigest()
        print(generated_hash," = ", write_word)
        fob.write(generated_hash)
        fob.write(" = ")
        fob.write(write_word)
        fob.write("\n")
    else:
        fob.close()
        input("End of file")

#http://docs.python.org/2/library/hashlib.html#module-hashlib
