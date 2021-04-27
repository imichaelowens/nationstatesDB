#import libraries
from bs4 import BeautifulSoup
import requests
import time
import csv


url_base = "https://www.nationstates.net/"
nationUID= "https://www.nationstates.net/"

#url_list in order (Each # is a seperate url):
#Civil Rights #Economy
#Political Freedom #Population
#Authoritarianism #Average Disposable Income
#Average Income #Average Income of Poor
#Average Income of Rich #Averageness
#Black Market #Business Subsidization
#Charmlessness #Cheerfulness
#Compassion #Compliance
#Corruption #Crime
#Culture #Death Rate
#Defense Forces #Eco-Friendliness
#Economic Freedom #Economic Output
#Employment #Environmental Beauty
#Foreign Aid #Freedom From Taxation
#Government Size #Health
#Human Development Index #Ideological Radicality
#Ignorance #Inclusiveness
#Income Equality #Industry: Arms Manufacturing
#Industry: Automobile Manufacturing #Industry: Basket Weaving
#Industry: Beverage Sales #Industry: Book Publishing
#Industry: Cheese Exports #Industry: Furniture Restoration
#Industry: Gambling #Industry: Information Technology
#Industry: Insurance #Industry: Mining
#Industry: Pizza Delivery #Industry: Retail
#Industry: Timber Woodchipping #Industry: Trout Fishing
#Influence #Integrity
#Intelligence #International Artwork
#Law Enforcement #Lifespan
#Niceness #Nudity
#Obesity #Pacifism
#Political Apathy #Primitiveness
#Public Education #Public Healthcare
#Public Transport #Recreational Drug Use
#Religiousness #Residency
#Rudeness #Safety
#Scientific Advancement #Sector: Agriculture
#Sector: Manufacturing #Secularism
#Social Conservatism #Taxation
#Tourism #Wealth Gaps
#Weaponization #Weather
#Welfare #World Assembly Endorsements
#Youth Rebelliousness

url_list = [
    'page=list_nations/censusid=0', 'page=list_nations?censusid=1',
    'page=list_nations?censusid=2', 'page=list_nations?censusid=3',
    'page=list_nations?censusid=53', 'page=list_nations?censusid=85',
    'page=list_nations?censusid=72', 'page=list_nations?censusid=73',
    'page=list_nations?censusid=74', 'page=list_nations?censusid=67',
    'page=list_nations?censusid=79', 'page=list_nations?censusid=31',
    'page=list_nations?censusid=64', 'page=list_nations?censusid=40',
    'page=list_nations?censusid=6', 'page=list_nations?censusid=42',
    'page=list_nations?censusid=51', 'page=list_nations?censusid=77',
    'page=list_nations?censusid=55', 'page=list_nations?censusid=5',
    'page=list_nations?censusid=46', 'page=list_nations?censusid=7',
    'page=list_nations?censusid=48', 'page=list_nations?censusid=76',
    'page=list_nations?censusid=56', 'page=list_nations?censusid=63',
    'page=list_nations?censusid=78', 'page=list_nations?censusid=50',
    'page=list_nations?censusid=27', 'page=list_nations?censusid=39',
    'page=list_nations?censusid=68', 'page=list_nations?censusid=45',
    'page=list_nations?censusid=37', 'page=list_nations?censusid=71',
    'page=list_nations?censusid=33', 'page=list_nations?censusid=16',
    'page=list_nations?censusid=10', 'page=list_nations?censusid=12',
    'page=list_nations?censusid=18', 'page=list_nations?censusid=24',
    'page=list_nations?censusid=11', 'page=list_nations?censusid=22',
    'page=list_nations?censusid=25', 'page=list_nations?censusid=13',
    'page=list_nations?censusid=21', 'page=list_nations?censusid=20',
    'page=list_nations?censusid=14', 'page=list_nations?censusid=23',
    'page=list_nations?censusid=19', 'page=list_nations?censusid=15',
    'page=list_nations?censusid=65', 'page=list_nations?censusid=52',
    'page=list_nations?censusid=36', 'page=list_nations?censusid=86',
    'page=list_nations?censusid=30', 'page=list_nations?censusid=44',
    'page=list_nations?censusid=34', 'page=list_nations?censusid=9',
    'page=list_nations?censusid=61', 'page=list_nations?censusid=47',
    'page=list_nations?censusid=38', 'page=list_nations?censusid=69',
    'page=list_nations?censusid=75', 'page=list_nations?censusid=29',
    'page=list_nations?censusid=57', 'page=list_nations?censusid=60',
    'page=list_nations?censusid=32', 'page=list_nations?censusid=80',
    'page=list_nations?censusid=35', 'page=list_nations?censusid=43',
    'page=list_nations?censusid=70', 'page=list_nations?censusid=17',
    'page=list_nations?censusid=26', 'page=list_nations?censusid=62',
    'page=list_nations?censusid=8', 'page=list_nations?censusid=49',
    'page=list_nations?censusid=58', 'page=list_nations?censusid=4',
    'page=list_nations?censusid=59', 'page=list_nations?censusid=41',
    'page=list_nations?censusid=28', 'page=list_nations?censusid=66',
    'page=list_nations?censusid=54']

#Scrape nation data from the 
def scrapeNationData(combinedUrl):
    global x
    while x < 10000:
        nextUrl = None
        nextUrl = combinedUrl + '?start=' + str(x)

        print(nextUrl)

        #set soup parameters
        page = requests.get(nextUrl)
        soup =  BeautifulSoup(page.content, 'html.parser')

        #get nation rows from page
        nationRows = soup.findAll('tr')

        #Remove table header from list
        print(len(nationRows))
        nationRows.pop(0)
        print(len(nationRows))

        #////print(nationRows)
        for nation in nationRows:
            if x < 10000:

                #empty lists for scraped data
                scrapedData = []
                scrapedNationProperties = []

                #////print(nation)

                #get children 'td' and iterate over them
                nationCell = nation.findAll('td')

                #Assign scraped data
                rowNationURL = nationCell[1].find('a').get('href')

                # ----- Get Nation Properties ------
                nationCompleteURL = url_base + rowNationURL
                pageProperties = requests.get(nationCompleteURL)
                soupProperties = BeautifulSoup(pageProperties.content, 'html.parser')
                infoScrapeBubbles = soupProperties.findAll('div', {'class' : 'newmainlinebubblebottom'})
                

                
                for bubble in infoScrapeBubbles:
                    bubbleValue = bubble.text
                    scrapedNationProperties.append(bubbleValue)
                
                #Remove nation influence and administration strings
                try:
                    scrapedNationProperties.pop(0)
                    scrapedNationProperties.pop(0)
                except:
                    pass

                
                try:
                    #Assign values then send to write function
                    rowNationName = nationCell[1].text
                    rowWACategory = nationCell[2].text
                    rowNationCivilRights = scrapedNationProperties[0]
                    rowNationEconomy = scrapedNationProperties[1]
                    rowNationPoliticalFreedoms = scrapedNationProperties[2]

                    scrapedData.extend((rowNationURL,rowNationName,rowWACategory, rowNationCivilRights, rowNationEconomy, rowNationPoliticalFreedoms))
                    writeCSV(scrapedData)
                except:
                    pass
            else:
                return None
        x = x + 10
    return



def writeCSV(writeRowData):
    outputFile = open('testNationData.csv', 'a', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(writeRowData)
    outputFile.close()
    return None


def initFile():
    #Create File Headers
    outputFile = open('testNationData.csv', 'a', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow((['Unique URL', 'Nation Name', 'WA Category', 'Civil Rights', 'Economy', 'Political Freedom']))
    outputFile.close()

    #Begin Scraping Function
    for nationURL in url_list:
        global x
        x = 0

        combinedUrl = url_base + nationURL
        scrapeNationData(combinedUrl)

    return None


initFile()

