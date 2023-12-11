import socket
from twilio.rest import Client

# Twilio account SID and auth token
account_sid = ""
auth_token = ""

# Twilio phone number and recipient phone number
twilio_number = ""
to_number = ""

# IRC server information
server = 'irc.chathispano.com'
port = 6667
channel = '#mexico'
bot_name = 'TeVigilo'
nickname = 'metus'

# Twilio client object
client = Client(account_sid, auth_token)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((server, port))

sock.send(('NICK {}\r\n'.format(bot_name)).encode('utf-8'))
sock.send(('USER {} 0 * :{}\r\n'.format(bot_name, bot_name)).encode('utf-8'))

while True:
    data = sock.recv(4096).decode('utf-8')
    if data.find('PING') != -1:
        sock.send(('PONG {}\r\n'.format(data.split(':')[1])).encode('utf-8'))
    elif '376' in data:
        sock.send(('JOIN {}\r\n'.format(channel)).encode('utf-8'))
        break

while True:
    data = sock.recv(4096).decode('iso-8859-1')
    print(data)
    if data.find('PING') != -1:
        sock.send(('PONG {}\r\n'.format(data.split(':')[1])).encode('utf-8'))
    if 'PRIVMSG' in data and 'metus' in data:
        username = data.split('!', 1)[0][1:]
        if username != 'metus':
            message = '{} te mencionó: {}'.format(username, data.split(':', 2)[2])
            client.messages.create(to=to_number, from_=twilio_number, body=message)

sock.close()


 


