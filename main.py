from rubpy import Client

# اینجا کویید چنل رو قرار بدید
chat_id = "b0EG30886d2ebe684047ad60628303a1"
with Client("bot") as bot:
	while True:
		lists = bot.get_messages_interval(chat_id, "25")
		ilists = []
		for i in lists['messages']:
			ilists.append(i['message_id'])
		bot.delete_messages(chat_id, ilists)
		print("message is delete ", ilists)
			
			
		   
