"""
Helper module for Skype
"""
import os
import sys
import requests
from helpers.base_helper import BaseHelper
from conf import skype_conf

class SkypeHelper(BaseHelper):
    """
    Skype Helper object
    """

    def post_message_on_skype(self, message):
        "Posts a predefined message on the set Skype channel"
        try:
            headers = {'Content-Type': 'application/json'}
            payload = {"msg" : message,
                      "channel": os.environ.get['channel_id'],
                      "API_KEY": os.environ.get['api_key']}

            response = requests.post(url=skype_conf.SKYPE_SENDER_ENDPOINT,
                                     json=payload, headers=headers)
            if response.status_code == 200:
                self.write(f'Successfully sent the Skype message - {message}')
            else:
                self.write(f'Failed to send Skype message', level='error')
        except Exception as err:
            raise Exception(f'Unable to post message to Skype channel, due to {err}')

        return response
