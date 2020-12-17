# import all of my programs and packages.  
# Selenium will be doing the scraping and Scrapy will be doing the parsing
import scrapy
from scrapy.selector import Selector
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
from random import randint

#Scrapy automatically creates the scraping and parsing architechture for you, including the
    #spider class.

class Sold_ItemsSpider(scrapy.Spider):
    name = 'sold_items'
    allowed_domains = ['www.grailed.com'] 
    start_urls = ['https://www.grailed.com/sold/9Hr4phZJJA']

#the init function is to run Selenium
    def __init__(self):
        #the options allow me to run the spider in a way that is less likely to be detected.  
        #with Grailed, it is not possible to load the page without opening the brower, so headless
        #scraping is not possible, which means the scraping will take longer.  Headless scraping,
        #however, is also more easily detected and blocked.  Due to Grailed's sophisticated website
        #with bot-detection, I need to mimic as closely as possible human web browsing behavior. 
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_path = which("chromedriver")
        #the driver is how Selenium 'drives' Chrome
        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        #I set the window size a bit larger with the hopes of being able to capture more items per scroll
        driver.set_window_size(1920, 1080)
        #The driver.get() is the Selenium function for calling the website.  I am able to call 
        #directly the 'sold' items listing, filtered by those sold in Europe.  My attempts to log-in
        #and navigate to this page in other ways was always detected and blocked. 
        driver.get("https://www.grailed.com/sold/9Hr4phZJJA")

        #I define my wait times to be random and set up my scrolling variables to be able to deal
        #with Grailed's infinite scroll page. 
        wait_time = randint(0,3)
        scroll_pause_time = wait_time
        screen_height = driver.execute_script("return window.screen.height;")
        i=1
        #I use the while loop to look for the height of the page that is loaded with each new call
        #and then scroll further. 
        while True:
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 1
            #I give it some time between each scroll to pause, so as not to overtax the server. 
            time.sleep(scroll_pause_time)
            #If I could scroll all the way down, I would use the following two lines of code.
            #However, due to the number of items involved, limitations on my brower's memory, and 
            #Grailed's site, I am unable to load all ~300,000 items that are listed at any given time
            #on the sold page.  
                #scroll_height = driver.execute_script("return document.body.scrollHeight;")
                #if (screen_height) * i > scroll_height:
            #Therefore, I define the number of times I want to scroll, with the following condition.  
            if i > 10:
                break
        
        #after loading the page as much as possible, I use the driver.page_source from Selenium to 
        #scrape the html from the page that I loaded. 
        self.html = driver.page_source

        time.sleep(wait_time)

        #I then close the driver. 
        driver.close()

    #The parse function is where Scrapy takes over.  First, I have to turn the html scraped by 
    #Selenium into text that Scrapy can read.  This is done using the Selector function. 
    def parse(self, response):
        response_obj = Selector(text=self.html)
        
        #once the html is able to be read by Scroping, I use a for loop to parse the text into
        #the different variables that I want to get using XPath.   
        for item in response_obj.xpath("//div[@class='feed-item']"):
            yield {
                'brand': item.xpath(".//p[@class='listing-designer']/text()").get(),
                'title': item.xpath(".//p[@class='listing-title']/text()").get(),
                'sold_price': item.xpath(".//p[@class='sub-title sold-price']/span/text()").get(),
                'when_sold': item.xpath(".//span[@class = 'date-ago']/text()").get(),
                #I use the response.urljoin on the item links in order to return absolute URLs rather
                #than the relative URLs that are otherwise returned.  
                'item_links': response.urljoin(item.xpath(".//a[@class = 'listing-item-link']/@href ").get())
            }

#In the command line, I run the spider and have it send the results directly into a CSV file.  
