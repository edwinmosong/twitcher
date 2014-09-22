twitcher
========

A simple Twitch TV API wrapper in Python.

## Description
This wrapper was created to be consumed by myself in creating an app that would
very easily display information about streams online and links to them. 

## Usage
Still a WIP (so implementation may change, this will be updated accordingly), 
but usage will be aimed to be super easy and simple.

Simply import twitcher and start using it!

```bash
>>> import twitcher
>>> twitcher = twitcher.Twitcher()
# get stream from riotgame's channel (case-sensitive)
>>> rito = twitcher.get_stream_info(channel='riotgames')
>>> rito_stream = rito.get_streams()[0]
>>> rito_stream.viewers
76327
>>> rito_stream.url
'http://www.twitch.tv/riotgames'
>>> rito_stream.game
'League of Legends'
```

To get all streams in a specific game:

```bash
>>> import twitcher
>>> twitcher = twitcher.Twitcher()
# get all CS:GO games
>>> csgo = twitcher.get_stream_info(game='Counter-Strike: Global Offensive')
>>> csgo
<twitcher.streams.StreamInfoHelper object at 0x107802d10>
```

Here's a great time to show how to iterate over streams from your query. The
default limit of streams retrieved is 25, but for games like Counter-Strike: GO
and League of Legends, the number of streams easily exceeds 25. Let's work off
of the CSGO example from above and limit our results to 5 streams. If you want to iterate over all results:

```
>>> for sih in csgo:
...     for stream in sih.get_streams():
...             print stream.status
...             print '>>>', stream.url
...             print '###', str(stream.viewers)
...
CS w/ @summit1g.
>>> http://www.twitch.tv/summit1g
### 11984
Short stream before practice
>>> http://www.twitch.tv/n0thingtv
### 2492
ScreaM - SaiyajiN Mod // New SubEmote // The Hype is real !
>>> http://www.twitch.tv/scream
### 1761
WarOwl Live! Games Overwatch and More!
>>> http://www.twitch.tv/warowl
### 975
Redline AWP Giveaway at 169,696 FOLLOWERS!
>>> http://www.twitch.tv/kittyplaysgames
### 774
shaffeR's short stream till gf home, then OVERNIGHT DRINKING STREAM
>>> http://www.twitch.tv/shaffer2369
### 504
REBROADCAST | SLTV S11
>>> http://www.twitch.tv/starladder5
### 488
ceh9 playing with Zeus and friends CS:GO
>>> http://www.twitch.tv/ceh9
### 358
...
```

The above example seems pretty silly if all you want is to retrieve all Stream objects. For this very reason, a convenience method `get_all_streams` is provided. You can optionally pass a limit parameter to limit how many Stream objects are retrieved. The limit parameter is there to avoid long wait times for games with a large number of streams. The default value is set to 50 (twice the normal limit). If you set limit=0, the method will grab all streams (not recommended).

```bash
>>> csgo
<twitcher.streams.StreamInfoHelper object at 0x107802d10>
>>> all_streams = csgo.get_all_streams(limit=33)
>>> len(all_streams)
33
>>> all_streams
[<twitcher.streams.Stream object at 0x106a630d0>, <twitcher.streams.Stream object at 0x106e107d0>, <twitcher.streams.Stream object at 0x106e10ad0>, <twitcher.streams.Stream object at 0x106ebfa50>, ...]
```

## To do
* Maybe implement users and user functionality
* Maybe support more resources in the TwitchTV api.
