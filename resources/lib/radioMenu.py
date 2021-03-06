# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import os
import sys
import re
import urllib
import urllib2 
import cookielib

__addon__           = xbmcaddon.Addon()
__addon_id__        = __addon__.getAddonInfo('id')
__addonname__       = __addon__.getAddonInfo('name')
__icon__            = __addon__.getAddonInfo('icon')
__addonpath__       = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__            = __addon__.getLocalizedString
__path__            = os.path.join(__addonpath__, 'resources', 'lib' )
__path_img__        = os.path.join(__addonpath__, 'resources', 'media' )

sys.path.append(__path__)
sys.path.append (__path_img__)

class Main:
        
    def start(self, selfGet):
    
        # vars
        self = selfGet
        
        list = [
		['Slovenské rádia', sys.argv[0] + '?sk', 'radioSlovakia.png', ''],
        ['České rádia', sys.argv[0] + '?cz', 'radioCzechRepublic.png', ''],
		['Top 10 SK', sys.argv[0] + '?topSK', 'favouriteSK.png', ''],
		['Top 10 CZ', sys.argv[0] + '?topCZ', 'favouriteCZ.png', ''],
            ]
                
        for v in list:
            listItem = xbmcgui.ListItem(label=v[0], iconImage=__path_img__ + '//' + v[2])
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=v[1], listitem=listItem, isFolder=True)
        
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        if self.opt != '':
            
            Title = list[int(self.opt)][0]
            Icon = list[int(self.opt)][2]
            URL = list[int(self.opt)][3]
            
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            