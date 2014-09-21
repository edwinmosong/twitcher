"""
"""

class Stream(object):
	"""
	Class Stream represents a Stream in TwitchTV
	"""
	def __init__(data):
		"""
		:params: data - response in JSON format
		"""
		self._data = data
		
		# stream is online
		if self._data['stream'] is None:
			self.online 		= False
			self.stream_url		= self._data['_links']['self']
			self.broadcaster	= None
			self.preview		= None
			self.stream_id		= None
			self.viewers		= 0
			self.name			= None
			self.game			= None
			self.channel_url	= self._data['_links']['channel']
			self.channel 		= None
			self.channel_id		= None

		# stream is offline
		else:
			self.online			= True
			self.stream_url 	= self._data['stream']['_links']['self']
			self.broadcaster 	= self._data['broadcaster']
			self.preview 		= self._data['preview']
			self.stream_id		= self._data['stream']['_id']
			self.viewers		= int(self._data['viewers'])
			self.name 			= self._data['name']
			self.game			= self._data['game']
			self.channel_url	= self._data['_links']['channel']
			self.channel 		= Channel(self._data['channel'])
			self.channel_id	= self._data['stream']['channel']['_id']
			