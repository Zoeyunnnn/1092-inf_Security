import sys
import random as rand
class RSA:
    def __init__(self):
        print(self.getRandList())
        self.p, self.q = map(int, input("p,q:").split(","))
        self.N = self.p*self.q
        self.N1 = (self.p-1)*(self.q-1)
        #找出跟N1互質的e之列表供選擇(5個)
        print(self.getElist(self.N1))
        self.e = int(input("choose 'e':")) 
        #找出跟e互質的d之列表供選擇(5個)
        print(self.getElist(self.e))
        self.d = int(input("choose 'd':"))
        x,msg = input("function,msg:").split(",")
        if x == 'e':
            self.encrypt(int(msg))
        else :
            self.decrypt(int(msg))
    def encrypt(self, M):
        print("Encrypt：",(M**self.e)%self.N)
    def decrypt(self, C):
        print("Decrypt：",(C**self.d)%self.N)
    def getRandList(self):
        list=[]
        while len(list)<5:
            i = rand.randint(1024,65536)
            if i%2!=0:
                list.append(i)
        return list
    def getElist(self,N1):
        data=[]
        while len(data)<5:
            i = int(10*rand.random()+1)
            if (self.setPrime(N1,i)):
                data.append(i)
        return data
    def setPrime(self,N1,i):
        maxV = max(N1,i)
        minV = min(N1,i)
        if maxV%minV == 1:
            return True
        elif maxV%minV == 0:
            return False
        else :
            return self.setPrime(minV,maxV%minV)
if __name__ == '__main__':
    print(sys.argv)
    RSA()
    #print(rsa.fun(int(sys.argv[1]),int(sys.argv[2])))
    if len(sys.argv)>3:
        if sys.argv[1] == '-e':
            r = RSA(sys.argv[2])
            print(r.encrypt(sys.argv[3]))
        elif sys.argv[1] == '-d':
            r = RSA(sys.argv[2])
            print(r.decrypt(sys.argv[3]))