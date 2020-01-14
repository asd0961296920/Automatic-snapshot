# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:25:53 2020

@author: Typhoon
"""
# -*- coding: utf-8 -*-
from requests_html import HTMLSession
import re,os,pathlib,base64
from requests_html import AsyncHTMLSession
#如果 DOWNLOAD 資料夾不存在就新建
base_dir = os.path.dirname(os.path.realpath(__file__))+"\\"
img_dir=base_dir+"DOWNLOAD\\"
pathlib.Path(img_dir).mkdir(parents=True, exist_ok=True)

#清除 DOWNLOAD 資料夾裡的 jpg 及 png 檔
filelist = [ f for f in os.listdir(img_dir) if f.endswith(".jpg") or f.endswith(".gif") or f.endswith(".png")]
for f in filelist:
    os.remove(os.path.join(img_dir, f))
    
    
print('~~~使用說明~~~')
    
print('本程式請在一定要在cmd(命令提示字元)中執行')
print('本程式只要輸入需要查詢的關鍵字，就會自動下載該關鍵字所查詢到的２０張圖片到DOWNLOAD資料夾中')
print('若沒有DOWNLOAD資料夾，程式會在該程式所在位置自動建立一個')
print('每次查詢前會將DOWNLOAD資料夾清空，如要運行第二次程式前請先將DOWNLOAD資料夾中需要的圖片備分')   
        
print('~~~使用說明~~~')
        
    

word = input('請輸入搜尋關鍵字: ')
print('正在爬取圖片中...')
url = 'https://www.google.com.tw/search?q='+word+' &rlz=1C1CAFB_enTW617TW621&source=lnms&tbm=isch&sa=X&ved=0ahUKEwienc6V1oLcAhVN-WEKHdD_B3EQ_AUICigB&biw=1128&bih=863'


session = HTMLSession()
r = session.get(url)
r.html.render(sleep=3,scrolldown=1,wait=2)
img_arr=r.html.find("img")
img_no=0
for i in img_arr:
  tmp_content=''
  try:
    tmp_content=(i.attrs['src'])
  except:
    pass
  finally:
    if tmp_content!='' and tmp_content.find('http')==-1 and tmp_content.find('/images')==-1:
      if img_no>0:
        if tmp_content.find("jpeg")>-1:
          img_type='.jpg'
        elif tmp_content.find("gif")>-1:
          img_type='.gif'
        else:
          img_type='.png'
        img_url=img_dir+'img'+str(img_no)+img_type
        print(img_url)
        with open(img_url,'wb') as file:
          base64_data = re.sub('^data:image/.+;base64,', '', tmp_content)
          byte_data = base64.b64decode(base64_data)
          file.write(byte_data)
          file.flush()
        file.close() 
      img_no=img_no+1
print('圖片爬取完成')    