import os

def rename_filename():
    file_path = os.path.dirname("C:\Spring 2016\Nanodegree Program\prank\prank")
    print (file_path)
    os.chdir("C:\Spring 2016\Nanodegree Program\prank\prank")
    list = os.listdir("C:\Spring 2016\Nanodegree Program\prank\prank")
    print (list)
    for file_name in list:
        os.rename(file_name,file_name.translate(None, "0123456789"))
        
        
rename_filename()