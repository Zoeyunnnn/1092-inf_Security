import hashlib
import sys

def check(str):
    for pw in pwlist:
        t = pw.encode()
        data = hashlib.sha256(t).hexdigest()
        if(data==str):
            return pw

pwlist = []
with open("10k most common.txt", "r") as file:
    for line in file:
        currentPlace = line[:-1] #從後面數來，取到換行\n前
        pwlist.append(currentPlace)

if len(sys.argv) == 2:
    msg = sys.argv[1].encode()
    hashvalue = hashlib.sha256(msg)
    print("sha256 result:",hashvalue1.hexdigest())
elif len(sys.argv) == 3:
    if(sys.argv[1] == '-c'):
        print("password(sha256):",check(sys.argv[2]))
