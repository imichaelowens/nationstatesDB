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
    'page=list_nations/censusid=47']

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
                

                #/////print(len(infoScrapeBubbles))
                #////print(nationCompleteURL)
                for bubble in infoScrapeBubbles:
                    bubbleValue = bubble.text
                    scrapedNationProperties.append(bubbleValue)
                
                #Remove nation influence and administration strings
                try:
                    scrapedNationProperties.pop(0)
                    scrapedNationProperties.pop(0)
                except:
                    pass

                #/////print(scrapedNationProperties)
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
    #////print(writeRowData)
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
        #x = 0
        x = 500

        combinedUrl = url_base + nationURL
        scrapeNationData(combinedUrl)

    return None


initFile()

