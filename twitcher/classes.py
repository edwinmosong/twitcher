import requests

class Stream(object):
    """
    Class Stream represents a Stream in TwitchTV
    """
    def __init__(self, data):
        """
        :params: data - response in JSON format
        """
        if data is None:
            raise AssertionError('received empty data')
        self._data = data
        
        # stream is offline
        if self._data['stream'] is None:
            self.online         = False
            self.broadcaster    = None
            self.preview        = None
            self.stream_id      = None
            self.viewers        = 0
            self.name           = None
            self.game           = None
            self.channel        = None
            self.url            = None

        # stream is online
        else:
            self.online         = True
            self.broadcaster    = self._data['stream'].get('broadcaster')
            self.preview        = self._data['stream'].get('preview')
            self.stream_id      = self._data['stream'].get('_id')
            self.viewers        = int(self._data['stream'].get('viewers', 0))
            self.name           = self._data['stream'].get('name')
            self.game           = self._data['stream'].get('game')
            self.channel        = Channel(self._data['stream']['channel'])
            self.url            = self.channel.url


class Channel(object):
    def __init__(self, channel_data):
        if channel_data is None:
            raise AssertionError('received empty channel_data')

        self._channel_data  = channel_data
        self.display_name   = self._channel_data.get('display_name')
        self._links         = self._channel_data.get('_links')
        self.teams          = self._channel_data.get('teams')
        self.created_at     = self._channel_data.get('created_at')
        self.logo           = self._channel_data.get('logo')
        self.updated_at     = self._channel_data.get('updated_at')
        self.mature         = self._channel_data.get('mature')
        self.video_banner   = self._channel_data.get('video_banner')
        self._id            = self._channel_data.get('_id')
        self.background     = self._channel_data.get('background')
        self.banner         = self._channel_data.get('banner')
        self.url            = self._channel_data.get('url')
        self.game           = self._channel_data.get('game')

