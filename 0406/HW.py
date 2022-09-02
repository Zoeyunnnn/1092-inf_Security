import hashlib
import sys

def check(str):
    for pw in pwlist:
        t = pw.encode()
        data = hashlib.sha1(t).hexdigest()
        data1 = hashlib.sha256(t).hexdigest()
        data2 = hashlib.sha512(t).hexdigest()
        data3 = hashlib.md5(t).hexdigest()
        if(data==str):
            print("password(sha1):",pw)
            break
        elif(data1==str):
            print("password(sha256):",pw)
            break
        elif(data2==str):
            print("password(sha512):",pw)
            break
        elif(data3==str):
            print("password(md5):",pw)
            break

pwlist = []
with open("10k most common.txt", "r") as file:
    for line in file:
        currentPlace = line[:-1] #從後面數來，取到換行\n前
        pwlist.append(currentPlace)

if len(sys.argv) == 2:
    msg = sys.argv[1].encode()
    hashvalue = hashlib.sha1(msg)
    hashvalue1 = hashlib.sha256(msg)
    hashvalue2 = hashlib.sha512(msg)
    hashvalue3 = hashlib.md5(msg)
    print("sha1 result:",hashvalue.hexdigest())
    print("sha256 result:",hashvalue1.hexdigest())
    print("sha512 result:",hashvalue2.hexdigest())
    print("md5 result:",hashvalue3.hexdigest())
elif len(sys.argv) == 3:
    if(sys.argv[1] == '-c'):
        check(sys.argv[2])