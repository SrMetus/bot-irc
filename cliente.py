server_irc = "irc.irc-hispano.org"
port_irc = 6667
channel_irc = "#pub"
botnick_irc = "testbot"
botnickpass_irc = "nickkpass"
botpass_irc = "botpass//"
irc = bot_irc()
irc.connect_irc(server_irc, port_irc, channel_irc, botnick_irc, botpass_irc, botnickpass_irc)

while True:
    text = irc.response_irc()
    print(text)

    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send_irc(channel, "First message")