# Median Market Price for Second-Hand Clothing

<i>Caitlin Sanderson<br>
  Final Project<br>
  Ironhack Berlin, Oct - Dec 2020</i><br><br>
  ## Project Description<br>
The second-hand clothing market is highly competative and sometimes rather fickle.  A dress that cost 300€ new, might sell for less in the second-hand market, than one that cost 30€, depending on current trends.  As the owner of a second-hand clothing online retail business, I want to make sure that I am offering the best deal possible to my customers.  Additionally, because I purchase our product directly from customers for immediate re-sale, I want to provide our selling-side customers with as fair price as possible, but one that will increase the probability that the piece will sell quickly.  Finally, I want to keep up with which brands are popular and can command a higher price in the second-hand market.  So I set out to see how I could gather information on what our competitors are selling and how much they are selling it for.<br><br>

  ## The Pipeline Process
  Setting up my data pipeline broke down into roughly four main steps:
<ol><li>Gathering the data by web scraping</li>
  <li>Cleaning and shaping the data using Python and Pandas in Jupyter Notebooks</li>
  <li>Using NLP pre-processing packages and techniques to help me match the language used from the data gathered to our own, internal language, and</li>
  <li>Creating easily accessible, useful information from that data to inform my business decisions.  This resulted in a median price generator that gives me the median price that a type category of clothing from a specified brand sold for in the past 14 days.</li></ol>While I still have a long way to go to make it usable in my day-to-day business operations, this repo shows that I was able to complete a first iteration of all of these steps. <br>
   
  ## Tools Used
  I used many tools in this project, but here are the main ones:<br>
  <ul><li>Scrapy</li><li>Selenium</li><li>Python</li><li>Pandas</li><li>NLTK</li><br>
  
  ## Resources and Shout-Outs
  Neither Scrapy nor Selenium were covered in the bootcamp.  I used the [Udemy course Modern Web Scraping with Python using Scrapy Splash Selenium](https://www.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/), created by Ahmed Rafik, to give me the basics.<br><br>
  While NLP was briefly covered, I relied a lot on the [very helpful video](https://www.youtube.com/watch?v=xvqsFTUsOmc&feature=youtu.be&ab_channel=PyOhio) and [github repo](https://github.com/adashofdata/nlp-in-python-tutorial) from Alice Zhao to help me through that part of the process. She also taught me about pickling, for which I am very happy! <br><br>
  
  ## The Repo
  In this repo is the following:
  <ol><li>My webscraping spider and resulting csv file</li>
  <li>The two jupyter notebooks I used to clean, shape, process, and analyze my data, and </li>
  <li>My folder of pickles</li>
  <li>My presentation slides</li>
