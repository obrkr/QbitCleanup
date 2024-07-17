#!/usr/bin/python3

# Needs to have
# pip3 install qbittorrent-api

from qbittorrentapi import Client
client = Client(host='localhost:10764', username='username', password='password')

torrent_list = client.torrents.info()
categories = client.torrent_categories.categories

for torrent in torrent_list:
    for status in torrent.trackers:
        if '4K-Remux' in torrent.category and ('Nuked' in status.msg or 'not registered' in status.msg or 'Trumped' in status.msg):
            print(torrent.name,' ',status.msg,' ',torrent.category)
            torrent.delete(hash=(torrent.hash),delete_files=True)
