import flast
import threading

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
