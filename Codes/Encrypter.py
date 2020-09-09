import time

# A basic encrypting script
# It's algorithm ->
# 1.) It reverses the string
# 2.) it changes vowels to numbers assigned like a=0 , e=1 and so on

print('Welcome to Encrypto...')
time.sleep(0.5)

encrypt = input('Please enter the letters to encrypt\n>>> ').lower()
# Converted it to lowercase to avoid mistakes

encryp_dict = {"a": "0", "e": "1",
               "i": "2", "o": "3",
               "u": "4"}

parse_encrpyt = encrypt[::-1]
# Reversed the string

for vowels in encryp_dict:
    parse_encrpyt = parse_encrpyt.replace(vowels, encryp_dict[vowels])
# Replaced the vowels with the dictionary

print(parse_encrpyt)

decryp_dict = {"0": "a", "1": "e",
               "2": "i", "3": "o",
               "4": "u"}
# Created a dictionary for decrypting the encrypted password


decrypt = input('Do you want to to decrypt the above encrypted code?\n(Y)es or (N)o\n>>>').lower()

if decrypt == 'y':
    parse_decrypt = parse_encrpyt[::-1]
    # Reversed the encrypted password

    for vowels in decryp_dict:
        parse_decrypt = parse_decrypt.replace(vowels, decryp_dict[vowels])
    # Reversed them with the decryt dictionary

    print(parse_decrypt)
    print('Your decrypted word is in small form...')

else:
    print('Thanks for using')

# This is a very basic encrypter and decrypter
# Just to give a idea ( working on more harder algorithms now )
