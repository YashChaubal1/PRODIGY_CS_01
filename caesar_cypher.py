#Yash Chaubal E214
def encrypt(text,shift):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+= chr((ord(char)+shift-65)%26+65)
        else:
            result+=chr((ord(char)+shift-97)%26+97)
    return result
text=input("Enter text:")
shift=3
print("Shift:"+ str(shift))
print("Cipher:"+ encrypt(text,shift))
