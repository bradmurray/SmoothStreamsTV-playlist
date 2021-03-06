#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''generate an m3u8 playlist with your SmoothStreamsTV credentials'''

from getpass import getpass
from json import loads, dumps
from os import path
from urllib import urlopen, urlencode
import time

__appname__ = 'SSTV-playlist'
__author__ = 'Stevie Howard (stvhwrd)'
__copyright__ = 'Copyright 2016, Stevie Howard'
__credits__ = ['Stevie Howard']
__license__ = 'MIT'
__version__ = '0.1beta'
__maintainer__ = 'Stevie Howard'
__email__ = 'stvhwrd@uvic.ca'
__status__ = 'Beta'


greeting = '''
WELCOME to the SmoothStreamsTV playlist generator!

This program will generate an .m3u8 playlist file with all available channels
for the SmoothStreamsTV IPTV provider, playable in media players and browsers.
Please note: channel names/numbers are sourced from SmoothStreamsTV,
and current as of September 25, 2016.
'''


def main():
    # ENTER YOUR CREDENTIALS BELOW
    # example: username = 'sampleuser@email.com'
    # example: password = 'psswrd1234!'
    username = ''
    password = ''

    # CHOOSE YOUR SERVER HERE (see list below)
    # example for US West:  server = 'dnaw'
    server = ''

    servers = {
        'EU Random': 'deu',
        'EU DE-Frankfurt': 'deu.de1',
        'EU NL-EVO': 'deu.nl2',
        'EU NL-i3d': 'deu.nl1',
        'EU UK-London': 'deu.uk',
        'US Random': 'dna',
        'US East': 'dnae',
        'US West': 'dnaw',
        'US East-NJ': 'dnae1',
        'US East-VA': 'dnae2',
        'US East-CAN': 'dnae3',
        'US East-CAN2': 'dnae4',
        'Asia': 'dsg'
    }

    # If you have not hardcoded your credentials (above),
    # you will be prompted for them on each run.
    if not username or not password:
        colourPrint('bold', greeting)
        username, password = getCredentials()

    authSign = getAuthSign(username, password)

    if not server:
        server = getServer(servers)

    colourPrint('yellow',
                '\nPlease wait, generating playlist.')

    playlistText = generatePlaylist(server, authSign)
    playlistFile = buildPlaylistFile(playlistText)
# end main()


def getAuthSign(un, pw):
    '''request JSON from server and return hash'''

    baseUrl = 'http://smoothstreams.tv/schedule/admin/dash_new/hash_api.php?'

    params = {
        "username": un,
        "password": pw,
        "site": "viewstvn"
    }

    url = baseUrl + urlencode(params)

    try:
        response = urlopen(url).read().decode('utf-8')
        data = loads(response)
        if data['hash']:
            colourPrint('green',
                        'Thank you, authentication complete.\n')
            return data['hash']

    except ValueError:
        colourPrint('red',
                    'Unable to retrieve data from the server.\n' +
                    'Please check your internet connection and try again.')
        exit(1)
    except KeyError:
        colourPrint('red',
                    'There was an error with your credentials.\n' +
                    'Please double-check your username and password,' +
                    ' and try again.')
        exit(1)
# end getAuthSign()


def getCredentials():
    '''prompt user for username and password'''

    colourPrint('bold',
                ('You may wish to store your credentials and server preferences in this file ' +
                 'by opening it in a text editor and filling in the username, password, and ' +
                 'server fields.  If you choose not to do this, you will be prompted for ' +
                 'this information on each run of this script.'))

    colourPrint('yellow',
                '\nPlease enter your username for SmoothStreamsTV:')
    username = raw_input('')
    colourPrint('green',
                '\nThank you, ' + username + '.\n')

    colourPrint('yellow',
                '\nPlease enter your password for SmoothStreamsTV:')
    password = getpass('')

    return username, password
# end getCredentials()


def getServer(servers):
    '''prompt user to choose closest server'''

    validServer = False

    colourPrint('yellow',
                '\nServer options:')
    colourPrint('yellow',
                dumps(servers, sort_keys=True, indent=4))
    print('Example, for US West: enter "dnaw" (without the quotes)\n')
    colourPrint('yellow',
                '\nPlease choose your server:')
    server = raw_input('')
    for key, value in list(servers.items()):
        # cheap and dirty alternative to regex
        if server in value and len(value) == len(server):
            validServer = True
            colourPrint('green',
                        '\nYou have chosen the ' + key + ' server.\n')
            break

    if not validServer:
            colourPrint('red',
                        ('\n"' + value + '" is not a recognized server.' +
                         ' The playlist will be built with "' + value + '",' +
                         ' but may not work as expected.\n'))

    return (server)
# end getServer()


def buildPlaylistFile(body):
    '''write playlist to a new local m3u8 file'''

    title = 'SmoothStreamsTV.m3u8'

    # open file to write, or create file if DNE, write <body> to file and save
    with open(title, 'w+') as f:
        f.write(body)
        f.close()

    # check for existence/closure of file
    if f.closed:
        colourPrint('yellow',
                    '\nPlaylist built successfully, located at: ')
        colourPrint('underline',
                    path.abspath(title))
        exit(0)
    else:
        raise FileNotFoundError
# end buildPlaylistFile()


def generatePlaylist(server, authSign):
    '''build string of channels in m3u8 format based on global channelDictionary'''

    m3u8 = '#EXTM3U\n'
    # iterate through channels in channel-number order
    for channel in sorted(channelDictionary, key=lambda channel: int(channel)):
        m3u8 += ('#EXTINF:-1, ' + channel +
                 ' ' + channelDictionary[channel] +
                 '\n' + 'http://' + server +
                 '.smoothstreams.tv:9100/viewstvn/ch' + channel +
                 'q1.stream/playlist.m3u8?wmsAuthSign=' + authSign + '\n')

    return m3u8
# end generatePlaylist()


class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def colourPrint(spec, text):
    '''print text with specified formatting effect'''

    text = str(text)
    if spec.upper() == 'BOLD':
        print(colour.BOLD + text + colour.END)
    elif spec.upper() == 'GREEN':
        print(colour.GREEN + text + colour.END)
    elif spec.upper() == 'YELLOW':
        print(colour.YELLOW + text + colour.END)
    elif spec.upper() == 'RED':
        print(colour.RED + text + colour.END)
    elif spec.upper() == 'PURPLE':
        print(colour.PURPLE + text + colour.END)
    elif spec.upper() == 'CYAN':
        print(colour.CYAN + text + colour.END)
    elif spec.upper() == 'DARKCYAN':
        print(colour.DARKCYAN + text + colour.END)
    elif spec.upper() == 'BLUE':
        print(colour.BLUE + text + colour.END)
    elif spec.upper() == 'UNDERLINE':
        print(colour.UNDERLINE + text + colour.END)
# end colourPrint()


channelDictionary = {
    '01': 'ESPNews',
    '02': 'ESPN',
    '03': 'ESPN 2',
    '04': 'ESPN U',
    '05': 'Fox Sports 1',
    '06': 'Fox Sports 2',
    '07': 'NFL Network',
    '08': 'NBA TV',
    '09': 'MLB Network',
    '10': 'NHL Network',
    '11': 'NBC Sports Network',
    '12': 'Golf Channel',
    '13': 'Tennis Channel',
    '14': 'CBS Sports Network',
    '15': 'Fight Network',
    '16': 'WWE Network',
    '17': 'Sportsnet World',
    '18': 'Sportsnet 360',
    '19': 'Sportsnet Ontario',
    '20': 'Sportsnet One',
    '21': 'TSN 1',
    '22': 'beIN US',
    '23': 'Univision Deportes',
    '24': 'ESPN Deportes',
    '25': 'USA Network',
    '26': 'Viceland',
    '27': 'Destination America',
    '28': 'TBS',
    '29': 'TNT',
    '30': 'SyFy',
    '31': 'Spike',
    '32': 'Cartoon Network East',
    '33': 'A&E',
    '34': 'NBC East (Buffalo)',
    '35': 'CBS East (Buffalo)',
    '36': 'ABC East (Buffalo)',
    '37': 'Fox East (Buffalo)',
    '38': 'CNN',
    '39': 'CNBC',
    '40': 'Fox News 360',
    '41': 'History Channel',
    '42': 'Discovery Channel',
    '43': 'National Geographic',
    '44': 'FX',
    '45': 'FXX',
    '46': 'Comedy Central',
    '47': 'AMC',
    '48': 'HBO East',
    '49': 'HBO Comedy',
    '50': 'HBO Signature',
    '51': 'HBO Zone',
    '52': 'ShowTime East',
    '53': 'ActionMax HD East',
    '54': 'Cinemax Moremax',
    '55': 'Starz Cinema',
    '56': 'Starz East',
    '57': '',
    '58': '',
    '59': 'Cinemax East',
    '60': 'Cinemax 5 Star',
    '61': '',
    '62': '',
    '63': '',
    '64': '',
    '65': '',
    '66': '',
    '67': '',
    '68': '',
    '69': '',
    '70': '',
    '71': '',
    '72': '',
    '73': '',
    '74': '',
    '75': '',
    '76': '',
    '77': '',
    '78': '',
    '79': '',
    '80': '',
    '81': '',
    '82': '',
    '83': '',
    '84': '',
    '85': '',
    '86': '',
    '87': '',
    '88': '',
    '89': '',
    '90': '',
    '91': '',
    '92': '',
    '93': '',
    '94': '',
    '95': '',
    '96': '',
    '97': '',
    '98': '',
    '99': '',
    '100': '',
    '101': '',
    '102': '',
    '103': '',
    '104': '',
    '105': '',
    '106': '',
    '107': '',
    '108': '',
    '109': '',
    '110': '',
    '111': '',
    '112': 'Sky Sports News HQ',
    '113': 'Sky Sports 1 UK',
    '114': 'Sky Sports 2 UK',
    '115': 'Sky Sports 3 UK',
    '116': 'Sky Sports 4 UK',
    '117': 'Sky Sports 5 UK',
    '118': 'Sky Sports F1 UK',
    '119': 'MMA 1 Slot (FightPass etc)',
    '120': 'MMA 2 Slot (Overflow if necessary)'
}


if __name__ == '__main__':
    main()
