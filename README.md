# BSY-bonus stage 5
Python bot for BSY bonus assignment.

# Requirements

1. Your task is to write the bot code and the controller code. The bot will be the infected computer, and the controller is what you use to control the bots.

2. Both parts should use gist.github.com to communicate.

3. The goal is to run some of your bots as 'infected' computers in the github channel, and you also connect to this channel with your controller to control them.

4. The communication between the bots and the controller should not be easily detected as 'bots' in the channel, therefore all communication should look like normal English markdown or text (text, images and emojis are accepted). You should use some steganography technique to hide your messages as English.

5. The controller should check if the bots are alive periodically

6. The controller should give orders to the bot and the bot should answer the output of the orders
The minimum orders are the following commands:
	- w (list of users currently logged in)
	- ls <PATH> (list content of specified directory)
	- id (if of current user)
	- Copy a file from the bot to the controller. The file name is specified
	- Execute a binary inside the bot given the name of the binary. Example: ‘/usr/bin/ps’

7. Publish the whole code in github and put the link as a flag for this stage.


| Requirements | Fulfilled    |
|--------------|--------------|
| item 1       | &check; |
| item 2       | &check; |
| item 3       | &check; |
| item 4       | &check; |
| item 5       | &check; |
| item 6       | &check; |
| item 7       | &check; |

# Steganography
* library pyUnicodeSteganography
* using text steganography


# Communication
* The first communication (registration) takes place via a call to the controller's API endpoint. The controller creates a Gist and in the following communication is Bot=gist_id.
* Communication between bots is done via Gist comments.
* Communication includes all commands with input.
* The pyUnicodeSteganography library is used for not capturing the communication.
* When the bot wants to shut down, it calls the /unregister-bot API, which deletes the gist belonging to the bot.


# Controller
* There are 3 threads (for api routes, for CMD input and for checking bot alive)
* Controller is implemented in Flask


# Bot
* When the bot starts, it registers with the controller and gets its gist_id.
* It then regularly checks for new before and after comments and processes and replies to new comments with a comment.
