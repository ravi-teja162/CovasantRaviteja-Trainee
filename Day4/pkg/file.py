import os.path, glob, os
import datetime

class File:
    def __init__(self,path):
        self.path = path
        self.folder = glob.glob(path+r"\*")
        self.sorted_folder = []
        
    
    def getMaxSizeFile(self, max_files):
        self.sorted_folder = sorted(self.folder, key = lambda x: os.path.getsize(x))
        return self.sorted_folder[:max_files]
        
    def getLatestFiles(datetime.date(2018,2,1)):
        pass
        
        
        
    def __str__(self):
        return f"{self.sorted_folder}
        

    
   
