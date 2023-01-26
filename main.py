import amino
import random
import threading
from flask import Flask

app = Flask("")
@app.route("/")
def home():
	return "Bot is on"
	
def run():
	app.run(host = "0.0.0.0",port=random.randint(1000,9000))

def main():
	t = threading.Thread(target=run)
	t.start()

main()

client = amino.Client(deviceId="1966C095A1F1B5226FB9DE33CBD6D1909E99305869D1B90F71F470D0170A8A395A07AEB8063B1380E6")
#client.login(email="shivampanwarqe@gmail.com",password="uiic2208")
client.login(email="rdo5eu@oosln.com",password="uiic2208")

comId = '173896069' #aquarious

sub = amino.SubClient(comId=comId,profile=client.profile)

@client.event('on_text_message')
def on_text_message(data):
	content = data.message.content
	command = content.startswith
	chatid = data.message.chatId
	if command("-game"):
		sub.send_message(chatId=chatid, message="[cb]Game list \n1. Rock paper scissors [Ex : -rps rock]\n\n[ci]Please make sure you write the command carefully!")
	if command("-check"):
		sub.send_message(chatId=chatid,message="[Bot is online]")
	if command("-rps"):
			choices = ['rock', 'paper', "scissors"]
			computer = random.choice(choices)
			msg = data.message.content
			split = msg.split(" ")
			player = split[1]
			if player == computer:
				sub.send_message(chatId=chatid,message=f"Bot ={computer}\nPlayer = {player}\nTie!!")
				
			elif player == "rock":
				if computer == "paper":
					sub.send_message(chatId=chatid,message=f"Bot = {computer} \nPlayer = {player}\nYou lose!")
				if computer == "scissors":
						sub.send_message(chatId=chatid,message=f"Bot = {computer} \nPlayer = {player}\nYou win!!")
						
			elif player == "scissors":
				if computer == "rock":
					sub.send_message(chatId=chatid,message=f"Bot = {computer} \nPlayer = {player}\nYou lose!!")
				if computer == "paper":
					sub.send_message(chatId=chatid,message=f"Bot = {computer} \nPlayer = {player}\nYou win!!")
					
			elif player == "paper":
				if computer == "scissors":
					sub.send_message(chatId=chatid,message=f"Bot = {computer} \nPlayer = {player}\nYou lose!!")
				if computer == "rock":
					sub.send_message(chatId=chatid,message=f"Bot = {computer} \nPlayer = {player}\nYou win!!")
			
			
print('ready')
