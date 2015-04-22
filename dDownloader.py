### ############################################################################################################
###	#	
### # Author: 			#		The Highway
### # Description: 	#		Downloader File For:  Glitch (Key Tool)
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import common
from common import *
def download(url,destfile,destpath,dp=None):
    if not dp: dp=xbmcgui.DialogProgress(); dp.create(addonName,"Downloading & Copying File",' ',' '); 
    dp.update(0); destpath=tP(destpath)
    if isPath(destpath)==False: os.mkdir(destpath)
    urllib.urlretrieve(url,os.path.join(destpath,destfile),lambda nb,bs,fs,url=url: _progressbarhook(nb,bs,fs,url,dp)); 
def _progressbarhook(Numblocks,BlockSize,FileSize,url,dp):
    try: percent=min((Numblocks*BlockSize*100)/FileSize,100); dp.update(percent); 
    except: percent=100; dp.update(percent); 
    if dp.iscanceled(): raise Exception("Canceled"); dp.close(); 