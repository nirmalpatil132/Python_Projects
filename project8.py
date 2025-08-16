# # Project 8. Caeser Cipher

logo = '''       
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
'''

alphanets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        # Non-alphabetic characters (numbers, symbols, spaces) are left unchanged
        if letter in alphanets:
            position = alphanets.index(letter)
            new_position = (position + shift_amount) % 26
            cipher_text += alphanets[new_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded text : {cipher_text}")

def decrypt(original_text, shift_amount):
    plain_text = ""
    for letter in original_text:
        # Non-alphabetic characters (numbers, symbols, spaces) are left unchanged
        if letter in alphanets:
            position = alphanets.index(letter)
            new_position = (position - shift_amount) % 26
            plain_text += alphanets[new_position]
        else:
            plain_text += letter
    print(f"Here is the decoded text : {plain_text}")

while True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Invalid option. Please type 'encode' or 'decode'.")
    restart = input("Type 'yes' to go again. Otherwise type 'no': ").lower()
    if restart != "yes":
        print("Goodbye!")
        break
