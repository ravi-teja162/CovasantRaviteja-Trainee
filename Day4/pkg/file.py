import os.path, glob, os
import datetime

class File:
    def __init__(self,path):
        self.path = path
        self.folder = glob.glob(path+r"\*") 
        self.sorted_folder = []
        self.files_time = []
        
    
    def getMaxSizeFile(self, max_files):
        self.sorted_folder = sorted(self.folder, key = lambda x: os.path.getsize(x), reverse = True)
        return self.sorted_folder[:max_files]
        
    def getLatestFiles(self, date):
        for i in self.folder:
            self.mtime = datetime.datetime.fromtimestamp(os.path.getmtime(i))
            if date < self.mtime.date():
                self.files_time.append(i)
        return self.files_time
                
                
                
        
        
        
        
        
    def __str__(self):
        return f"{self.sorted_folder}"
        

    
   
