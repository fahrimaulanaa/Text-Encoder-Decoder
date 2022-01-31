#Import module yang dibutuhkan
from cProfile import label
from tkinter import *;
import base64

#Setup module
root = Tk()
root.geometry('500x300')
root.title("Encoder dan Decoder pesan by Fahri Maulana")
Label(root, text='ENCODE DECODE', font='arial 20 bold').pack()
label(root, text='Fahri Maulana',font= 'arial 20 bold').pack(side = BOTTOM)
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

#Def Encoding mode
def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#Def Decoding mode
