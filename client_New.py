import socket
from threading import Thread
import tkinter
import notify2

def receive():
    while True:
        data = c.recv(102).decode("utf8")
        msg_list.insert(tkinter.END, data)
        message = data.split(':',1)
        notify2.init('Message')
        print(message[1])
        n = notify2.Notification(message[0], message[1])
        n.set_urgency(notify2.URGENCY_CRITICAL)
        n.timeout = 500
        n.show()
        msg_list.see("end")       

def send(data = ''):
    data = my_msg.get()
    my_msg.set("")
    c.send(bytes(data,'utf8'))

def remove():
    msg_list.delete(0, tkinter.END)

top = tkinter.Tk()
top.title("chatbox")
top.resizable(0,0)
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
msg_list = tkinter.Listbox(messages_frame, height=15, width=50,  bg = 'white')
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack(ipady=10, ipadx=50, side=tkinter.LEFT)
entry_field.focus()
send_button = tkinter.Button(top, text="Send", command=send,fg = 'green')
send_button.pack(ipady=8,ipadx=14, side=tkinter.LEFT)
clear_button = tkinter.Button(top, text="Clear", command=remove,fg = 'red')
clear_button.pack(ipady=8, side=tkinter.LEFT)



host = 'localhost'
port = 12345
addr = (host,port)
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(addr)
name = 'Dark Lord'
c.send(bytes(name,"utf8"))

Thread(target = receive).start()
tkinter.mainloop()
#while True:
    #print(name,end = '')
    #data = input()
    #c.send(bytes(data,'utf8'))
