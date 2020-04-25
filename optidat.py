#!/usr/bin/env python3
from datetime import datetime 
import os
import csv

start_time = datetime.now() 

print('\n\nBe patient! \n\nDepneding on the size of your data file this program can take \nseveral minutes to run.\n\nFor inquiries, suggestions or comments email mikerthomas58@gmail.com Thanks!\n\n')
# Ask user for input file name.
my_file = input("Please type an input file name. This should be the name of \nyour 'dis-sbcsu;,optidat;' customer file. \nExample 'filename.txt': ")


# Ask user for delimted file name.
delimited_file = input("Please type delimited file name: ")
with open(my_file) as f:

# Word and strings to search on
    searchstrings = ('INDIVIDUAL DEVICE DATA ----------------OPTISET', 'INDIVIDUAL DEVICE DATA ----------------OPTIP500', 
                     'INDIVIDUAL DEVICE DATA ----------------OPTIIP', 'OPTISET E ** NOT PLUGGED YET **', 'OPTIPOINT500 ** NOT PLUGGED YET **', 
                     'OPTIIP-PHONE ** NOT PLUGGED YET **', 'OPTIPOINT500 ENTRY', 'OPENSTAGE 15', 'OPENSTAGE 80', 'OPTIPOINT500 BASIC', 
                     '(SOFTCLIENT)-OPTIIP', 'OPTIPOINT500 STANDARD', 'OPTIPOINT500 ADVANCE', 'OPTISET E ADVANCE', 'OPTISET E STANDARD','OPENSTAGE 40', 'OPENSTAGE 60', 
                     'AP1120 ANALOG ADAPTER', 'DPIP', 'OPTIPOINT420 STANDARD', 'OPTIPOINT420 ADVANCE', 'OPTIPOINT600 OFFICE', 'OPTIPOINTWL2 STANDARD', 
                     'OPENSTAGE 20 T', 'UFIP','V1.', 'V2.', 'V3', 'V4.', 'V5.', 'IPADDR', 'SUBIPADDR',)

# import all data in searchstring into file 
    for line in f.readlines():
        for word in searchstrings:
            if word in line:
                text_file = open('temp.txt', "a") 
                text_file.write(line)
                text_file.close()
                print (line)  # prints each line to the screen
                print('Please wait!!\nThis could take sevral minutes\ndepending on the size of the file\nand speed of your computer!!')

# appends each line to the file.
data =[]
with open('temp.txt','r+') as file:
    x = file.readlines()

    for i in range(0,len(x),2):
        data.append(x[i:i+2])
new =[' '.join(i) for  i in data]
for i in range(len(new)):
    new[i]=new[i].replace('\n','')

    with open('temp.txt','w') as file:
        for i in new:
            file.write(i+'\b')

# Clean up data, removes or changes charachers like -,| or : to commas, renames feilds to remove hypens.
with open('temp.txt', 'r+') as infile: # all data on 1 line
    with open(delimited_file, 'w') as outfile:  # comma delimited file
        data = infile.read()
        data = data.replace("OPTIIP-PHONE", "OPTIIPPHONE")
        data = data.replace("(SOFTCLIENT)-OPTIIP", "SOFTCLIENT_OPTIIP")
        data = data.replace("+------ ", "\n") # removes plus symbol and creates a new line for each searchstring phone.
        data = data.replace(" ----------------", ",")
        data = data.replace("--------------+ ","")
        data = data.replace("-------------+", "")
        data = data.replace("------------+", "")
        data = data.replace("-----------+", "")
        data = data.replace("---", ",")
        data = data.replace("-", ",")
        data = data.replace("|", ",")
        data = data.replace(":", ",")
        data = data.replace("+", "")
        data = data.replace(',,,,,,,,,', ',')
        data = data.replace(',,,,,,,,', ',')
        data = data.replace(',,,,,,,', ',')
        data = data.replace(',,,,,,', ',')
        data = data.replace(',,,,,', ',')
        data = data.replace(',,,,', ',')
        data = data.replace(',,,', ',')
        data = data.replace(',,', ',')
        data = data.replace('ANALOG,ADAPTER', 'ANALOG_ADAPTER')
        data = data.replace('', '')
        data = data.replace('OPTISET,E,**,NOT,PLUGGED,YET,**,', 'OPTISET_E,**NOT_PLUGGED_YET**,')
        data = data.replace('OPTISET,E,STANDARD', 'OPTISET_E,STANDARD')
        data = data.replace(',,', ',')
        data = data.replace(',OPTIIPPHONE,**,NOT,PLUGGED,YET,**,', ',OPTIIPPHONE,**NOT_PLUGGED_YET**,')
        data = data.replace(',OPTIPOINT500,**,NOT,PLUGGED,YET,**,', ',OPTIPOINT500,**NOT_PLUGGED_YET**,')
        data = data.replace(',OPENSTAGE,40,T,', ',OPENSTAGE,40_TDM,')
        data = data.replace('DPIP,55,', 'DPIP_55,')
        data = data.replace('OPENSTAGE,15,T,', 'OPENSTAGE,15_TDM,')
        data = data.replace(',C01,DPIP_55', ',C01,,,,DPIP_55')
        data = data.replace('OPENSTAGE,40,0', 'OPENSTAGE,40_IP,0')
        data = data.replace("INDIVIDUAL,DEVICE,DATA,", "INDIVIDUAL_DEVICE_DATA,")
        data = data.replace("IPADDR", "")
        data = data.replace("EMERG NO ", "")
        data = data.strip()
        outfile.write(data)
        
# Puts header row in CSV file.
with open(delimited_file ,newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open(delimited_file,'w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['INDIVIDUAL DEVICE DATA', 'FAMILY', 'EXTEN', 'PHONE FAMILY', 'EXT', 'ASSET-ID KEYBD TYPE', 'SW VERS BOOT-SW', 'TEST HWVERS',
                 'SW VERSION TDM & HFA', 'SW VERSION TDM & HFA', 'IPADDR', 'REMOVE', 'REMOVE', 'REMOVE', 'DSS VERSION', 'IPADDR', 'REMOVE', 'SW VERS BOOT-SW', 
                 'SW VERS BOOT-SW', 'TEST HWERS', 'IPADDR', 'IPADDR', 'REMOVE', 'SW VERS BOOT-SW', 'SW VERS BOOT-SW', 'TEST HWERS', 'DPIP CONTROL ADAPTER', 'IPADDR', 'REMOVE', 'SW VERS BOOT-SW', 'TEST HWERS', 
                 'DPIP CONTROL ADAPTER', 'IPADDR', 'IPADDR', 'SW VERS BOOT-SW', 'TEST HWERS', 'REMOVE', 'REMOVE', 'IPADDR'])
    w.writerows(data)

os.remove("temp.txt")
print("\n\ntemp.txt file was succdesfully removed!")

time_elapsed = datetime.now() - start_time 

print('\n\nProgram run time (hh:mm:ss.ms) {}'.format(time_elapsed))

final_comment = ('\n\nIf you find a bug or have a comment about this program \nplease email mikerthomas58@gmail.com \n\nhit enter key to close this window')
input(final_comment)
