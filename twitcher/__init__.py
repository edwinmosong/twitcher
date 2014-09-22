# twitcher project.
# Edwin Mo
"""
twitcher - A simpleTwitchTV API wrapper.

This python package provides ease of use and accessibility to many, if not all,
of TwitchTV's features.
"""
import json
import requests

import helper
import streams

__version__ = '0.0.1'

BASE_URL = 'https://api.twitch.tv/kraken'
GET_API_PATHS = {
    'streams':              '/streams/?',
    'streams_channel':      '/streams/%s/?',
    'streams_feature':      '/streams/featured?',
    'streams_summary':      '/streams/summary?',
    'channel':              '/channels/%s?',
    'channel_videos':       '/channels/%s/videos?',
    'channel_follows':      '/channels/%s/follows?'
}

class Twitcher(object):
    """ 
    TwitchTV client that is used to make and send requests. This class wraps
    requests and returns objects.
    """
    def __init__(self):
        self.rest_helper = helper.RESTHelper()

    def get_stream_info(self, game='', channel='', limit=25, offset=0,
        embeddable='false', hls='false'):
        """
        Returns a StreamInfoHelper object for the requested query.

         https://github.com/justintv/Twitch-API/blob/master/v2_resources/
        streams.md#get-streamschannel
    
        :params:        Default Description
        ------------------------------------------------------------------
        game            ''      Streams categorized under game.
        channel         ''      Streams from a comma-separated list of channels.
                                Name are case-sensitive.
        limit           25      Maximum number of objects in array. Max is 100
        offset          0       Object offset for pagination.
        embeddable      'false' If set to true, returns streams that can be 
                                embedded.
        hls             'false' If set to true, only returns using HLS.
        """
        if channel:
            endpoint = GET_API_PATHS['streams_channel'] % channel
        else:
            endpoint = GET_API_PATHS['streams']

        params = dict([('game', game), ('channel', channel), ('limit', limit),
                      ('offset', offset), ('embeddable', embeddable), 
                      ('hls', hls)])

        stream_info = self.rest_helper.request(endpoint=endpoint, params=params)
        return streams.StreamInfoHelper(stream_info, params=params)

