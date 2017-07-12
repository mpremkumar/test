from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException  

urls= [
'https://www.marketsmojo.com/Stocks?StockId=968623&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=732927&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=869476&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=741664&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=308603&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=964509&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=915363&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=302921&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=248522&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=347298&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=957749&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=452063&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=452187&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=959222&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=887786&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=909467&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=950641&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=141796&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=264317&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=919264&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=608125&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=363433&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=744293&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=878484&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=793847&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=166837&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=539868&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=422311&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=751831&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=687677&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=513245&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=639617&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=597145&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=463886&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=761462&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=383151&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=171892&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=213617&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=435326&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=179698&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=880342&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=313810&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=589145&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=107657&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=110452&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=129013&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=950027&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=347516&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=816180&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=372338&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=542329&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=955411&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=146836&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=707242&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=734514&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=209609&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=346859&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=573496&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=856648&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=621045&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=928540&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=757094&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=577677&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=585335&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=531797&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=971778&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=321642&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=854537&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=918007&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=634431&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=881291&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=820711&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=601113&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=809565&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=386301&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=592009&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=191974&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=650168&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=169739&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=729412&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=227845&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=591083&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=855995&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=713180&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=248543&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=983371&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=956244&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=941844&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=399834&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=969461&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=934380&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=329828&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=864806&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=891577&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=190647&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=482661&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=946643&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=705833&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=958236&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=941607&Exchange=0'
]
f= open("finance1.txt","a+")
browser=webdriver.Firefox()
browser.maximize_window()
for url in urls:
	browser.get(url)
	browser.execute_script("window.scrollTo(0,7600);")
	browser.implicitly_wait(10)
	browser.find_element_by_css_selector('#PrevDetails').click()
	data = []
	for tr in browser.find_elements_by_css_selector('#consolidated-1 > table'):
		ths = tr.find_elements_by_tag_name('th')
		tds = tr.find_elements_by_tag_name('td')
		if ths: 
			data.append([th.text for th in ths])
		if tds: 
			data.append([td.text for td in tds])
		f.write(str(data))
browser.quit()
#PrevDetails
#consolidated-1 > table



	
