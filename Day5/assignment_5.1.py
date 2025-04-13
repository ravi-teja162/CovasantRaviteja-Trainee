import requests
import os
import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

class download_all_links:
    def __init__(self, url, path):
        self.url = url
        self.path = path

        self.original_url_obj = self.html_parse(self.url)
        self.all_links = self.get_all_links(self.original_url_obj)

    def html_parse(self, url):
        try:
            self.html_text = requests.get(url)
            if self.html_text.status_code == 200:
                self.bs4_obj = BeautifulSoup(self.html_text.text, "html.parser")
                return self.bs4_obj
            else:
                print("Error: ", self.html_text.status_code)
                return None
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def get_all_links(self, obj):
        return [a.attrs['href'] for a in obj.select("a") if a.attrs.get('href', '').startswith("https")] 

    def download(self, link):
        print("Started extracting from", link)
        obj = self.html_parse(link)

        if obj:
            print("Text extracted from", link)
            try:
                filename = link.replace("https://", "").replace("/", "_")[:50] + ".html"
                filepath = os.path.join(self.path, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(obj.prettify())

                print(f"Saved {link} to {filename}")
            except Exception as e:
                print(f"Failed to write {link}: {e}")


        

    def download_content(self):
        with ThreadPoolExecutor(max_workers=5) as executor: #5 or 10 workers giving good result
            for link in self.all_links:
                executor.submit(self.download, link)
            
                  

if __name__ == '__main__':
    url = r"https://www.w3schools.com/python/"   #you can change the link if you want to 
    path = r"C:\Users\Raviteja\Documents\handson\Day5\html_files_assignment5"  #give Complete paths by copying from the directory in the file explorer 
    
    os.makedirs(path, exist_ok=True) 
      
    d = download_all_links(url, path)

    links = d.all_links
    print(len(links), "links found")
    s = time.time()
    d.download_content()
    print("Time taken is, ",time.time() - s) #Execution time 

