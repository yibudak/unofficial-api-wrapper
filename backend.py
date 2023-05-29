from flask import Flask, request, jsonify
from twitter.account import Account
from flask_expects_json import expects_json
from config import Config

conf = Config("/etc/api_wrapper.conf")
app = Flask(__name__)
account = Account(conf.tw.email, conf.tw.username, conf.tw.password)

API_SCHEMA = {
    "type": "object",
    "properties": {
        "tweet_text": {"type": "string"},
        "reply_to": {"type": "integer"},
        "token": {"type": "string"},
    },
    "required": ["tweet_text", "reply_to", "token"],
}


@expects_json(API_SCHEMA, silent=True)
@app.route("/send_reply", methods=["POST"])
def send_reply():
    data = request.get_json()
    tweet_text = data["tweet_text"]
    reply_to = data["reply_to"]
    token = data["token"]

    if token != conf.app.token:
        return sonify({"status": "error"}), 400
    try:
        account.reply(text=tweet_text, tweet_id=reply_to)
        return jsonify({"status": "ok"}), 200
    except:
        return jsonify({"status", "error"}), 400
