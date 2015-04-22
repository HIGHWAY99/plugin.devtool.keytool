#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)
import dHiddenDownloader
import dExtract
#############################################################################
#############################################################################
tFolder=tP('special://temp'); tFile='temp.zip'; tBoth=os.path.join(tFolder,tFile); 
UnpackDest=tP('special://home'); 
#UnpackDest=os.path.join(tP('special://home'),'addons'); 
u=showkeyboard("","Please give the url of an image:"); 
debob(['u',u]); 
if len(u) > 11:
	r=popYN("Safety Check.","Are you sure you want to download and extract ","all contents within it.","",n="no",y="yes"); 
	if r:
		dp=xbmcgui.DialogProgress(); dp.create(AddonTitle,"Downloading ",'','Please Wait')
		if isFile(u)==False:
			debob([u,tFile,tFolder]); 
			dDownloader.download(u,tFile,tFolder,dp); 
		if isFile(tBoth):
			debob(['UnpackDest',UnpackDest]); 
			dp.update(0,"","Extracting Zip Please Wait"); 
			dExtract.all(tBoth,UnpackDest,dp); 
			r2=popYN("Safety Check.",'Would you like to delete "temp.zip"?',"","",n="no",y="yes"); 
			if r2:
				os.remove(tBoth); 
#############################################################################
#############################################################################
