import sys

class Crypt:
    def __init__(self, key):
        self.key = key
    def encrypt(self, msg):
        msglist = list(msg)
        msglen = len(msg)
        keylist = list(key)
        keylen = len(key)
        cText = ['']*msglen
        for i in range(msglen):
            cText[i] = chr(ord(msglist[i]) ^ ord(keylist[i % keylen]))
        return ''.join(cText)
    def decrypt(self, msg):
        msgList = list(msg)
        msglen = len(msgList)
        keyList = list(self.key) 
        keylen = len(keyList)
        plainText = ['']*msglen

if __name__ == '__main__':
    if len(sys.argv) > 2:
        if sys.argv[1] == '-e':
            p = Crypt(sys.argv[2])
            print(p.encrypt(sys.argv[3]))
        else:
            p = Crypt(sys.argv[2])
            print(p.decrypt(sys.argv[3]))

