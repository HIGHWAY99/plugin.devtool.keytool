#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)
#############################################################################
#############################################################################
a=[]; n=False; 
#p=os.path.join(tP('special://home'),'userdata','Database')
p=tP('special://database')
dirs=os.listdir(p)
#popOK("This might a take while.","Building list.","Please be patient.","")
for f in dirs:
	#debob(['dir',f,os.path.join(p,f)])
	if (f.endswith('.db')) and (os.path.exists(os.path.join(p,f))==True) and (os.path.isfile(os.path.join(p,f))==True):
		#debob(['dir',f,os.path.join(p,f)])
		a.append(f)
if len(a) > 0:
	n=askSelection(a,"Select a file.")
if n:
		if not n==(0-1):
			debob(['n',n]); 
			s=a[n]
			debob(['n',n,'s',s]); 
			u=os.path.join(p,s)
			debob(['u',u]); 
			r=popYN("Safety Check.","Are you sure you want to remove this file.","","",n="no",y="yes")
			if r:
				os.remove(u)
				#shutil.rmtree(u)
				debob(['Attemping to remove file',u])
				popOK("Attempting to remove:","Remove file",u,s)
#############################################################################
#############################################################################
