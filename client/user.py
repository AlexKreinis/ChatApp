import requests


class User:
    postURL = "http://localhost:5000/api/chat"
    getURL= "http://localhost:5000/api/chat/"

    def __init__(self, id, name, lastName, ip, motherBoard, password, friendsList):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.ip = ip
        self.motherBoard = motherBoard
        self.password = password
        self.motherBoard = motherBoard
        self.friendsList = friendsList

    def sendMessage(self, msg, friend_id):
        if friend_id in self.friendsList:
            PARAMS = {'ID': self.id, "otherID": friend_id, 'chat': [{"senderName": self.name, "text": msg}, ]}
            r = requests.post(url=User.postURL, json=PARAMS)
            pastebin_url = r.text
            print(pastebin_url)
        else:
            print("ERROR can't to send a message to friend that not in your's friendsList")

    def getMessage(self, friend_id):
        # Params : friend ID - the id of the friend that the message will be send to.
        # return the content of the message
        curURL = User.getURL + "{}/{}".format(self.id, friend_id)
        r = requests.get(url=curURL)
        data = r.json()
        text = data['chat'][0]["text"]
        return text

    def getFriends(self):
        return self.friendsList

    def approveControl(self):
        pass

    def getControl(self,friend_id):
        pass

    def getmotherBoard(self,friend_id):
        pass

    def addFriend(self, friend_id):
        self.friendsList.append(friend_id)

    def deleteFriend(self, friend_id):
        try:
            self.friendsList.remove(friend_id)
        except ValueError as e:
            print(e)


us1 = User('205509', 'matan', 'davidian', '0.0.0.0', 'intel mother Board', '123123', ['2312', '12332', '123'])
us1.sendMessage("hello my name is matan third try", '123')
print(us1.getMessage('123'))

