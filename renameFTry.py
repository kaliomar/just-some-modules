import os

# not success yet:try to automating rename files from txt file
def auto_rename():
   names = open("test.txt", "r")
   start_list = []
   for index, line in enumerate(names):
      start_list.append(line)

   os.chdir("/root/testology")
   file_list = os.listdir("/root/testology")
   i = 0
   for file in file_list:
      os.rename(file,start_list[i])
      i+=1

# to delete line "free video" from the list.
def delet_freeVideo():

   file = open("new.txt", "a")
   fileold = open("test.txt", "r")
   for index, line in enumerate(fileold):
      if line != "Free Video!\n":
         file.write(line)

# to delete number of video which in seperated line.
def delete_num():

   file = open("new1.txt", "a")
   fileold = open("new.txt", "r")
   for index, line in enumerate(fileold):
      if len(line) > 3:
         file.write(line)

# to delete duplicate file names.
def delete_duplicate():

   file = open("new2.txt", "a")
   fileold = open("new1.txt", "r")
   for index, line in enumerate(fileold):
      if index % 2 == 1:
         file.write(line)

# to add number to the beginning of line

def add_starterNumber():
   topic = open("new2.txt", "r")
   new = open("new3.txt", "a")
   n = 1
   for line in topic:
      new.write(str(n) + "-" + line)
      n += 1
