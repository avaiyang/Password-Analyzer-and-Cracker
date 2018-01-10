import hashlib
import sys
    
def wordlist():
    inp = open('input.txt', 'r', encoding='utf-8' )
    x = []                                          #creating new lists, x, y
    y = []
    z = '00000'                                     #assigning the variable z the value 000000
    
    for line in inp.read().splitlines():            #converting the wordlist into hash SHA1
        c_hash = hashlib.sha1()
        c_hash.update((line).encode('utf-8'))
        q = c_hash.hexdigest()
        q = z + q[5:].strip()                       #Replacing the first 5 characters of the hash to 00000, since those hash value are cracked 
        x.append(q)                                 
        y.append(line)
    return(x,y)

def password():
    out = open('SHA1.txt','r', encoding='utf-8')
    z=[]
    for line2 in out.read().splitlines():
        z.append(line2)                             #assinging the line from the password dump to list z
    return(z)

def main():
    a,b=wordlist()                                  #assigning the value from the wordlist to a and b
    c=password()                                    #assigning the value from the password dump to c
    
    for r in range(len(a)):                         #traversing the list a
        for s in range(len(c)):
            if(a[r]==c[s]):                         #comparing the passwords in hash format from the dump and the wordlist
                sys.stdout = open('Password_Cracked.txt','a',encoding='utf-8')
                print(c[s],':', b[r])               #printing the hash value along with the actual password
                sys.stdout.close()
                break
    
if __name__=='__main__':main()