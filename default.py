#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)

#############################################################################
#############################################################################
ACTION_PREVIOUS_MENU 		=  10	## ESC action
ACTION_NAV_BACK 				=  92	## Backspace action
ACTION_MOVE_LEFT 				=   1	## Left arrow key
ACTION_MOVE_RIGHT 			=   2	## Right arrow key
ACTION_MOVE_UP 					=   3	## Up arrow key
ACTION_MOVE_DOWN 				=   4	## Down arrow key
ACTION_MOUSE_CLICK_LEFT	= 101	## Mouse click left ??
ACTION_MOUSE_WHEEL_UP 	= 104	## Mouse wheel up
ACTION_MOUSE_WHEEL_DOWN = 105	## Mouse wheel down
ACTION_MOUSE_DRAG 			= 106	## Mouse drag
ACTION_MOUSE_MOVE 			= 107	## Mouse move
#
ACTION_KEY_P						=	 79	## P - Pause
ACTION_KEY_R						=	 78	## R - Rewind
ACTION_KEY_F						=	 77	## F - Fast Forward
ACTION_SELECT_ITEM			=		7	## ?
ACTION_PARENT_DIR				=		9	## ?
ACTION_CONTEXT_MENU			=	117	## ?
ACTION_NEXT_ITEM				=	 14	## ?
ACTION_BACKSPACE				=	110	## ?
#
ACTION_KEY_X						=	 13	## X - Stop
ACTION_aID_0						=	  0	## ???
#
ACTION_REMOTE_MUTE					=	 91	## MUTE
#ACTION_REMOTE_FULLSCREEN		=	 ??	## FullScreen
ACTION_REMOTE_INFO					=	 11	## Info
ACTION_REMOTE_PLAYPAUSE			=	 12	## Play / Pause
ACTION_REMOTE_CONTEXTMENU		=	117	## Context Menu
ACTION_REMOTE_STOP					=	 13	## Stop
#
ACTION_KEY_VOL_MINUS				=	 89	## F - Fast Forward
ACTION_KEY_VOL_PLUS					=	 88	## F - Fast Forward
#
ACTION_SHOW_FULLSCREEN			=  36 ## Show Full Screen
ACTION_TOGGLE_FULLSCREEN		= 199 ## Toggle Full Screen
#############################################################################
#############################################################################

d=xbmcgui.Dialog(); 

class CustomWindow(xbmcgui.WindowXML):
#class CustomWindow(xbmcgui.WindowXMLDialog):
		closing=False; firsttime=False; c={}; strXMLname=''; strFallbackPath=''; List01D=[]; List01DB=[]
		maxW=1280; maxH=720; 
		##
		def __init__(self,strXMLname,strFallbackPath):
			self.strXMLname=strXMLname
			self.strFallbackPath=strFallbackPath
		def onInit(self):
			#try:
				try: self.wID=xbmcgui.getCurrentWindowId()
				except: self.wID=0
				deb('CurrentWindowId()',str(self.wID)); 
				deb('getResolution()',str(self.getResolution())); 
				self.firsttime=True
				debob(['screen size',self.getWidth(),self.getHeight()])
				debob(['skin size',self.maxW,self.maxH])
				self.LoadSkinItems()
				try: self.setFocus(self.bExit)
				except: pass
				self.setupScreen()
				try: self.setFocus(self.List01)
				except: pass
			#except: pass
		def ResetTheList(self):
			#try: 
#				PlaySndWav('cards_shuffling')
				self.ScrTp('0','erCount'); 
				self.List01.reset(); 
#				self.List02.reset(); 
#				self.List03.reset(); 
				self.List01DB=[]; #self.ErrLabel01.setLabel(' '); 
				self.List01D=[]; 
#				self.DeckImage=iDeck()
#				self.ImgCard01.setImage(self.DeckImage)
#				self.ImgCard02.setImage(self.DeckImage)
#				self.CardNo1=''
#				self.CardNo2=''
			#except: pass
		def saveFileArray(self):
			#try:
				html=str(self.FileArray)
				FileSAVE(self.UrlFile,html)
				pass
			#except: pass
		def loadFileArray(self):
			#try:
				if isPath(addonUserDataPathTP)==False:
						try: os.mkdir(addonUserDataPathTP)
						except: pass
				#self.UrlFile=addonProfile2('urls.txt')
				self.UrlFile=addonPath2('urls.txt')
				try: html=FileOPEN(self.UrlFile)
				except: html=''
				if html=='': html='[]'; #FileSAVE(self.UrlFile,html)
				self.FileArray=eval(html)
				
				self.reloadFileArray()
			#except: pass
		def reloadFileArray(self):
			#try:
				self.ResetTheList()
				iCount=0
				for UrlData in self.FileArray:
					#try:
						#debob(UrlData); 
						try: Title=UrlData['Title']
						except: Title=''
						try: Thumb=UrlData['Thumb']
						except: Thumb=''
						try: Url=UrlData['Url']
						except: Url=''
						try: iAction=UrlData['Action']
						except: iAction=''
						try: Desc=UrlData['Desc']
						except: Desc=''
						try: ItemDate=UrlData['Date']
						except: ItemDate=''
						if Title=='': Title=''+Url
						#debob(['Title',Title,'Url',Url,'ItemDate',ItemDate,'Thumb',Thumb]); 
						item=xbmcgui.ListItem(Title); 
						if Thumb.startswith('special://'): Thumb=tP(Thumb)
						item.setThumbnailImage(Thumb); 
						item.setLabel(Title); 
						item.setLabel2(Desc); 
						item.setProperty('ItemDate',str(ItemDate)); 
						item.setProperty('iCount',str(iCount)); 
						item.setProperty('ItemTitle',str(Title)); 
						item.setProperty('ItemUrl',str(Url)); 
						item.setProperty('ItemAction',str(iAction)); 
						item.setProperty('ItemDesc',str(Desc)); 
						
						self.List01.addItem(item); 
						iCount=iCount+1; 
						pass
					#except: pass
				
				
				
				
				
				pass
			#except: pass
		def setupScreen(self):
			#try:
				#self.iBack.setImage(artp("black1")); 
				#self.iBackground.setImage(MediaFile("black1.png")); 
				self.iBack.setImage(MediaFile("black1.png")); 
				self.iBackground.setImage(addonFanart); 
				
				#wegweg
				#return
				#self.loadLogFile()
#				self.loadCardList()
				self.loadFileArray()
				
				
				##
			#except: pass
		def LoadSkinItems(self):
			try:
				self.c['iBack']=1; 
				self.c['iBackground']=2; 
				self.c['bExit']=10; 
				try: self.iBack=self.getControl(self.c['iBack']); 
				except: pass
				try: self.iBackground=self.getControl(self.c['iBackground']); 
				except: pass
				try: self.bExit=self.getControl(self.c['bExit']); 
				except: pass
				
				self.c['List01']=9000; 
				try: self.List01=self.getControl(self.c['List01']); 
				except: pass
#				self.c['List02']=9001; 
#				try: self.List02=self.getControl(self.c['List02']); 
#				except: pass
#				self.c['List03']=9002; 
#				try: self.List03=self.getControl(self.c['List03']); 
#				except: pass
				self.c['ErrLabel02']=101; 
				try: self.ErrLabel02=self.getControl(self.c['ErrLabel02']); 
				except: pass
#				self.c['ErrLabel03']=102; 
#				try: self.ErrLabel03=self.getControl(self.c['ErrLabel03']); 
#				except: pass
				self.c['BtnTopMenu01']=400; 
				try: self.BtnTopMenu01=self.getControl(self.c['BtnTopMenu01']); 
				except: pass
				self.c['BtnTopMenu02']=401; 
				try: self.BtnTopMenu02=self.getControl(self.c['BtnTopMenu02']); 
				except: pass
				self.c['BtnTopMenu03']=402; 
				try: self.BtnTopMenu03=self.getControl(self.c['BtnTopMenu03']); 
				except: pass
				
				#self.ScrTp('0','erCount'); 
				
				
				
			except: pass
		def ScrTp(self,s='',v='ScreenType'):
			try:
				if len(v) > 0:
					self.setProperty(v,s); 
			except: pass
		def onClick(self,controlId):
			#try:
				if   controlId==self.c['bExit']: self.AskToClose()
				#elif   controlId==self.c['SideGroup01ocBtn']: 
				#	gX=self.SideGroup01.getX(); gY=self.SideGroup01.getY(); 
				#	debob(['From',gX,gY])
				#	if gX==self.maxW: self.SideGroup01.setPosition(1030,gY); debob(['To',1030,gY])
				#	else: self.SideGroup01.setPosition(self.maxW,gY); debob(['To',self.maxW,gY])
				#	
				#	pass
				elif   controlId==self.c['BtnTopMenu01']: ## Add Url ##
					try:
						#print "test0"
#						self.loadCardList()
						#print "test1"
						iCount=int(self.List01.getSelectedItem().getProperty('iCount')); 
						ItemDate=self.List01.getSelectedItem().getProperty('ItemDate'); 
						Img=self.List01.getSelectedItem().getProperty('Img'); 
						Name=self.List01.getSelectedItem().getLabel(); 
						Url=self.List01.getSelectedItem().getLabel2(); 
						self.useUrlItem(iCount,Name,Url,ItemDate,Img,'Add')
						pass
					except:
						iCount=0-1; Name=''; Url=''; ItemDate=''; Img=''; 
					#try:
					self.useUrlItem(iCount,Name,Url,ItemDate,Img,'Add')
					#		self.useUrlItem(0-1,"","","","",'Add')
					#except: pass
				elif   controlId==self.c['BtnTopMenu02']: ## Remove Url ##
					try:
#						self.StandCards()
						iCount=int(self.List01.getSelectedItem().getProperty('iCount')); 
						ItemDate=self.List01.getSelectedItem().getProperty('ItemDate'); 
						Img=self.List01.getSelectedItem().getProperty('Img'); 
						Name=self.List01.getSelectedItem().getLabel(); 
						Url=self.List01.getSelectedItem().getLabel2(); 
						self.useUrlItem(iCount,Name,Url,ItemDate,Img,'Remove')
						pass
					except: pass
				elif   controlId==self.c['BtnTopMenu03']: ## Clear All Urls ##
					try:
#						self.dealCard(1)
						self.FileArray=[]
						self.saveFileArray()
						self.reloadFileArray()
						pass
					except: pass
#				elif   controlId==self.c['BtnCard01']:
#						#self.BtnCard01
#						#self.ImgCard01
#						#note("Card","1")
#						self.dealCard(1)
#						pass
#				elif   controlId==self.c['BtnCard02']: 
#						#self.BtnCard02
#						#self.ImgCard02
#						#note("Card","2")
#						self.StandCards()
#						pass
				elif   controlId==self.c['List01']: 
					#try:
						iCount=int(self.List01.getSelectedItem().getProperty('iCount')); 
						ItemDate=self.List01.getSelectedItem().getProperty('ItemDate'); 
						Img=self.List01.getSelectedItem().getProperty('Img'); 
						Name=self.List01.getSelectedItem().getLabel(); 
						Url=self.List01.getSelectedItem().getLabel2(); 
						#self.useUrlItem(iCount,Name,Url,ItemDate,Img)
						self.useUrlItem(iCount)
						
						
						
						pass
					#except: pass
				else:
					try:
						
						pass
					except: pass
			#except Exception,e: debob(["Error",e])
			#except: pass
		def useUrlItem(self,iCount,Name='',Url='',ItemDate='',Img='',tAnswer='',url='',Desc='',iAction=''): 
			#try:
				if not iCount==(0-1): print self.FileArray[iCount]
				if len(Url) > 0: url=Url
				else: 
					if not iCount==(0-1):
						#debob(['iCount',iCount])
						try: 
							url=self.FileArray[iCount]['Url']
						except: url=''
				#debob(['url',url])
				if iCount==(0-1):
					return
					#pass
				else:
					try:
						if ItemDate=='': ItemDate=self.FileArray[iCount]['Date']
					except: ItemDate=''
					try:
						if Name=='': Name=self.FileArray[iCount]['Title']
					except: Name=''
					try:
						if Desc=='': Name=self.FileArray[iCount]['Desc']
					except: Desc=''
					try:
						if Img=='': Img=self.FileArray[iCount]['Thumb']
					except: Img=''
					try:
						if iAction=='': iAction=self.FileArray[iCount]['Action']
					except: iAction=''
				play=xbmc.Player(GetPlayerCore()); 
				debob({'iCount':iCount,'Answer':tAnswer,'Action':iAction,'A2':self.FileArray[iCount]['Action']})
				if (tAnswer=='') and (iAction==''):
					SelAry=[]; 
					if (iAction=='Playback') and (('://' in url) or (':\\' in url) or (url.startswith('/'))):
						SelAry.append("Direct Play")
						SelAry.append("UrlResolver Play")
						SelAry.append("UrlResolver Play +")
					else:
						SelAry.append("Do Job")
					SelAry.append("Add")
					SelAry.append("Edit")
					SelAry.append("Remove")
					SelAry.append("Cancel")
					rAnswer=askSelection(SelAry,"Options")
					tAnswer=SelAry[rAnswer]
				elif (len(tAnswer)==0) and (len(iAction) > 0):
					tAnswer=iAction
				else: 
					tAnswer='Cancel'
				if   tAnswer=='Cancel': return
				elif tAnswer=='Remove':
						a=self.FileArray[iCount]
						self.FileArray.remove(a)
						#for a in self.FileArray:
						#		if a['Url']==url:
						#				self.FileArray.remove(a)
						self.saveFileArray()
						self.reloadFileArray()
						return
				elif tAnswer=='Edit':
						a=self.FileArray[iCount]
						#for a in self.FileArray:
						#		if a['Url']==url:
						New_Url=showkeyboard(url,"URL")
						New_Title=showkeyboard(Name,"TITLE")
						New_Desc=showkeyboard(Desc,"Description")
						New_Action=showkeyboard(iAction,"Action")
						New_Thumb=showkeyboard(Img,"THUMB / IMAGE / GRAPHIC")
						if (len(New_Url)==0): return
						self.FileArray.remove(a)
						self.FileArray.append({'Title':New_Title,'Thumb':New_Thumb,'Date':'%s-%s-%s'%(str(datetime.date.today().year),str(datetime.date.today().month),str(datetime.date.today().day)),'Url':New_Url,'Desc':New_Desc,'Action':New_Action})
						#debob(self.FileArray)
						self.saveFileArray()
						self.reloadFileArray()
						return
				elif tAnswer=='Add':
						New_Url=showkeyboard("","Action")
						New_Title=showkeyboard("","TITLE")
						New_Desc=showkeyboard("","Description")
						New_Action=showkeyboard("","Action")
						New_Thumb=showkeyboard("","THUMB / IMAGE / GRAPHIC")
						if (len(New_Url)==0) and (len(New_Title)==0) and (len(New_Thumb)==0) and (len(New_Desc)==0): return
						if (len(New_Url)==0): return
						self.FileArray.append({'Title':New_Title,'Thumb':New_Thumb,'Date':'%s-%s-%s'%(str(datetime.date.today().year),str(datetime.date.today().month),str(datetime.date.today().day)),'Action':New_Url,'Desc':New_Desc,'Action':New_Action})
						#debob(self.FileArray)
						self.saveFileArray()
						self.reloadFileArray()
						return
				elif tAnswer=='Direct Play':
					#try:
						#debob({'url':url})
						try: play.play(url)
						except: pass
						return
					#except: return
				elif tAnswer=='UrlResolver Play':
					#try:
						import urlresolver
						stream_url=urlresolver.HostedMediaFile(url).resolve()
						#debob({'stream_url':stream_url})
						try: play.play(stream_url)
						except: pass
						return
					#except: return
				elif tAnswer=='UrlResolver Play +':
					#try:
						#importURLResolver()
						import urlresolver
						_plugin_path=xbmc.translatePath(os.path.join(addonPath,'resources','lib','plugins'))
						urlresolver.plugnplay.plugin_dirs=[]
						urlresolver.plugnplay.set_plugin_dirs(urlresolver.common.plugins_path,_plugin_path)
						urlresolver.plugnplay.load_plugins()
						##
						stream_url=urlresolver.HostedMediaFile(url).resolve()
						#debob({'stream_url':stream_url})
						try: play.play(stream_url)
						except: pass
						return
					#except: return
				#elif tAnswer=='':
				#elif tAnswer=='':
				#elif tAnswer=='':
				#else: #return
				elif len(iAction)==0: return
				elif iAction=='wipe':
						#try:
							
							
							pass
						#except: return
				elif iAction=='remove-addon':
						#try:
							
							
							pass
						#except: return
				elif (iAction=='place-package') and (len(url) > 0):
						#try:
							
							
							pass
						#except: return
				elif (iAction=='place-wizard') and (len(url) > 0):
						#try:
							
							
							pass
						#except: return
				elif iAction.startswith('import '):
						#try:
							FPrefix=ps('Import Prefix')
							FToImport=iAction.replace('import ','').strip()
							if isFile(tP(os.path.join(addonPath,FPrefix+FToImport+ps('Import Sufix'))))==True:
								__import__(FPrefix+FToImport)
							return
						#except: return
				#	pass
				#	##
				##
				else: return
				pass
			#except: pass
		def onAction(self,action): 
			try:
				actId=int(action.getId()); actIds=str(action.getId()); actBC=str(action.getButtonCode()); xx=0; yy=0; 
				try: actAmnt1=action.getAmount1()
				except: actAmnt1=0-900
				try: actAmnt2=action.getAmount2()
				except: actAmnt2=0-900
				mW=self.maxW; mH=self.maxH; mWa=int(self.getWidth()); mHa=int(self.getHeight()); 
				actAmnt1k=int(actAmnt1*mW/mWa); actAmnt2k=int(actAmnt2*mH/mHa); 
				##
				if   action==ACTION_PREVIOUS_MENU: self.AskToClose()
				elif action==ACTION_NAV_BACK: self.AskToClose()
				else:
					if not actId==0:
						#debob({'action type':'UNKNOWN','getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
						pass
						##
					##
				##
			except Exception,e: debob(["Error",e]); debob([actId,actIds,actBC])
			except: pass
		def CloseWindow(self):
			try:
				self.closing=True; 
			except: pass
			self.close()
		def CW(self): self.CloseWindow()
		def AskToClose(self):
			try:
				if self.closing==False:
					if d.yesno(addonName," ","Are you sure that you want to exit?","","No","Yes"): self.closing=True; self.CloseWindow()
				else: self.CloseWindow()
			except: pass
		##
######


#############################################################################
#############################################################################
skinFilename='CustomWindow001.xml'
try:    Emulating=xbmcgui.Emulating
except: Emulating=False
if __name__=='__main__':
	#cWind=CustomWindow(skinFilename,addon_path,'default')
	cWind=CustomWindow(skinFilename,addon_path) #,'default'
	cWind.doModal()
	del cWind
	sys.modules.clear()

#############################################################################
#############################################################################
