class Message:
    message_counter = 1
    def __init__(self,sender,content):
        self.sender = sender
        self.counter = content
        self.id = Message.message_counter
        Message.message_counter += 1
    
    def __str__(self):
        return f"({self.id}) {self.sender.username} : {self.content}"
    
class User:
    def __init__(self,username):
        self.username = username
        self.chatRoom = None
    
    def join_chatroom(self,chatroom):
        if self.chatRoom:
            print(f"{self.username} is already in a chatroom")
        else:
            chatroom.add_user(self)
            self.chatRoom = chatroom
            print(f"{self.username} joined {chatroom.name}")
    
    def leave_chatroom(self):
        if not self.chatRoom:
            print(f"{self.username} is not in any chatroom")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatr
    
    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)