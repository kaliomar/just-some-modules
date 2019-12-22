import os


def rename_files():
   os.chdir(r"/root/")
   # file = open("four.txt", "a")
   fileold = open("darkcode.txt", "r")
   count = 0
   for line in fileold:
      if len(line) >= 8:
         count += 1
   return count
   print "hi"


rename_files()
