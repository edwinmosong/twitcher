# twitcher project.
# Edwin Mo
"""
twitcher - A simpleTwitchTV API wrapper.

This python package provides ease of use and accessibility to many, if not all,
of TwitchTV's features.
"""
import json
import requests

import classes
import helper

__version__ = '0.0.1'

BASE_URL = 'https://api.twitch.tv/kraken'
GET_API_PATHS = {
    'streams':              '/streams/',
    'streams_channel':      '/streams/%s/',
    'streams_feature':      '/streams/featured',
    'streams_summary':      '/streams/summary',
    'channel':              '/channels/%s',
    'channel_videos':       '/channels/%s/videos',
    'channel_follows':      '/channels/%s/follows'
}

class Twitcher(object):
    """ 
    TwitchTV client that is used to make and send requests. This class wraps
    requests and returns objects.
    """
    def __init__(self):
        self.rest_helper = helper.RESTHelper()

    def get_streams(self):
        """
        Returns a list of Stream objects that are currently online on TwitchTV.

        :returns: a list of Stream objects
        """
        pass

    def get_stream_info(self, channel):
        """
        Returns a Stream object for channel

        :params: channel - string of name for the stream's channel
        :returns: classes.Stream object
        """
        endpoint = GET_API_PATHS['streams_channel'] % channel
        stream_info = self.rest_helper.request(endpoint=endpoint)
        return classes.Stream(stream_info)

