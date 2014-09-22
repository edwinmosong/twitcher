"""
helper.py 

Contains helper classes and methods.
"""
import json
import logging
import requests
import urllib

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

    def request(self, verb='GET', url=BASE_URL, endpoint='', params={}):
        """
        Wraps requests. Sets defaults for verb(GET) and 
        url('https://api.twitch.tv/kraken')
        """
        target = url + endpoint + urllib.urlencode(params)

        logging.info({'status': 'making http request', 'verb': verb.upper(),
                      'url': target})

        if verb.upper() == 'GET':
            response = requests.get(target)
            if response.status_code != 200:
                raise RESTException('Failed attempting to %s: %s' % (verb, 
                    target))
        elif verb.upper() == 'PUT':
            response = requests.put(target)
            if response.status_code != 200:
                raise RESTException('Failed attempting to %s: %s' % (verb, 
                    target))
        else: # only supporting GET and PUT for now
            raise RESTException(
                'Attempted to request <%s> but only GET and PUT are supported.'
                 % verb.upper())

        return json.loads(response.content)