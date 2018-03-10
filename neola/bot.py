from chatterbot import ChatBot
bot = ChatBot(
    "Neola",
    database="db.sqlite3"
)
while True:
    request = input('You : ')
    res = bot.get_response(request)
    print('Neola : ', res)
