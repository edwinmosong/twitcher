"""
streams.py 

Contains classes StreamInfoHelper and Stream. StreamInfoHelper is a wrapper with
iteration capabilities to iterate over a large set of streams. Stream is a
representation of the TwitchTV stream.
"""
import requests

import channels
import helper


class StreamInfoHelper(object):
    """
    Creates ease of use for user. This is a wrapper/helper that is returned 
    from all stream-get requests. Exposes relevant info in the result set of 
    Streams such as total viewers.

    StreamInfoHelper iterable: if > 25 results, iterate over all "next" links 
    self.result_set  iterable: list of Stream objects (capped at 25)

    To iterate over each Stream in the result set:
        >>> for stream in myStreamInfoHelper.result_set:
        ...     # do your thing

    To iterate over each result_set:
        >>> for result_set in myStreamInfoHelper:
        ...     # do your thing
        
    """
    def __init__(self, data, params):
        """
        :params:    data   - data returned from RESTHelper.request()
                    request_kwargs - dictionary of parameters passed to get this
                    information. Used for iteration.
        :returns:   StreamInfoHelper object
        """
        if data is None:
            raise AssertionError('received empty data')
        self._data = data
        self.rest_helper        = helper.RESTHelper()
        self._params            = params

        self.result_set         = self._get_results(self._data)
        self.viewers            = self._get_viewers()
        self._total             = len(self.result_set)
        # iteration variables
        self._iter_start        = False

        if self._total == 0 or self._total < self._params['limit']:
            self._next = None
        else:
            self._next = self._data['_links'].get('next')

    def __iter__(self):
        self._iter_start = True
        self._next = self._data['_links'].get('next')
        return self

    def next(self):
        if self._iter_start:
            self._iter_start = False
            return self

        if self._next is None:
            raise StopIteration()
        else:
            # self._next already has the url with previous, correct params
            # passing params again would cause the url to be invalid!
            _data = self.rest_helper.request(url=self._next, 
                                             params={})
            sih = StreamInfoHelper(_data, params=self._params)
            self._next = sih._next
            return sih

    def _get_results(self, data):
        """ 
        Parses a response already in JSON format. This is specific to the Stream
        requests. 
        :params:    data - data in dictionary
        :returns:   list of Stream objects, or empty list
        """
        if data is None:
            return []

        _data = data
        stream_objs = []

        if 'streams' in _data:
            for stream_data in _data['streams']:
                stream_objs.append(Stream(stream_data))
            return stream_objs

        elif 'stream' in _data:
            return [Stream(_data['stream'])]

        elif 'featured' in _data:
            for featured_stream in _data['featured']:
                stream_objs.append(Stream(featured_stream['stream']))
            return stream_objs

        else:
            raise AssertionError('was expecting streams or stream, but only \
                found %s' % ' '.join([keys for keys in _data.iterkeys()]))

    def _get_viewers(self):
        """
        Gets all viewers in self.result_set
        """
        total_viewers = 0
        for stream in self.result_set:
            total_viewers += stream.viewers
        return total_viewers

    def get_streams(self):
        """ 
        Returns the result set of Streams.
        """
        return self.result_set

    def get_all_streams(self, limit=50):
        """
        :params: limit, default to 50 (twice normal limit)
        Returns the result set of all streams, up to the provided limit. This 
        goes through all _next links and returns Stream objects in a list.
        This is currently a very slow process, if limit is set to 0 or a very
        high number.
        """
        all_streams = []
        for sih in self:
            for stream in sih.get_streams():
                if limit != 0 and len(all_streams) >= limit:
                    return all_streams
                all_streams.append(stream)
        return all_streams


class Stream(object):
    """
    Class Stream represents a Stream in TwitchTV
    """
    def __init__(self, stream_data):
        """
        :params: stream_data - stream data in JSON
        """
        if stream_data is None:
            raise AssertionError('received empty data')
        self._data = stream_data
        
        # stream is offline
        if self._data is None:
            self.online         = False
            self.channel        = None
            self.broadcaster    = None
            self.preview        = None
            self.stream_id      = None
            self.viewers        = 0
            self.display_name   = None
            self.status         = None
            self.game           = None
            self.url            = None

        # stream is online
        else:
            self.online         = True
            self.channel        = channels.Channel(self._data['channel'])
            self.broadcaster    = str(self._data.get('broadcaster'))
            self.preview        = str(self._data.get('preview'))
            self.stream_id      = str(self._data.get('_id'))
            self.viewers        = int(self._data.get('viewers', 0))
            self.display_name   = str(self.channel.display_name)
            self.status         = self.channel.status
            self.game           = str(self._data.get('game'))
            self.url            = str(self.channel.url)
