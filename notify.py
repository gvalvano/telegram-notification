#  Copyright 2019 Gabriele Valvano
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import telegram_notifier
import logging
import argparse
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


# telegram bot ---
TELEGRAM_TOKEN_ID = ''  # token-id
TELEGRAM_CHAT_ID = ''  # chat-id
# ----------------

parser = argparse.ArgumentParser(description='Notifier.')
parser.add_argument("--message", type=str, help='Message for the notifier.', default='Process terminated.')
parser.add_argument("--token_id", type=str, help='Token ID for the chat bot.', default=TELEGRAM_TOKEN_ID)
parser.add_argument("--chat_id", type=str, help='Chat ID for the chat bot.', default=TELEGRAM_CHAT_ID)
parser.add_argument("--hostname", type=str, help='Name of the server running the task.', default=hostname)
parser.add_argument("--ip", type=str, help='IP address of the server running the task.', default=IPAddr)


def main():

    args = parser.parse_args()
    text = args.message
    hostname = args.hostname
    ip = args.ip

    # telegram bot:
    token_id = args.token_id
    chat_id = args.chat_id

    # - - - - - - - - - -
    # Telegram notification:
    msg = "Automatic message from host: '{hostname}', at: {ip}\n{separator}\n" \
          "<b>MESSAGE: </b>\n<pre> {text} </pre>".format(separator=' -' * 10, text=text, hostname=hostname, ip=ip)
    telegram_notifier.basic_notifier(logger_name='training_notifier',
                                     token_id=token_id,
                                     chat_id=chat_id,
                                     message=msg,
                                     level=logging.INFO)


# just calls the `main` function above
if __name__ == '__main__':
    main()

