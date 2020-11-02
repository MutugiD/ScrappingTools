###image = [image['src'] for image in content.find_all('img', {'itemprop':'image'})]
# src = link/source, img= class |'itemprop':'image' =  defining piece (copied)

##s_address = [s_address['content'] for s_address in content.find_all('meta', {'itemprop':'streetAddress'})]
#content = source of address || itemprop="streetAddress"

import requests 
from bs4 import BeautifulSoup
import json
import csv


class RunScrapper: 
    
    results = []  
    
    def fetch(self, url):
        print('HTTP GET request to URL: %s' % url, end='')
        response = requests.get(url)
        print(' | Status code: %s' % response.status_code)
        return response 
    
    def url_main(self, hmtl): 
        pass 
    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        title = [title.text.strip() for title in content.find_all("h2", {'class': 'propertyCard-title'})]
        address = [address.text.strip() for address in content.find_all("address", {'class':'propertyCard-address'})]
        s_address = [s_address['content'] for s_address in content.find_all('meta', {'itemprop':'streetAddress'})]
        description = [description.text for description in content.find_all('span', {'data-test':'property-description'})]
        price = [price.text.strip() for price in content.find_all('div', {'class':'propertyCard-priceValue'})]
        date = [date.text.split()[-1] for date in content.find_all('span', {'class':'propertyCard-branchSummary-addedOrReduced'})]
        agent= [agent.text.split('by')[-1].strip() for agent in content.find_all('span', {'class':'propertyCard-branchSummary-branchName'})]
        image = [image['src'] for image in content.find_all('img', {'itemprop':'image'})]
        
        for index in range (0, len(title)): 
            self.results.append({
                'title':  title[index], 
                'address': address[index], 
                's_address': s_address[index], 
                'description': description[index], 
                'price': price[index], 
                'agent': agent[index],
                'image': image[index]
            })
            
            
                    
            
        
    
    def to_csv(self): 
        
        with open ('rightmove.csv', 'w') as csv_file: 
            writer = csv.DictWriter(csv_file, fieldnames =self.results[0].keys())
            writer.writeheader()
            
            for row in self.results:
                writer.writerow(row)
            print("Stored to 'rightmove.csv'")
            
    def run(self): 
        for page in range (0, 5):
            index = page * 24
            url = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E93917&index = '+ str(index) + ' &propertyTypes=&mustHave=&dontShow=&furnishTypes=&keywords='
            response = self.fetch(url)
       
                
            self.parse(response.text)
            
        self.to_csv()
                
            
            #html_file.read(response.content)
        
    
    
    
if __name__== '__main__':
    scrapper = RunScrapper()
    scrapper.run()
    
    
