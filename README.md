twitcher
========

A simple Twitch TV API wrapper in Python.

## Description
This wrapper was created to be consumed by myself in creating an app that would
very easily display information about streams online and links to them. 

## Usage
Still a WIP (so implementation may change, this will be updated accordingly), 
but usage will be aimed to be super easy and simple:

```bash
>>> import twitcher
>>> twitcher = twitcher.Twitcher()
# get stream from RiotGame's channel
>>> rito = twitcher.get_stream_info('RiotGames')
>>> rito.online
True
>>> rito.viewers
100000
>>> rito.game
'League of Legends'
```

To get all streams in a specific game:

```bash
>>> import twitcher
>>> twitcher = twitcher.Twitcher()
# get all CS:GO games
>>> csgo = twitcher.get_streams(game='Counter-Strike: Global Offensive')
>>> csgo
[<classes.Stream>, <classes.Stream>, ...]
```

## To do
* Maybe implement users and user functionality
* Maybe support more resources in the TwitchTV api.
