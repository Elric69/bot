#pylint:disable=W0702
import aminofix as amino
import random
import json
import requests
import os
from PIL import  Image
import time
from gtts import gTTS
import urllib.request
from joke.jokes import *
from uuid import uuid4
import threading
from helper import hp, com, ad, game,admin,crash,bedit
import flask
import threading
import random
app = flask.Flask("")

@app.route("/")

def home():
	return "Queen Bot is online"
	
def run():
	app.run(host="0.0.0.0", port = random.randint(1000,9000))

def keep_alive():
	o = threading.Thread(target=run)
	o.start()

keep_alive()

Email = "rdo5eu@oosln.com"
#Email = "redogi8497@cowck.com"
Password = "uiic2208"


#comId = '173896069' #aquarious
#comId='187945722' #imagination
comId = "207137967" #dark world
#comId = "19665645" #miraculous
vips = []
whiteList = []
blackList = []
cs = []

locked =[]

vip = "http://aminoapps.com/p/04dt0f"

client = amino.Client()
client.login(Email, Password)
client.join_community(comId=comId)
print('cm joined')

vipId = client.get_from_code(vip).objectId
vips.append(vipId)
whiteList.append(vipId)

sub = amino.SubClient(comId=comId,profile=client.profile)

L = ["http://aminoapps.com/p/mzdnk44","http://aminoapps.com/p/rsglfhc","http://aminoapps.com/p/plk5j7","http://aminoapps.com/p/jsvued","http://aminoapps.com/p/za9apv","http://aminoapps.com/p/h8j7zky","http://aminoapps.com/p/iv21n5","http://aminoapps.com/p/yl6hk8"]

for i in L:
	e = client.get_from_code(i).objectId
	whiteList.append(e)
print(f"Total admin : {len(whiteList)}\nTotal VIP : {len(vips)}")

adminName =[]
for k in whiteList:
	p = sub.get_user_info(k).nickname
	adminName.append(p)

print(adminName)

self = client.socket
def online():
	data = {
            "o": {
                "actions": ["Chatting"],
                "target": f"ndc://x{comId}/",
                "ndcId": int(comId),
                "id": "82333"
            },
            "t":304}
	data = json.dumps(data)
	time.sleep(2)
	client.socket.send(data)
	print("Bot status online : Done ✓")

def generate_transaction_id():
	return str(uuid4())
tran = generate_transaction_id()

@client.event('on_group_member_join')
def on_group_member_join(data):
	author = data.message.author
	if author.userId == client.userId : pass
	else:
		try:
			x=sub.get_chat_thread(data.message.chatId).title
			k=author.icon
			o=requests.get(k)
			file=open(".icons/author.png","wb")
			file.write(o.content)
			file.close()
			k =["Just landed to the chat.", "Need water??","Empty your pockets!!","Welcome to the team!!","A stranger has arrived.","Pokes!!","Yay!!! You win a lottery...Just kidding","Hospitable welcome!!","*whisper*Need drugs? ask the Host.","*whisper* Ever drunk???","Knock knock…(who is there?) It’s me"]
			wm = random.choice(k)
			with open(".icons/author.png","rb") as f:
				sub.send_message(chatId=data.message.chatId,message=f"""
[C]✬━━━━━━━━━━━━━━━━━━━━━✮
[C]｡ﾟﾟ･｡･ﾟﾟ｡｡ﾟﾟ･｡･ﾟﾟ｡
[C] 𝑯𝒆𝒍𝒍𝒐 {author.nickname}!
[C]｡ﾟﾟ･｡･ﾟﾟ｡｡ﾟﾟ･｡･ﾟﾟ｡
[C]🆆𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕥𝕙𝕖 {x}
[C]нσρє уσυ єηʝσу уσυя ѕтαу нєяє
[C]✬━━━━━━━━━━━━━━━━━━━━━✮
""",embedLink="http://aminoapps.com/p/04dt0f",embedImage=f,
embedTitle=author.nickname,embedContent=wm)
				print("Welcome")
		except:pass


@client.event('on_chat_tip')
def on_chat_tip(data):
	author = data.message.author
	authorId = author.userId
	if authorId == client.userId:
		pass
	else:
		msg = data.message
		coins = msg.extensions['tippingCoins']
		chatId = data.message.chatId
		author = data.message.author
		i=str(coins)
		sub.send_message(chatId=chatId, message=f'[C]Thank you for {i} coins \n\n[c]{author.nickname}')
		print("chat tip")

@client.event('on_text_message')
def on_text_message(data):
	mention = data.message.mentionUserIds
	content = data.message.content
	msgId = data.message.messageId
	chatId = data.message.chatId
	author = data.message.author
	authorId = author.userId
	command=content.startswith
	if author.userId in blackList:pass
	else:
		if command(crash):
			if authorId not in cs:
				sub.delete_message(chatId=chatId,messageId=msgId)
				cs.append(authorId)
				sub.send_message(chatId=chatId, message=f"please don't use that message <${author.nickname}$>\nIf you use that message again you'll be kicked from the gc")
			else:
				if authorId in cs:
					sub.delete_message(messageId=msgId,chatId=chatId)
					sub.kick(userId=authorId,chatId=chatId,allowRejoin=False)
					sub.send_message(chatId=chatId,message="User is kicked for violating the rules")

		if command("∆pfp"):
			if authorId in vips:
				info = sub.get_message_info(chatId = data.message.chatId, messageId = data.message.messageId)
				reply_message = info.json['extensions']
				if reply_message:
					image = info.json['extensions']['replyMessage']['mediaValue']
					filename = image.split("/")[-1]
					filetype = image.split(".")[-1]
					urllib.request.urlretrieve(image, filename)
					with open(filename, 'rb') as x:
						sub.edit_profile(icon=x)
						sub.send_message(chatId=chatId,message="Pfp changed",replyTo=msgId)
						os.remove(filename)

		if command("∆bot~edit"):
			if authorId in vips:
				sub.send_message(chatId=chatId,message=f"{bedit}")


		if command("∆nick"):
			if authorId in vips:
				o = content[5:]
				sub.edit_profile(nickname=o)
				sub.send_message(chatId,f"Nickname changed to {o}")

		if command("-dance"):
			if "-dance" in locked:
				sub.send_message(chatId,message="This command is locked", replyTo=msgId)
			else:
				x = random.choice(os.listdir(".dance"))
				o = f".dance/{x}"
				with open(o,"rb")as i:
					sub.send_message(chatId,file=i,fileType="gif")

		if command("-lock"):
			if authorId in whiteList:
				ms = data.message.content
				i = ms.split(" ")
				o = i[1]
				locked.append(o)
				print(locked)
				sub.send_message(chatId,f"[{o}] command is locked now",replyTo=msgId)
			if authorId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)
			
		if command("-unlock"):
			if authorId in whiteList:
				ms = data.message.content
				i = ms.split(" ")
				o = i[1]
				locked.remove(o)
				print(locked)
				sub.send_message(chatId,f"[{o}] command is unlocked now",replyTo=msgId)
			if authorId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)
			

		if command("-llocked"):
			sub.send_message(chatId=chatId,message=f"{locked}")
		if command("-iadmin"):
			if "-iadmin" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				sub.send_message(chatId, message=f"{adminName}",replyTo=msgId)


		if command("-ban"):
			if authorId in whiteList:
				for user in mention:
					if user in vips:
						blackList.append(authorId)
						sub.send_message(chatId,message=f"{author.nickname} is banned because he was trying to ban the owner",replyTo=msgId)
					if user not in vips:
						blackList.append(user)
						i = sub.get_user_info(user).nickname
						sub.send_message(chatId=chatId,message=f"{i} is banned, user can't use any command now",replyTo=msgId)
			if authorId not in whiteList :
				sub.send_message(chatId=chatId,message="You don't have access to the command", replyTo=msgId)

		if command("-unban"):
			if authorId in whiteList:
				for user in mention:
					blackList.remove(user)
					i = sub.get_user_info(user).nickname
					sub.send_message(chatId,message=f"{i} is unban now",replyTo=msgId)
			if authorId not in whiteList :
				sub.send_message(chatId=chatId,message="You don't have access to the command", replyTo=msgId)

		if command("-add"):
			if authorId in whiteList:
				for user in mention:
					whiteList.append(user)
					i = sub.get_user_info(user).nickname
					sub.send_message(chatId,message=f"{i} added as admin now",replyTo=msgId)
			if authorId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)
			
			
		if command("-remove"):
			if authorId in whiteList:
				for user in mention:
					if user in vips:
						whiteList.remove(authorId)
						sub.send_message(chatId, message=f"{author.nickname} is removed as admin because the mentioned person was the owner")
					else:
						whiteList.remove(user)
						i = sub.get_user_info(user).nickname
						sub.send_message(chatId,message=f"{i} is removed as admin",replyTo=msgId)
			if authorId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command")
		
		
		if command("-admin"):
			if "-admin" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				sub.send_message(chatId=chatId,message=admin)

		if command("-dice"):
			if "-dice" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				sub.send_message(chatId, f"🎲 -{random.randint(1, 20)},(1-20)- 🎲")


		if command("-follow"):
			if author.userId in whiteList:
				if "me" in content[7:14]:
					sub.follow(userId=author.userId)
					sub.send_message(chatId=chatId,message=f"started following {author.nickname}",replyTo=msgId)
				else:
					for user in mention:
						sub.follow(userId=user)
						m = sub.get_user_info(user).nickname
						sub.send_message(chatId=chatId, message=f"{m} has been followed",replyTo=msgId)
			if author.userId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)

		if command("-unfollow"):
			if author.userId in whiteList:
				if "me" in content[9:16]:
					sub.follow(userId=author.userId)
					sub.send_message(chatId=chatId,message=f"Unfollowed {author.nickname}",replyTo=msgId)
				else:
					for user in mention:
						if user in vips:
							i = sub.get_user_info(user).nickname
							sub.send_message(chatId=chatId,message=f"Can't do that for {i}",replyTo=msgId)
						else:
							sub.follow(userId=user)
							m = sub.get_user_info(user).nickname
							sub.send_message(chatId=chatId, message=f"{m} has been unfollowed",replyTo=msgId)
			if author.userId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)

		if command("-jview"):
			if "-jview" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				client.join_video_chat_as_viewer(comId=comId,chatId=chatId)
				sub.send_message(chatId=chatId,message="Joined as a viewer")


		if command("-join"):
			if author.userId in whiteList:
				sub.join_chat(chatId=chatId)
				print(f"join : {author.nickname}")
			
		if command("-leave"):
			if author.userId in whiteList:
				sub.leave_chat(chatId=chatId)
				print(f"leave : {author.nickname}")
			if author.userId not in vips:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)
				print(f"leave : {author.nickname}")
				
		if command("-ajoin"):
			if authorId in whiteList:
				o = sub.get_public_chat_threads(start=0,size=100).chatId
				for i in o:
					sub.join_chat(chatId=i)
				sub.send_message(chatId,message="Joined all public chats",replyTo=msgId)
			if authorId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)
		
		if command("-aleave"):
			if authorId in whiteList:
				o = sub.get_public_chat_threads(start=0,size=100).chatId
				for i in o:
					sub.leave_chat(chatId=i)
				sub.send_message(chatId,message="Left from all public chats",replyTo=msgId)
			if authorId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)


		if command("-linkjoin"):
			if author.userId in whiteList:
				i = data.message.content
				split = i.split(" ")
				link = split[1]
				l = str(link)
				cid = client.get_from_code(l).objectId
				sub.join_chat(chatId=cid)
				sub.send_message(chatId=chatId,message="Chat joined")
				print(f"linkjoin : {author.nickname}")
			if author.userId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)
				print(f"linkjoin : {author.nickname}")

		if command('-help'):
			try:
				img=open(".icons/img2.png","rb")
				sub.send_message(chatId=chatId, message=hp,embedImage=img,embedLink="http://aminoapps.com/p/04dt0f",embedTitle="Made by Elric",embedType=0)
				print(f"help : {author.nickname}")
			except:pass


		if command('-image'):
			if "-image" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				img=open(".icons/img2.png","rb")
				sub.send_message(chatId=chatId, message=ad)
				print(f"image : {author.nickname}")


		if command('-game'):
			if "-game" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				img=open(".icons/img2.png","rb")
				sub.send_message(chatId=chatId, message=game,embedImage=img,embedLink="http://aminoapps.com/p/04dt0f",embedTitle="Made by Elric")


		if command("-common"):
			if "-common" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				img=open(".icons/img2.png","rb")
				sub.send_message(chatId=chatId,message=com)
				print(f"common : {author.nickname}")


		if command("-coins"):
			if "-coins" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				coins = content[6:]
				i = int(coins)
				if i > 500:
					sub.send_message(chatId=chatId,message="Coins must be under 500",replyTo=msgId)
				else:
					sub.send_coins(coins=i,chatId=chatId,transactionId=tran)
					sub.send_message(chatId=chatId,message=f"Sent {i} coins to the host")


		if command('-pm'):
			if author.userId in whiteList:
				if 'me' in content[3:9]:
						sub.start_chat(userId=author.userId, message='Hello!!')
						sub.send_message(chatId=chatId,message=f'Chat started with {author.nickname}',replyTo=msgId)
				else:
					for user in mention:
						i=sub.get_user_info(user).nickname
						sub.start_chat(userId=user, message='Hello!!')
						sub.send_message(chatId, message=f'Chat started with {i}', replyTo=msgId)
			if author.userId not in whiteList:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)


		if command("-say"):
			if "-say" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				t=content[4:]
				out=gTTS(text=t,lang='en',tld='co.in',slow=False)
				out.save("text.mp3")
				with open("text.mp3","rb") as f:
					sub.send_message(chatId=data.message.chatId,file=f,fileType="audio")
					f.close()
					os.remove('text.mp3')

		
		if content.startswith("-startvc"):
			if "-startvc" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				sub.send_message(chatId=data.message.chatId,message="Starting Live mode in 5 seconds",replyTo=msgId)
				time.sleep(5)
				client.start_vc(comId=comId,chatId=chatId,joinType=1)
				sub.send_message(chatId=data.message.chatId,message="Vc started")


		if command("-endvc"):
			if "-endvc" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				sub.send_message(chatId=data.message.chatId,message="Ending Live mode in 5 seconds",replyTo=msgId)
				time.sleep(5)
				client.end_vc(comId=comId,chatId=chatId,joinType=2)
				sub.send_message(chatId=chatId,message="Vc ended")

			
		if command("-ai"):
			if "-ai" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				i=content[3:]
				link = f"http://api.brainshop.ai/get?bid=153868&key=rcKonOgrUFmn5usX&uid=1&msg={i}"
				response = requests.get(link)
				json_data = json.loads(response.text)
				chatbot = json_data["cnt"]
				sub.send_message(chatId=chatId, message=f"{chatbot}",replyTo=msgId)
			
		if command("-global"):
			if "-global" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				for user in mention:
					if user not in vips:
						i = sub.get_user_info(user).nickname
						img=open(".icons/img.png",'rb')
						a_id=client.get_user_info(userId=str(user)).aminoId
						sub.send_message(chatId=chatId,message=f'''
[CI]Global id of {i}
\n[ci]{author.nickname}
''',embedLink=f"https://aminoapps.com/u/{a_id}",embedTitle='Made by Elric',embedImage=img)
					if user in vips:
						o = sub.get_user_info(user).nickname
						sub.send_message(chatId=chatId, message=f"I don't have access to get global of {o}",replyTo=msgId)
				

		if command("-inviteall"):
			if "-inviteall" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				h=sub.get_online_users(start=0,size=1000).profile.userId
				m=len(h)
				for u in h:
					sub.invite_to_chat(userId=u,chatId=data.message.chatId)
				sub.send_message(chatId=chatId,message=f"invited {m} users in gc")


		if command('-hug'):
			if "-hug" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				if 'me' in content[4:8]:
					hx=random.choice(os.listdir(".hug"))
					hu=f".hug/{hx}"
					with open(hu,"rb") as f:
						sub.full_embed(chatId=chatId,image=f,message=f'•𝑄𝑢𝑒𝑒𝑛ꨄ︎• ‌hugs {author.nickname}',link="http://aminoapps.com/p/04dt0f")
				else:
					for user in mention:
						hx=random.choice(os.listdir(".hug"))
						i=sub.get_user_info(user).nickname
						hu=f".hug/{hx}"
						with open(hu,"rb") as f:
							sub.full_embed(chatId=chatId,image=f,message=f'{author.nickname} ‌hugs {i}',link="http://aminoapps.com/p/04dt0f")
								
						
		if command('-burger'):
			if "-burger" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				if 'for me' in content[7:]:
					de=".food/burger.png"
					with open(de,"rb") as f:
						sub.full_embed(chatId=chatId,image=f,message=f'''[ci]Here's the burger for {author.nickname}''',link="http://aminoapps.com/p/04dt0f")
				else:
					for user in mention:
						i=sub.get_user_info(user).nickname
						de=".food/burger.png"
						with open(de,"rb") as f:
							sub.full_embed(chatId=chatId,image=f,message=f'''[ci]Here's the Burger for {i}''',link="http://aminoapps.com/p/04dt0f")
					

		if command("-bg"):
			if "-bg" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				x=sub.get_chat_thread(chatId).backgroundImage
				image=sub.get_chat_thread(chatId).backgroundImage
				filename = image.split("/")[-1]
				urllib.request.urlretrieve(image, filename)
				with open(filename, 'rb') as fp:
					sub.send_message(chatId=chatId, file=fp, fileType="image")
				os.remove(filename)

		
		if command("-joke"):
			if "-joke" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				joke = [chucknorris(), icndb(), icanhazdad(), geek()]
				sub.send_message(data.message.chatId, message=random.choice(joke),replyTo=msgId)


		if command("-clear"):
			if author.userId in vips:
				try:
					c =content[7:]
					for i in c:
						d=int(i)
						a=sub.get_chat_messages(chatId=data.message.chatId,size=d)
						for a in a.messageId:
							sub.delete_message(chatId=data.message.chatId,messageId=a,asStaff=True,reason="clear")
				except:pass
				sub.send_message(chatId=data.message.chatId,message=f"Cleared {d} messages")
			if authorId not in vips:
				sub.send_message(chatId=chatId,message="You don't have access to the command",replyTo=msgId)
				print(f"clear : {author.nickname}")
		
		if command("-img"):
			if "-img" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				info = sub.get_message_info(chatId = chatId, messageId = msgId)
				reply_message = info.json['extensions']
				if reply_message:
					image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
					filename = image.split("/")[-1]
					filetype = image.split(".")[-1]
					if filetype!="image":
						filetype = "gif"
						urllib.request.urlretrieve(image, filename)
						with open(filename, 'rb') as fp:
							sub.send_message(chatId=chatId, file=fp, fileType=filetype)
							os.remove(filename)
							print(f"img : {author.nickname}")
			

		if command("-getpfp"):
			if "-getpfp" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				for user in mention:
					x=sub.get_user_info(user).icon
					r=requests.get(f"{x}")
					file=open(".icons/user.png","wb")
					file.write(r.content)
					file.close()
					with open(".icons/user.png","rb")as i:
						sub.send_message(chatId=chatId,file=i,fileType="image")
						os.remove(".icons/user.png")
			
		if command("-announce"):
			if "-announce" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				i=content[9:]
				p=author.icon
				r=requests.get(f"{p}")
				file=open(".icons/author.png","wb")
				file.write(r.content)
				file.close()
				x=sub.get_chat_threads(start=0,size=1000).chatId
				chat = sub.get_chat_thread(chatId).title
				for c in x:
					with open(".icons/author.png","rb") as pfp:
						sub.send_message(chatId=c,message=f"""
[C]✬━━━━━━━━━━━━━━━━━━━━━✮
[c] Announcement
[c]----------------------------
[c]{i}

[C]✬━━━━━━━━━━━━━━━━━━━━━✮
""",embedImage=pfp,embedTitle=f"By {author.nickname}",embedContent=f"Chat : {chat}",embedLink="http://aminoapps.com/p/832phl")
				sub.send_message(chatId=chatId,message="Announcement complete")

				
		if command("-uid"):
			if "-uid" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				x=data.message.chatId
				z=author.userId
				sub.send_message(chatId=chatId,message=f"""UserId -> {z}

ChatId -> {x}""")

			
		if command("-onmem"):
			if "-onmem" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				mem = []
				q=sub.get_online_users(start=0,size=1000)
				for o in q.profile.nickname:
					mem.append(o)
					i = o+"\n"
				sub.send_message(chatId=chatId,message=f"""[c]Online Members
[c]------------------------------
[c]{mem}
[c][c]------------------------------""")



		if command('-love'):
			if "-love" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				for user in mention:
					x=sub.get_user_info(userId=user).icon
					r=requests.get(f"{x}")
					file=open(".icons/user.png","wb")
					file.write(r.content)
					file.close()
					k=author.icon;o=requests.get(k)
					file=open(".icons/author.png","wb")
					file.write(o.content)
					file.close()
					image1 = Image.open('.icons/user.png')
					image2 = Image.open('.icons/author.png')
					image1 = image1.resize((400,400))
					image2 = image2.resize((400,400))
					image1_size = image1.size
					new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
					new_image.paste(image1,(0,0))
					new_image.paste(image2,(image1_size[0],0))
					new_image.save(".icons/img.jpg","JPEG")
					f_img=Image.open('.icons/img.jpg')
					new_image = f_img.resize((800,400))
					new_image.save('.icons/final.png')
					os.remove(".icons/author.png")
					os.remove(".icons/user.png")
					os.remove(".icons/img.jpg")
					with open (".icons/final.png","rb") as im:
						x=sub.get_user_info(userId=user).nickname
						ms=f"""[C]✬━━━━━━━━━━━━━━━━━━━━━━━✮
[c]Love ❤ match between
[c]{author.nickname} and {x}
[c]is {random.randint(0,100)}%
[C]✬━━━━━━━━━━━━━━━━━━━━━━━✮"""
						sub.full_embed(chatId=chatId,message=ms,link="http://aminoapps.com/p/04dt0f",image=im)
						os.remove(".icons/final.png")


		if command('-hate'):
			if "-hate" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				for user in mention:
					x=sub.get_user_info(userId=user).icon
					r=requests.get(f"{x}")
					file=open(".icons/user.png","wb")
					file.write(r.content)
					file.close()
					k=author.icon;o=requests.get(k)
					file=open(".icons/author.png","wb")
					file.write(o.content)
					file.close()
					image1 = Image.open('.icons/user.png')
					image2 = Image.open('.icons/author.png')
					image1 = image1.resize((400,400))
					image2 = image2.resize((400,400))
					image1_size = image1.size
					new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
					new_image.paste(image1,(0,0))
					new_image.paste(image2,(image1_size[0],0))
					new_image.save(".icons/img.jpg","JPEG")
					f_img=Image.open('.icons/img.jpg')
					new_image = f_img.resize((800,400))
					new_image.save('.icons/final.png')
					os.remove(".icons/author.png")
					os.remove(".icons/user.png")
					os.remove(".icons/img.jpg")
					with open (".icons/final.png","rb") as im:
						x=sub.get_user_info(userId=user).nickname
						ms=f"""[C]✬━━━━━━━━━━━━━━━━━━━━━━━✮
[c]Hate 💔 between 
[c]{author.nickname} and {x}
[c]is {random.randint(0,100)}%
[C]✬━━━━━━━━━━━━━━━━━━━━━━━✮"""
						sub.full_embed(chatId=chatId,message=ms,link="http://aminoapps.com/p/04dt0f",image=im)
						os.remove(".icons/final.png")
				
				
			
		if command('-kill'):
			if "-kill" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				for user in mention:
					if user in vips:
						o = sub.get_user_info(user).nickname
						sub.send_message(chatId=chatId, message=f"Can't do that for <$@{o}$>",mentionUserIds=user,replyTo=msgId)
					if user not in vips:
						x=sub.get_user_info(userId=user).icon
						r=requests.get(f"{x}")
						file=open(".icons/user.png","wb")
						file.write(r.content)
						file.close()
						k=author.icon;o=requests.get(k)
						file=open(".icons/author.png","wb")
						file.write(o.content)
						file.close()
						Image1 = Image.open('.icons/imgg.png')
						Image1copy = Image1.copy()
						Image2 = Image.open('.icons/user.png')
						Image2copy = Image2.copy()
						img2=Image2copy.resize((50,50))
						Image1copy.paste(img2, (250,270))
						Image1copy.save('.icons/paste.png')
						image3=Image.open(".icons/paste.png")
						image4=Image.open(".icons/author.png")
						img4=image4.resize((50,50))
						img3=image3.copy()
						img3.paste(img4,(415,105))
						img3.save(".icons/cut.png")
						i_mg=Image.open(".icons/cut.png")
						f_img=i_mg.resize((800,500))
						f_img.save(".icons/final.png")
						os.remove(".icons/paste.png")
						os.remove(".icons/cut.png")
						with open (".icons/final.png","rb") as im:
							x=sub.get_user_info(userId=user).nickname
							ms=f"""
[ci]{author.nickname} killed {x}"""
							sub.full_embed(chatId=chatId,message=ms,link="http://aminoapps.com/p/04dt0f",image=im)

				
				
		if command('-propose'):
			if "-propose" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				for user in mention:
					x=sub.get_user_info(userId=user).icon
					r=requests.get(f"{x}")
					file=open(".icons/user.png","wb")
					file.write(r.content)
					file.close()
					k=author.icon;o=requests.get(k)
					file=open(".icons/author.png","wb")
					file.write(o.content)
					file.close()
					Image1 = Image.open('.icons/pro.png')
					Image1copy = Image1.copy()
					Image2 = Image.open('.icons/user.png')
					Image1 = Image.open('.icons/pro.png')
					Image1copy = Image1.copy()
					Image2 = Image.open('.icons/user.png')
					Image2copy = Image2.copy()
					img2=Image2copy.resize((60,60))
					Image1copy.paste(img2, (330,60))
					Image1copy.save('.icons/paste.png')
					image3=Image.open(".icons/paste.png")
					image4=Image.open(".icons/author.png")
					img4=image4.resize((60,60))
					img3=image3.copy()
					img3.paste(img4,(180,140))
					img3.save(".icons/cut.png")
					i_mg=Image.open(".icons/cut.png")
					f_img=i_mg.resize((800,800))
					f_img.save(".icons/final.png")
					os.remove(".icons/paste.png")
					os.remove(".icons/cut.png")
					with open (".icons/final.png","rb") as im:
						x=sub.get_user_info(userId=user).nickname
						ms=f"""[C]✬━━━━━━━━━━━━━━━━━━━━━✮
[c]{author.nickname} proposed {x}
[C]✬━━━━━━━━━━━━━━━━━━━━━✮"""
						sub.full_embed(chatId=chatId,message=ms,link="http://aminoapps.com/p/04dt0f",image=im)
						os.remove(".icons/final.png")
						os.remove(".icons/author.png")
						os.remove(".icons/user.png")

					
		if command('-slap'):
			if "-slap" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				for user in mention:
					if user in vips:
						o = sub.get_user_info(user).nickname
						sub.send_message(chatId=chatId, message=f"Can't do that for <$@{o}$>",mentionUserIds=user,replyTo=msgId)
					if user not in vips:
						x=sub.get_user_info(userId=user).icon
						r=requests.get(f"{x}")
						file=open(".icons/user.png","wb")
						file.write(r.content)
						file.close()
						k=author.icon;o=requests.get(k)
						file=open(".icons/author.png","wb")
						file.write(o.content)
						file.close()
						image1 = Image.open('.icons/user.png')
						image2 = Image.open('.icons/author.png')
						Image1 = Image.open('.icons/slap.png')
						Image1copy = Image1.copy()
						Image2 = Image.open('.icons/user.png')
						Image2copy = Image2.copy()
						img2=Image2copy.resize((60,60))
						Image1copy.paste(img2, (100,45))
						Image1copy.save('.icons/paste.png')
						image3=Image.open(".icons/paste.png")
						image4=Image.open(".icons/author.png")
						img4=image4.resize((60,60))
						img3=image3.copy()
						img3.paste(img4,(340,80))
						img3.save(".icons/cut.png")
						i_mg=Image.open(".icons/cut.png")
						f_img=i_mg.resize((800,500))
						f_img.save(".icons/final.png")
						os.remove(".icons/paste.png")
						os.remove(".icons/cut.png")
						with open (".icons/final.png","rb") as im:
							x=sub.get_user_info(userId=user).nickname
							ms=f"""[C]✬━━━━━━━━━━━━━━━━━━━━━━━✮
[c]{x} got {random.randint(0,50)}
[c] slaps from {author.nickname}
[C]✬━━━━━━━━━━━━━━━━━━━━━━━✮"""
							sub.full_embed(chatId=chatId,message=ms,link="http://aminoapps.com/p/04dt0f",image=im)

							os.remove(".icons/final.png")



		if command("-rps"):
			if "-rps" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				choices = ['rock', 'paper', "scissors"]
				computer = random.choice(choices)
				arg = data.message.content
				split = arg.split(" ")
				player = split[1]
				k=data.message.author.icon
				o=requests.get(k)
				file=open(".game/author.png","wb")
				file.write(o.content)
				file.close()
				image=Image.open(".game/lose.png")
				img=image.copy()
				image2=Image.open(".game/author.png")
				img2 = image2.copy()
				img3=img2.resize((190,190))
				img.paste(img3,(160,30))
				img.save(".game/sfinal.png")
				o = Image.open(".game/sfinal.png")
				m = o.resize((835,430))
				m.save(".game/losefinal.png")
				_image = Image.open(".game/win.png")
				_img = _image.copy()
				_image2=Image.open(".game/author.png")
				_img2 = _image2.copy()
				_img3=_img2.resize((190,190))
				_img.paste(img3,(505,50))
				_img.save(".game/sfinal.png")
				_o = Image.open(".game/sfinal.png")
				_m = _o.resize((835,430))
				_m.save(".game/winfinal.png")
				os.remove(".game/sfinal.png")
				l = "http://aminoapps.com/p/04dt0f"
			
				if player == computer:
					with open(".game/tie.png","rb") as o:
						sub.full_embed(chatId=chatId,message=f"""[cb]----[Result : Tie]----\n[c]Bot.     : {computer}\n[c]Player : {player}""",link=l,image=o)

				elif player == "rock":
					if computer == "paper":
						with open(".game/losefinal.png","rb")as o:
							sub.full_embed(chatId=chatId,message=f"""[cb]----[Result : You Lose!]----\n[c]Bot.     {computer}\n[c]Player : {player}""",link=l,image=o)


					if computer == "scissors":
						with open(".game/winfinal.png","rb")as o:
							sub.full_embed(chatId=chatId,message=f"""[cb]----[Result : You Win!]----\n[c]Bot.     : {computer}\n[c]Player : {player}""",link=l,image=o)

						
				elif player == "scissors":
					if computer == "rock":
						with open(".game/losefinal.png","rb")as o:
							sub.full_embed(chatId=chatId,message=f"""[cb]----[Result : You Lose!]----\n[c]Bot.     : {computer}\n[c]Player : {player}""",link=l,image=o)

						
					if computer == "paper":
						with open(".game/winfinal.png","rb")as o:
							sub.full_embed(chatId=chatId,message=f"""[cb]----[Result : You Win!]----\n[c]Bot.     : {computer}\n[c]Player : {player}""",link=l,image=o)

						
				elif player == "paper":
					if computer == "scissors":
						with open(".game/losefinal.png","rb")as o:
							sub.full_embed(chatId=chatId,message=f"""[cb]----[Result : You Lose!]----\n[c]Bot.     : {computer}\n[c]Player : {player}""",link=l,image=o)

						
					if computer == "rock":
						with open(".game/winfinal.png","rb")as o:
							sub.full_embed(chatId=chatId,message=f"""[cb]----[Result : You Win!]----\n[c]Bot.     : {computer}\n[c]Player : {player}""",link=l,image=o)




		if command('-trash'):
			if "-trash" in locked:
				sub.send_message(chatId,"This command is locked",replyTo=msgId)
			else:
				for user in mention:
					if user in vips:
						o = sub.get_user_info(user).nickname
						sub.send_message(chatId=chatId, message=f"Can't do that for <$@{o}$>",mentionUserIds=user,replyTo=msgId)
					if user not in vips:
						x=sub.get_user_info(userId=user).icon
						r=requests.get(f"{x}")
						file=open(".icons/user.png","wb")
						file.write(r.content)
						file.close()
						k=author.icon;o=requests.get(k)
						file=open(".icons/author.png","wb")
						file.write(o.content)
						file.close()
						image1 = Image.open('.icons/user.png')
						image2 = Image.open('.icons/author.png')
						Image1 = Image.open('.icons/trash.png')
						Image1copy = Image1.copy()
						Image2 = Image.open('.icons/user.png')
						Image2copy = Image2.copy()
						img2=Image2copy.resize((75,75))
						Image1copy.paste(img2, (40,250))
						Image1copy.save('.icons/paste.png')
						image3=Image.open(".icons/paste.png")
						image4=Image.open(".icons/author.png")
						img4=image4.resize((95,95))
						img3=image3.copy()
						img3.paste(img4,(280,100))
						img3.save(".icons/cut.png")
						i_mg=Image.open(".icons/cut.png")
						f_img=i_mg.resize((800,800))
						f_img.save(".icons/final.png")
						os.remove(".icons/paste.png")
						os.remove(".icons/cut.png")
						with open (".icons/final.png","rb") as im:
							x=sub.get_user_info(userId=user).nickname
							ms=f"""
[ci]{author.nickname} throws {x} in dustbin"""
							sub.full_embed(chatId=chatId,message=ms,link="http://aminoapps.com/p/04dt0f",image=im)
							os.remove(".icons/final.png")
							os.remove(".icons/user.png")
							os.remove(".icons/author.png")
			
print('ready')
while True:
	online()
	time.sleep(420)
