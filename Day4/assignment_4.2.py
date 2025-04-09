from pkg.file import File
import datetime


path = "."
file_obj = File(path)
max_num = 2
maxSize_obj = file_obj.getMaxSizeFile(max_num)
latestFile_obj = file_obj.getLatestFiles(datetime.date(2018,2,1))

print(maxSize_obj)
print(latestFile_obj)
