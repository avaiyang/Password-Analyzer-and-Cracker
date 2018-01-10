import hashlib
import sys
    
def wordlist():
    inp = open('input.txt', 'r', encoding='utf-8' )     #opening the file containing the wordlist
    x = []
    y = []
    w = []
    z = [str(x).zfill(2) for x in range(100)]           #zfill argument is used to create two digit integers, ranging from 00 - 99
    
    for line in inp.read().splitlines():
        for i in z:                                     #iterating the salt value ranging from 00 - 99
            line12 = i + line                           #adding salt value at the begining the wordlist
            c_hash = hashlib.sha256()                   #converting the wordlist to SHA256
            c_hash.update((line12).encode('utf-8'))
            q = c_hash.hexdigest()              
            w.append(i)                                 #adding the values to a list
            x.append(q)
            y.append(line)
    return(x,y,w)

def password():
    out = open('formspring.txt','r', encoding='utf-8')
    z=[]
    for line2 in out.read().splitlines():               
        z.append(line2)                                 #assinging the hash value from the password dump to list z
    return(z)

def main():
    a,b,d=wordlist()                                    #assigning the value from the wordlist to a,b and d
    c=password()                                        #assigning the value from the password dump to c
    
    for r in range(len(a)):
        for s in range(len(c)):
            if(a[r]==c[s]):                             #comparing the passwords in hash format from the dump and the wordlist
                sys.stdout = open('password_cracked.txt','a',encoding='utf-8')
                print(c[s], ':', b[r],':',  'salt =', d[r],)     #printing the hash value along with the actual password and the salt value
                sys.stdout.close()
                break
    
if __name__=='__main__':main()