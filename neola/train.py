from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
#initiate the neola bot
bot = ChatBot('Neola')
#open conversation file
conv = open('conv.txt', 'r').readlines()
#set the line trainer
bot.set_trainer(ListTrainer)
#train the using conv.txt
bot.train(conv)
#loop will run for conversation
while True:
	#input the user input
	request = input('You : ')
	#get the response from chatterbot trained data
	res = bot.get_response(request)
	#print the response
	print('Neola : ', res)
