#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''generate an m3u8 playlist from a single URL'''

import re, time
from subprocess import call


__appname__ = 'SmoothStreamsTV-playlist-generator'
__author__ = 'Stevie Howard (stvhwrd)'
__version__ = '0.0pre0'
__license__ = 'MIT'


def main():
    '''higher level program controller'''
    try:
        print(instructions)

        # prompt user to input their authenticated URL
        URL = raw_input('\n')
        token = str(extractToken(URL))

        # inject current token into m3u8 skeleton
        m3u8Body = insertToken(m3u8Skeleton, authSignPlaceholder, token)

        # build and output the playlist file
        buildPlaylistFile(m3u8Body)

        # confirm success
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
#end main


def extractToken(URL):
    '''extract the token from the provided URL using regular expressions'''
    try:
        p = re.compile(ur'wmsAuthSign=(.+?)$', re.MULTILINE)
        token = re.findall(p, URL)
        return (token[0])
    except AttributeError:
        # AuthSign not found in the URL
        found = ''
        print ('Unable to extract token.')
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
#end extractToken


def insertToken(targetString, pattern, insertion):
    '''replace all instances of <pattern> in <targetString> with <insertion>'''
    return targetString.replace(pattern, insertion)
#end insertToken


def buildPlaylistFile(body):
    '''write playlist textbody to a new local m3u8 file'''
    try:
        # title will be the current date in yyyy/mm/dd format
        date = str(time.strftime('%Y-%m-%d'))
        title = 'SmoothStreamsTV_' + date + '.m3u8'

        # create file with subprocess.call (to call shell functions)
        call(['touch', title])

        # open file or create file if DNE, write <body> to file and save
        with open(title, 'w+') as f:
            f.write(body)
            f.flush()
            f.close()

        # check for existence/closure of file
        if f.closed:
            print ("\n\nPlaylist built successfully, located at: ")
            call(['pwd'])
        else:
            raise FileNotFoundError

    except:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
#end buildPlaylistFile


# specify placeholder for actual Auth Sign
authSignPlaceholder = '{AuthSign}'


# text body of m3u8, missing only the Auth Sign
m3u8Skeleton = '''
#EXTM3U
#EXTINF:-1, 01 ESPNews (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch01.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 02 ESPN (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch02.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 03 ESPN 2 (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch03.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 04 ESPN U (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch04.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 05 Fox Sports 1 (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch05.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 06 Fox Sports 2 (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch06.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 07 NFL Network (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch07.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 08 NBA TV (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch08.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 09 MLB Network (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch09.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 10 NHL Network (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch10.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 11 NBC Sports Network (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch11.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 12 Golf Channel (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch12.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 13 Tennis Channel (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch13.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 14 CBS Sports Network (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch14.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 15 Fight Network (Bell)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch15.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 16 WWE Network (Bell)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch16.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 17 Sportsnet World (Bell)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch17.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 18 Sportsnet 360 (Bell)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch18.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 19 Sportsnet Ontario (Bell)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch19.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 20 Sportsnet One (Bell)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch20.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 21 TSN 1 (Bell)
# Empty channels
#EXTINF:-1, 34 NBC East (Buffalo)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch34.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 35 CBS East (Buffalo)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch35.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 36 ABC East (Buffalo)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch36.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 37 Fox East (Buffalo)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch37.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 38 CNN
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch38.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 39 CNBC
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch39.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 40 Fox News 360
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch40.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 41 History Channel (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch41.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 42 Discovery Channel (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch42.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 43 National Geographic (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch43.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 44 FX (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch44.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 45 FXX (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch45.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 46 Comedy Central (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch46.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 47 AMC (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch47.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 48 HBO East (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch48.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 49 HBO Comedy (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch49.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 50 HBO Signature (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch50.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 51 HBO Zone (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch51.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 52 ShowTime East (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch52.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 53 ActionMax HD East (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch53.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 54 Starz Cinema (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch54.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 55 Starz East
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch55.smil/playlist.m3u8?wmsAuthSign={AuthSign}
# Empty channels
#EXTINF:-1, 59 Cinemax East (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch59.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 60 Cinemax 5 Star (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch60.smil/playlist.m3u8?wmsAuthSign={AuthSign}
# Empty channels
#EXTINF:-1, 112 Sky Sports News HQ
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch112.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 113 Sky Sports 1 UK
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch113.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 114 Sky Sports 2 UK
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch114.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 115 Sky Sports 3 UK
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch115.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 116 Sky Sports 4 UK
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch116.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 117 Sky Sports 5 UK
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch117.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 118 Sky Sports F1 UK
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch118.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 119 MMA 1 Slot (FightPass etc)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch119.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 120 MMA 2 Slot (Overflow if necessary)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch120.smil/playlist.m3u8?wmsAuthSign={AuthSign}
'''


instructions = '''
WELCOME to the SmoothStreamsTV playlist generator!

This program will generate an .m3u8 playlist file with all available channels for the SmoothStreamsTV IPTV \
provider, playable in media players and browsers.
Please note: channel names and listings are sourced from SmoothStreamsTV, and current as of September 5, 2016.

1. Please ensure that you are signed into SmoothStreamsTV, and go to this page:

        http://streamtvnow.tv/players/web_auth_old/index.php

2. Click on the VLC traffic cone icon and copy the URL from the 'HLS' box to your clipboard.

    Example:
        http://dnaw1.smoothstreams.tv:9100/viewstvn/ch19.smil/playlist.m3u8?wmsAuthSign=c2VydmVyX3RpbWU9O...

3. Paste the full URL here (and press return):
'''


if __name__ == '__main__':
    main()
