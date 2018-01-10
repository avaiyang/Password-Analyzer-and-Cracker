import sys

def wordlist():
    inp = open('input.txt', 'r', encoding='utf-8')
    y=[]
    
    for line in inp.read().splitlines():
        y.append(line)                          #to assign the words from the wordlist file to list y
    return(y)

def password():
    out = open('password.file','r', encoding='ISO-8859-1')
    z=[]
    for line2 in out.read().splitlines():
        z.append(line2)                         #assinging the line from the password dump to list z
    return(z)

def main():
    a = wordlist()                              #assigning the value from the wordlist to a
    b = password()                              #assigning the value from the password dump to b
    
    for r in range(len(a)):                     #traversing the list a
        for s in range(len(b)):                 #traversing the list b
            c = b[s].split(':', 2)              #assigning the password value from password dump to c
            if(a[r] in c):                      #comparing the passwords from the dump and the wordlist
                sys.stdout = open('Password_Cracked.txt','a',encoding='utf-8')
                print(b[s].split(':',1)[-1], ':', a[r])          #printing the email-id and the password
                sys.stdout.close()
                break                           #using break in order to remove the multiple ids with same passwords
    
if __name__=='__main__':main()
