import glob
import os.path
path = r"C:\Users\Raviteja\Documents\handson\Day2"

folder = glob.glob(path+r"\*")



def largeSize(folder, large):
    for file in folder:
        if os.path.isfile(file):
                size = os.path.getsize(file)
                if size > large:
                    large = size
                    
        elif os.path.isdir(file):
            
            sub = glob.glob(os.path.join(file, "*"))
            large = largeSize(sub, large)
            
            
                
    return large
           
            
print("The largest file size", largeSize(folder, 0))