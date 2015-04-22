#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)
#############################################################################
#############################################################################
#p=os.path.join(tP('special://home'),'userdata','Thumbnails')
#p=tP('special://home')
p1=tP('special://home'); 
r=popYN("Safety Check.","Are you sure you want to empty this folder ","of all contents within it.","Remember to change to Confluence skin first.",n="no",y="yes"); 
if r:
	for root,dirs,files in os.walk(p1,topdown=False):
		try:
			for name in files:
				try:
					if name in ['kodi.log','kodi.old.log','xbmc.log','xbmc.old.log']:
						pass
					elif (name.endswith('.db')) and ((name.startswith('Textures')) or (name.startswith('Addons')) or (name.startswith('MyVideos')) or (name.startswith('MyMusic')) or (name.startswith('ViewModes')) or (name.startswith('commoncache'))): # or (name.startswith(''))
						pass
					elif (name.endswith('.xml')) and ('keymaps' in root):
						pass
					elif addonId in root: ## Keeps This Addon ##
						pass
					else:
						try: os.remove(os.path.join(root,name))
						except: pass
				except: pass
		except: pass
		try:
			for name in dirs:
				try:
					if name in ['userdata','Database','keymaps','system','addons','packages']:
						pass
					elif addonId in root: ## Keeps This Addon ##
						pass
					elif addonId in name: ## Keeps This Addon ##
						pass
					else:
						try: os.rmdir(os.path.join(root,name))
						except: pass
				except: pass
		except: pass
	xbmc.executebuiltin("XBMC.UpdateLocalAddons()"); 
	popOK("Folder(s) emptied, removed, and remade.","Finished.","This would be a good time to restart Kodi (XBMC).","")
#############################################################################
#############################################################################
