from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('devi')

conv = open('conv.txt', 'r').readlines()

bot.set_trainer(ListTrainer)

bot.train(conv)

while True:
	request = input('You : ')
	res = bot.get_response(request)

	print('Devi : ', res)
