def initFile():
    #Create File Headers
    outputFile = open('carsFromJapan.csv', 'a', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow((['Unique URL', 'Model', 'Model Year', 'Miles Driven', 'Price']))
    outputFile.close()

    #Page 1
    for carURL in url_list:
        combinedUrl = url_base + carURL
        scrapeCarData(combinedUrl)

    #Page 2
    for carURL in url_list_page_2:
        combinedUrl = url_base + carURL
        scrapeCarData2(combinedUrl)

    return None






    # writeCarPageUrl = rowData[1].find('a', {'class' : 'strong-color'}).attrs['href']
        # writeModel = rowData[1].find('h2').text
        # writeModelYear = rowData[2].find('span').text
        # writeDriven = rowData[3].find('span').text
        # writePrice = rowData[6].find('span').text
        
        #Remove commas + Convert to float + caluclate km to miles + cast to string
        writeDriven = writeDriven.replace(',','')
        writeDriven = float(writeDriven)
        writeDriven = writeDriven * 0.62137
        writeDriven = round(writeDriven, 2)
        writeDriven = str(writeDriven)
        writePrice = writePrice.replace(',','')
        writePrice = writePrice.replace('US$ ','')
        
        #place elems into list
        scrapedData.extend((writeCarPageUrl,writeModel,writeModelYear,writeDriven, writePrice))
        writeCSV(scrapedData)