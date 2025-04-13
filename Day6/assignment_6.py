import asyncio
import requests
import os
import time
import aiohttp
from bs4 import BeautifulSoup


class download_all_links:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    
    async def html_parse(self, url):
        try:
            async with aiohttp.ClientSession() as sess:
                async with sess.get(url) as resp:
                    self.html_text = await resp.text()
                    self.html_code = resp.status

            if self.html_code == 200:
                self.bs4_obj = BeautifulSoup(self.html_text, "html.parser")
                return self.bs4_obj
            else:
                print("Error: ", self.html_code)
                return None
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            
    async def get_all_links(self, obj):
        self.all_links =  [ a.attrs['href']  for a in obj.select("a") if a.attrs.get('href', '').startswith("https")] 
        return self.all_links 


    async def download(self, link):
        print("Started extracting from", link)
        obj = await self.html_parse(link)

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


    async def download_content(self):
        main_page = await self.html_parse(self.url)
        if main_page == None:
            return False
        
        links = await self.get_all_links(main_page) 
        
        tasks = [asyncio.create_task(self.download(link)) for link in  self.all_links]
        for task in asyncio.as_completed(tasks):
            res = await task
        



if __name__ == '__main__':
    url = r"https://www.w3schools.com/python/"   #you can change the link if you want to 
    path = r"C:\Users\Raviteja\Documents\handson\Day5\html_files_assignment5"  #give Complete paths by copying from the directory in the file explorer 
    
    os.makedirs(path, exist_ok=True) 
      
    d = download_all_links(url,path)
    s = time.time()
    p = asyncio.run(d.download_content())
    if not p:
        print("Invalid Link or cannot parse this HTML")
  
   
    print("Time taken is, ",time.time() - s) #this gives the execution time it depends on the number of links presnet in the website 

