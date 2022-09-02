#Hash function use sha256
import hashlib
import sys

if len(sys.argv) > 1:
    msg = sys.argv[1].encode() #to byte
    hashvalue = hashlib.sha256(msg)
    hashvalue2 = hashlib.md5(msg)
    print(hashvalue)
    print(hashvalue.hexdigest()) #use upper() more clear
    print(hashvalue2.hexdigest())