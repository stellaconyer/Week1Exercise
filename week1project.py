import os
import shutil

#create container folder for alphabet folders
os.mkdir("alphabet_folder")

#create a separate folder for each letter of the alphabet
for i in range(97,123):
    letter = chr(i)
    os.mkdir("alphabet_folder/%s" % letter)

#create list of alphabet folders and list of user files
alphabet_list = os.listdir("alphabet_folder")
user_files = os.listdir("originalfiles")
    
#move each user file into a folder that corresponds to the first
#letter of the user file
for a_user_file in zip_files:
	first_letter = a_user_file[0]
	src = "originalfiles/%s" % a_user_file
	dest = "alphabet_folder/%s/%s" % (first_letter, a_user_file)
	shutil.move(src,dest)