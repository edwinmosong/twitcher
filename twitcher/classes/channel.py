"""
"""

class Channel(object):
	def __init__(self, channel_data):
		self._channel_data 	= channel_data
		self.display_name	= self._channel_data['display_name']
		self._links			= self._channel_data['_links']
		self.teams 			= self._channel_data['teams']
		self.created_at		= self._channel_data['created_at']
		self.logo			= self._channel_data['logo']
		self.updated_at		= self._channel_data['updated_at']
		self.mature			= self._channel_data['mature']
		self.video_banner	= self._channel_data['video_banner']
		self._id			= self._channel_data['_id']
		self.background		= self._channel_data['background']
		self.banner 		= self._channel_data['banner']
		self.url			= self._channel_data['url']
		self.game			= self._channel_data['game']