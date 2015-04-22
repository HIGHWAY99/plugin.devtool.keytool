#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)
import dHiddenDownloader
#############################################################################
#############################################################################
u=showkeyboard("","Please give the url of an image:"); 
n=os.path.join(tP('special://home'),'media','Splash.png'); 
debob(['u',u]); debob(['n',n]); 
dHiddenDownloader.download(u,'Splash.png',os.path.join(tP('special://home'),'media'),useResolver=False); 
shutil.copyfile(u,n); 
#############################################################################
#############################################################################
