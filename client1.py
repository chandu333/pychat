import socket
from threading import Thread
import tkinter

def receive():
    while True:
        data = c.recv(102).decode("utf8")
        msg_list.insert(tkinter.END, data)

def send():
    data = my_msg.get()
    my_msg.set("")
    c.send(bytes(data,'utf8'))


top = tkinter.Tk()
top.title("chatbox")
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
msg_list = tkinter.Listbox(messages_frame, height=15, width=50,  bg = 'white')
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)/home/ioss/PycharmProjects/untitled/server.py
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send,fg = 'red')
send_button.pack()

host = 'localhost'
port = 12345
addr = (host,port)
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(addr)
print("enter your name")
name = input()
c.send(bytes(name,"utf8"))
Thread(target = receive).start()
tkinter.mainloop()
#while True:
    #print(name,end = '')
    #data = input()
    #c.send(bytes(data,'utf8'))



