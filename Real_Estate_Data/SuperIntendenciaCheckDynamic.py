import requests 
from bs4 import BeautifulSoup



class RunScrapper: 
    
    def fetch(self, url):
        print('HTTP GET request to URL: %s' % url, end='')
        response = requests.get(url)
        print(' | Status code: %s' % response.status_code)
        return response 
        
    def url_main(self, hmtl): 
        pass 
    def info_main(self): 
        pass 
    def csv(self, excel):
        pass
    def run(self): 
##write as JS
        response = self.fetch('https://www.rightmove.co.uk/property-for-sale/London.html')
        with open('res.html', 'wb') as html_file: 
            html_file.write(response.content)
        
    
    
    
if __name__== '__main__':
    scrapper = RunScrapper()
    scrapper.run()
    
    
