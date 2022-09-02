import sys
class Crypt:
    def __init__(self, key):
        self.key = key
    def encrypt(self, msg):
        msgList = list(msg)
        msglen = len(msgList)
        key = int(self.key)
        cipherText = ['']*msglen
        for i in range(msglen):
            OMsg = ord(msgList[i])
            newText = OMsg+key
            if newText > 90 and newText < 97:
                cipherText[i] = chr(65+(key-(90-OMsg)))
            elif newText > 122:
                cipherText[i] = chr(97+(key-(122-OMsg)))
            else:
                cipherText[i] = chr(newText)
        return ''.join(cipherText)
    def decrypt(self, msg):
        msgList = list(msg)
        msglen = len(msgList)
        key = int(self.key)
        plainText = ['']*msglen
        for i in range(msglen):
            OMsg = ord(msgList[i])
            newText = OMsg-key
            if newText > 90 and newText < 97:
                plainText[i] = chr(122-(key-(OMsg-90)))
            elif newText < 65:
                plainText[i] = chr(90+(key-(OMsg-65)))
            else:
                plainText[i] = chr(newText)
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