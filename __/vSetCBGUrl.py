#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)
import dHiddenDownloader
fExt='.png'
#############################################################################
#############################################################################
u=showkeyboard("","Please give the url of an image:"); 
n=os.path.join(tP('special://home'),'media','bgWallpaper'+fExt); 
debob(['u',u]); debob(['n',n]); 
dHiddenDownloader.download(u,'bgWallpaper'+fExt,os.path.join(tP('special://home'),'media'),useResolver=False); 
xbmc.sleep(4000); 
DoE('Skin.SetString(%s,%s)'%('CustomBackgroundPath',n)); 
DoE('Skin.SetBool(%s)'%'UseCustomBackground'); 
#############################################################################
#############################################################################
