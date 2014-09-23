#!/usr/bin/env python
# whats_on.py 
# 
# Quick 'n dirty script that displays streams and links
import argparse

import colorama
import twitcher

GAMES = {'csgo': 'Counter-Strike: Global Offensive',
         'lol': 'League of Legends',
         'hearthstone': 'Hearthstone',
         'destiny': 'Destiny'}

def main():
    args = _arg_parser()

    t = twitcher.Twitcher()
    rs = t.get_stream_info(game=GAMES[args.game], limit=args.limit)
    all_streams = rs.get_all_streams(limit=args.limit)

    for stream in all_streams:
        print colorama.Fore.WHITE + \
            '........................................................................'
        print colorama.Fore.RED + stream.status
        print colorama.Fore.YELLOW + 'Viewers:     %d' % stream.viewers
        print colorama.Fore.BLUE + 'Url:         %s' % stream.url 
        print colorama.Fore.GREEN + 'Popout url:  %s' % stream.url + '/popout'


def _arg_parser():
    parser = argparse.ArgumentParser(description='parse game, limit')
    parser.add_argument('--game', help='target game', default='lol',
                        dest='game')
    parser.add_argument('--limit', help='limit of streams displayed', type=int,
                        default='10', dest='limit')
    return parser.parse_args()

if __name__ == '__main__':
    main()