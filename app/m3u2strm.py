#!/usr/bin/env python3
import tools
import streamClasses
import wget
import sys
import os
import shutil
import filecmp

provider = os.environ["provider"]
user = os.environ["user"]
pw = os.environ["pw"]
funct = os.environ["funct"]
tvListEnd = int(os.environ["tvlistend"])
eventListEnd = int(os.environ["eventlistend"])
tvPath = '/media/tvshows/'
moviePath = '/media/movies/'
eventPath = '/media/events/'
urltype = ''
providerUrl = ''
directory =  os.path.abspath(os.path.dirname(__file__))
if provider == 'apollo':
    providerUrl = 'https://tvnow.best/api/list/'+ user + '/' + pw + '/m3u8/'
print('...Starting Download...')
if funct == 'tv' or funct == 'all':
    urltype = 'tvshows'
    for i in range(1,tvListEnd):
        url = providerUrl + urltype +'/' + str(i)
        print(wget.download(url, ('m3u/apollotvshows-'+str(i)+'.m3u')))
        apollolist = streamClasses.rawStreamList('m3u/apollotvshows-'+str(i)+'.m3u')
        os.remove('m3u/apollotvshows-'+str(i)+'.m3u')
    print('comparing destination ', tvPath)
    c = filecmp.dircmp(directory+'/tvshows', tvPath)
    tools.compare_and_update(c)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('tvshows/')
if funct == 'events' or funct == 'all':
    urltype = 'events'
    for i in range(1,eventListEnd):
        url = providerUrl + urltype +'/' + str(i)
        print(wget.download(url, ('m3u/apolloevents-'+str(i)+'.m3u')))
        apollolist = streamClasses.rawStreamList('m3u/apolloevents-'+str(i)+'.m3u')
        os.remove('m3u/apolloevents-'+str(i)+'.m3u')
    print('comparing destination ', eventPath)
    c = filecmp.dircmp(directory+'/events', eventPath)
    tools.compare_and_update_events(c)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('events/')
if funct == 'latesttv' or funct == 'all':
    urltype = 'tvshows'
    print(wget.download(providerUrl+urltype, ('m3u/apollotvshows.m3u')))
    apollolist = streamClasses.rawStreamList('m3u/apollotvshows.m3u')
    os.remove('m3u/apollotvshows.m3u')
    print('comparing destination ', tvPath)
    c = filecmp.dircmp(directory+'/tvshows', tvPath)
    tools.compare_and_update(c)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('tvshows/')
if funct == 'movies' or funct == 'all':
    urltype = 'movies'
    print(wget.download(providerUrl+urltype, ('m3u/iptvmovies.m3u')))
    apollolist = streamClasses.rawStreamList('m3u/iptvmovies.m3u')
    os.remove('m3u/iptvmovies.m3u')
    print('comparing destination ', moviePath)
    c = filecmp.dircmp(directory+'/movies', moviePath)
    tools.compare_and_update_movies(c)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('movies/')
print('done')
