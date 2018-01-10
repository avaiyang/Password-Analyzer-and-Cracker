# Password-Analyzer-and-Cracker
## Note
`This is only for the educational purpose. Cracking passwords is illegal and not recommended`

## Description
In my Information Security and Privacy coursework, we were given a task to crack passwords for the given set of password dumps. 
These password dumps included leaked user data from the Yahoo, Linkedin and Formspring website, which were encrypted in the plaintext,  SHA-1 and SHA-256 respectively.

### Yahoo
The file consisted of plaintext, where by the user password were in the plaintext format. The idea behind this was to extract only the passwords from the file, analyze it and develop a new wordlist of your own in order to crack the encrptyed password fromt he other two websites.

### Linkedin
The password leak involved Secure Hash Algorithm (SHA-1) encryption. The passwords in the dump were in the encrypted form and the ones which were cracked had there first five characters of the hash valued replaced with zero’s. In this algorithm, the password is converted into a 40 bit string, and these hash values are irreversible in nature, that is, it cannot be converted back to passwords in plain text. For this leak, I used dictionary attack. This wordlist used was first converted into SHA-1 values, and then their first five characters were replaced with zeros and afterwards they were compared with the actual password dump values. Once there was a successful match, then the hash value and the actual password in plain text was printed out.

### Formspring
The formspring leak, involved Secure Hash Algorithm (SHA-256) encryption. The passwords were encrypted in the SHA-256 format in which a salt value ranging from 00 - 99 was added. This salt is a randomly generated number added to the passwords before converting it into the hash value, and since these are added before encryption, and SHA-256 is irreversible, so it becomes very difficult to crack the passwords, even if the salt value is known. Once the salt value was added to the wordlist, it was then encrypted and compared with the password dump. When the hash value of the wordlist matched with that of the dump file, then the hash value along with the password in plain text was printed.

For all of the above password leaks, the other technique I considered was the brute force attack. Brute force attack means that we are trying all possible characters for a particular length of password, for example, for a 6 digit long password, we have combinations involving 52 alphabets both uppercase and lowercase, 10 numeric value and 33 special characters, giving total guesses of (95)^6 which is very large, exhaustive and time consuming, as well as it is just the case for the 6 digit length password, hence I had to drop the idea of using this method.
