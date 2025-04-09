import glob
import os.path

path = r"C:\Users\Raviteja\Documents\handson\Day2"            #Change path 
folder = glob.glob(path+r"\*")
data = r"C:\Users\Raviteja\Documents\handson\Day2\data.txt"   #Create a file named data.txt to enter text 



def allInOne(folder,data):
    for file in folder:
        if os.path.isfile(file):
            if file.endswith(".txt"):
                with open(file,"rt") as f:
                    lines = f.readlines()
                with open(data,"at") as ft:
                    ft.write("\n##############################################################\n")
                    
                    ft.write("Data From file"+file+"\n")
                    ft.writelines(lines)
                    ft.write("\n##############################################################\n")
                    
        else:
            sub = glob.glob(os.path.join(file, "*"))
            allInOne(sub, data)
            
allInOne(folder,data)    
print("Data Entered Sucessfully")        
                    
                   
    
                
