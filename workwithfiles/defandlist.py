messages=['bienvenido','hasta pronto','adios']
sent_messages=[]
def show_messages(messages_list,sent_messages):
    
    while messages_list:
        sent_message= messages_list.pop()
        print (sent_message.title())
        sent_messages.append(sent_message)

show_messages(messages,sent_messages)
print(messages)
print(sent_messages)
print('Esos son todos los mensajes almacenados')
#si no queremos que la lista se altere, enviamos una copia así >> messages[:]
