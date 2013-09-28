import os

os.mkdir("alphabet_folder")

for i in range(97,99):
    letter = chr(i)
    os.mkdir("alphabet_folder/%s" % letter)

alphabet_list = os.listdir("alphabet_folder")
zip_files = os.listdir("files")
print alphabet_list.sort()
print zip_files
    
