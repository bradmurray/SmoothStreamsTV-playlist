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
            print ("Playlist built successfully, located at:")
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
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch21.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 22
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch22.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 23
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch23.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 24
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch24.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 25
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch25.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 26
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch26.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 27
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch27.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 28
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch28.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 29
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch29.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 30
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch30.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 31
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch31.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 32
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch32.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 33
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch33.smil/playlist.m3u8?wmsAuthSign={AuthSign}
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
#EXTINF:-1, 56
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch56.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 57
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch57.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 58
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch58.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 59 Cinemax East (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch59.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 60 Cinemax 5 Star (DirecTV)
http://dnaw1.smoothstreams.tv:9100/viewstvn/ch60.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 61
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch61.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 62
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch62.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 63
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch63.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 64
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch64.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 65
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch65.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 66
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch66.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 67
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch67.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 68
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch68.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 69
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch69.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 70
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch70.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 71
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch71.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 72
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch72.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 73
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch73.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 74
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch74.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 75
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch75.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 76
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch76.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 77
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch77.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 78
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch78.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 79
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch79.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 80
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch80.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 81
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch81.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 82
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch82.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 83
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch83.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 84
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch84.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 85
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch85.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 86
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch86.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 87
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch87.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 88
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch88.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 89
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch89.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 90
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch90.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 91
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch91.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 92
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch92.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 93
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch93.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 94
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch94.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 95
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch95.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 96
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch96.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 97
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch97.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 98
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch98.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 99
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch99.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 100
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch100.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 101
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch101.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 102
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch102.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 103
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch103.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 104
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch104.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 105
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch105.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 106
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch106.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 107
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch107.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 108
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch108.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 109
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch109.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 110
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch110.smil/playlist.m3u8?wmsAuthSign={AuthSign}
#EXTINF:-1, 111
#http://dnaw1.smoothstreams.tv:9100/viewstvn/ch111.smil/playlist.m3u8?wmsAuthSign={AuthSign}
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
