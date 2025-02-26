#!/usr/bin/python3

# Needs to have
# pip3 install qbittorrent-api

from qbittorrentapi import Client
client = Client(host='localhost:10764', username='username', password='password')

torrent_list = client.torrents.info()

for torrent in torrent_list:
    for status in torrent.trackers:
        if 'Unregistered torrent' in status.msg:
            print(torrent.name,' ',status.msg)
            torrent.delete(hash=(torrent.hash),delete_files=True)
