"""
"""
import json
import requests

import twitcher

BASE_URL = 'https://api.twitch.tv/kraken'


class RESTException(Exception):
    def __init__(self, msg):
        super(RESTException, self).__init__(self, msg)


class RESTHelper(object):
    """
    Helper class to wrap REST calls
    """
    def __init__(self):
        pass

    def request(self, verb='GET', url=BASE_URL, endpoint='', headers=None):
        """
        Wraps requests. Sets defaults for verb(GET) and 
        url('https://api.twitch.tv/kraken')
        """
        target = url + endpoint
        if verb.upper() == 'GET':
            response = requests.get(target, headers=headers)
            if response.status_code != 200:
                raise RESTException('Failed attempting to %s: %s' % (verb, 
                    target))
        elif verb.upper() == 'PUT':
            response = requests.put(target, headers=headers)
            if response.status_code != 200:
                raise RESTException('Failed attempting to %s: %s' % (verb, 
                    target))
        else: # only supporting GET and PUT for now
            raise RESTException('Attempted to request', verb.upper(), 'but only\
                GET and PUT are supported.')

        return json.loads(response.content)