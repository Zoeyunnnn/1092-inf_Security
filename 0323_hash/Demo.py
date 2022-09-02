import sys
class Crypt:
    def __init__(self, key):
        self.key = key
    def encrypt(self, msg):
        msgList = list(msg)
        msglen = len(msgList)
        keyList = list(self.key)
        keylen = len(keyList)
        cipherText = ['']*msglen     #加密後字串，弄成和msg一樣長度
        for i in range(msglen):
            cipherText[i] = chr(ord(msgList[i]) ^ ord(keyList[i % keylen]))
        return ''.join(cipherText)
    def decrypt(self, msg): #解密時msg是原文 
        msgList = list(msg)
        msglen = len(msgList)
        keyList = list(self.key) 
        keylen = len(keyList)
        plainText = ['']*msglen
        for i in range(msglen):
            plainText[i] = chr(ord(msgList[i]) ^ ord(keyList[i % keylen]))
        return ''.join(plainText)

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv)>2:
        if sys.argv[1] == '-e':
            c = Crypt(sys.argv[2])
            print(c.encrypt(sys.argv[3]))
        elif sys.argv[1] == '-d':
            c = Crypt(sys.argv[2])
            print(c.decrypt(sys.argv[3]))