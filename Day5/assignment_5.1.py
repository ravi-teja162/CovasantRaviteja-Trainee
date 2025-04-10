# download all the links in side the url
import requests
import os
import threading
from bs4 import BeautifulSoup

class download_all_links:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        
        
        self.original_url_obj = self.html_parse(self.url)
        self.all_links  = self.get_all_links(self.original_url_obj)
        
        
    def html_parse(self, url):
        self.html_text = requests.get(url)
        if self.html_text.status_code == 200:
            
            self.bs4_obj  = BeautifulSoup(self.html_text.text,"html.parser")
            return self.bs4_obj
        else:
            print("Error: ", self.html_text.status_code)
            return None
            
        
    def get_all_links(self, obj):
        all_links = [a.attrs['href'] for a in obj.select("a") if a.attrs['href'].startswith("https")] 
        return all_links
        
    def download(self,link):
        print("Started extracting from", link)
        obj = self.html_parse(link)
        
        #write each obj to file here
        if obj:
            try:
                filename = link.replace("https://", "").replace("/", "_")[:20] + ".html"
                filepath = os.path.join(self.path, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(obj.prettify())
                print(f" Saved {link} to {filename}")
            except Exception as e:
                print(f"Failed to write {link}: {e}")
        
        
        print("text Extracted from", link)
        
            
    def download_content(self):
        thrds = []
        
        for th in self.all_links:
            th = threading.Thread(target=self.download, args =( th,))
            thrds.append(th)
            
        [th.start() for th in thrds]
        [th.join() for th in thrds]
            
        
        
        
   

if __name__ == '__main__':
    url = r"https://www.w3schools.com/python/"  #give your link
    path = r"C:\Users\Raviteja\Documents\handson\Day5\html_files_assignment5"  #give Your own folder name
    d = download_all_links(url, path)
    links = d.all_links
    print(len(links)," links found")
    d.download_content()





