# SSTV-playlist
Generate a M3U8 playlist from an authenticated [SmoothStreamsTV URL](http://streamtvnow.tv/players/web_auth_old/index.php).  No affiliation with SmoothStreamsTV or StreamTVNow.

This program will output an M3U8 playlist file when fed an authenticated URL.  

It simply extracts the auth token from the authenticated URL and inserts it into an m3u8 template with the channel names/URLs from StreamTVNow.
