"""
channels.py 

Contains class and implementation of a TwitchTV channel.
"""

class Channel(object):
    def __init__(self, channel_data):
        if channel_data is None:
            raise AssertionError('received empty channel_data')

        self._channel_data  = channel_data
        self.display_name   = str(self._channel_data.get('display_name'))
        self._links         = self._channel_data.get('_links')
        self.teams          = self._channel_data.get('teams')
        self.created_at     = self._channel_data.get('created_at')
        self.logo           = str(self._channel_data.get('logo'))
        self.updated_at     = self._channel_data.get('updated_at')
        self.mature         = self._channel_data.get('mature')
        self.video_banner   = str(self._channel_data.get('video_banner'))
        self._id            = str(self._channel_data.get('_id'))
        self.background     = str(self._channel_data.get('background'))
        self.banner         = str(self._channel_data.get('banner'))
        self.url            = str(self._channel_data.get('url'))
        self.game           = str(self._channel_data.get('game'))
        self.status         = str(self._channel_data.get('status'))

