#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)
#############################################################################
#############################################################################
#p=os.path.join(tP('special://home'),'userdata','Thumbnails')
#p=tP('special://home')
r=popYN("Safety Check.","Are you sure you want to empty this folder ","of all contents within it.","Remember to change to Confluence skin first.",n="no",y="yes"); 
if r:
	a=[]; p1=tP('special://home'); 
	dirs=os.listdir(p1); 
	for f in dirs:
		p2=os.path.join(p1,f); 
		if (os.path.exists(p2)==True) and (os.path.isdir(p2)==True):
			a.append(p2); 
	a.append(os.path.join(tP('special://home'),'addons')); 
	a.append(tP('special://database')); 
	a.append(tP('special://userdata')); 
	a.append(tP('special://thumbnails')); 
	a.append(tP('special://temp')); 
	a.append(os.path.join(tP('special://home'),'cache')); 
	for p in a:
		try:
			if (os.path.exists(p)==True) and (os.path.isdir(p)==True):
				shutil.rmtree(p); 
				debob(['path removed',p]); 
				xbmc.sleep(1000); 
				FolderNEW(p); 
		except:
			debob(['path error *',p]); 
	xbmc.executebuiltin("XBMC.UpdateLocalAddons()"); 
	popOK("Folder(s) emptied, removed, and remade.","Finished.","This would be a good time to restart Kodi (XBMC).","")
#############################################################################
#############################################################################
