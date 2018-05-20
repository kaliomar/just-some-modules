import os
os.chdir("/root/Downloads/Udemy Hacking Wireless Networks Theory And Practice Tutorial")

def renameFiles():
   folderList = os.listdir("/root/Downloads/Udemy Hacking Wireless Networks Theory And Practice Tutorial")
   for folder in folderList:
      os.chdir("/root/Downloads/Udemy Hacking Wireless Networks Theory And Practice Tutorial/{}".format(folder))
      innerPath = os.getcwd()
      fileList=os.listdir("/root/Downloads/Udemy Hacking Wireless Networks Theory And Practice Tutorial/{}".format(folder))

      for file in fileList:
         os.rename(file, file.replace("_"," "))

renameFiles()
print "hi"
