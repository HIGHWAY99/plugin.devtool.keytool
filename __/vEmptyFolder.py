#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)
#############################################################################
#############################################################################
p=os.path.join(tP('special://home'),'addons','packages')
r=popYN("Safety Check.","Are you sure you want to empty this folder ","of all contents within it.","",n="no",y="yes")
if r:
	if (os.path.exists(p)==True) and (os.path.isdir(p)==True):
		debob(['p',p])
		shutil.rmtree(p)
		xbmc.sleep(2000)
		FolderNEW(p)
		popOK("Folder emptied, removed, and remade.","Finished.","","")
#############################################################################
#############################################################################
