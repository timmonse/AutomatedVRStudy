# File:          AutomatedGUI.py
# Author:        Evan Timmons
# Date:          10/15/2019
# ISU Email:     timmonse@iastate.edu
# Description:   This program automates the study process for the 2019 ARLAB user study


from subprocess import call
import random
import psutil  
import PySimpleGUI as sg      
import csv
import time
import sys
import datetime
import os

sg.ChangeLookAndFeel('SystemDefault')      

# ------ Menu Definition ------ #      
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
			['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
			['Help', 'About...'], ]      

# ------ Column Definition ------ #      
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
		   [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
		   [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
		   [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

layout = [      
	[sg.Menu(menu_def, tearoff=True)],      
	[sg.Text('VR User Study', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],    
	[sg.Text('Study Administrator')],      
	[sg.InputText('Example: Evan Timmons')],
	[sg.Text('UserID')],      
	[sg.InputText('Example: U0001')],

	[sg.Text('_'  * 80)], 
	
	#Change the default paths
    
	#Select the read distance study location
	[sg.Text('File Selection', size=(20, 1), justification='center', font=("Helvetica", 15), relief=sg.RELIEF_RIDGE)],   
	
	[sg.Text('Read Distance Study', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\Users\\timmonse\\Desktop\\ReadDistanceStudy\\VR Read Distance Study.exe"), sg.FileBrowse()],
	 
	#FIX ME ADD NAME OF FOLDER and change the paths
	[sg.Text('Supriya Study 1', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\Users\\timmonse\\Desktop\\ReadDistanceStudy\\VR Read Distance Study.exe"), sg.FileBrowse()],
	 
	[sg.Text('Supriya Study 2', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\Users\\timmonse\\Desktop\\ReadDistanceStudy\\VR Read Distance Study.exe"), sg.FileBrowse()],
	 
	[sg.Text('Supriya Study 3', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\Users\\timmonse\\Desktop\\ReadDistanceStudy\\VR Read Distance Study.exe"), sg.FileBrowse()],
	 
	 [sg.Text('_'  * 80)], 
	 
    [sg.Text('Output Folder', size=(35, 1))],      
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\Users\\timmonse\\Desktop\\testOutput\\"), sg.FolderBrowse()],
	 
	
	[sg.Text('_'  * 80)], 
	 
	[sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
]      


window = sg.Window('VR User Study', layout, default_element_size=(40, 1), grab_anywhere=False)      

event, values = window.Read() 

#Assign names to GUI inputs
if event != 'Submit':
    sys.exit()
elif ((event == 'Submit') and ((values[2] == "Example: U0001") or (values[1] == "Example: Evan Timmons"))):
    while((values[2] == "Example: U0001") or (values[1] == "Example: Evan Timmons")):
        sg.Popup('Make sure to change the first two input fields')
        event, values = window.Read()

# !!!!!     END OF GUI     !!!!! !!!!!     END OF GUI     !!!!! !!!!!     END OF GUI     !!!!! !!!!!     END OF GUI     !!!!!

admin_name = values[1]
user_ID = values[2]
read_distance_path = values[3]
scene_1_path = values[4]
scene_2_path = values[5]
scene_3_path = values[6]
output_path = values[7]

read_distance_file = os.path.basename(read_distance_path) 
scene_1_file = os.path.basename(scene_1_path) 
scene_2_file = os.path.basename(scene_2_path) 
scene_3_file = os.path.basename(scene_3_path) 
	
#Test variables DELETE ME
print(admin_name)
print(user_ID)
print(read_distance_path)
print(scene_1_path)
print(scene_2_path)
print(scene_3_path)
print(output_path)

print(read_distance_file)
print(scene_1_file)
print(scene_2_file)
print(scene_3_file)

#Save the start time to record the length of the full study
full_study_start_time = time.time()
	

#Time Read Distance Scene
read_distance_start_time = time.time()
#Open read distance scene and stay until close
call(read_distance_path)
while(read_distance_file in (p.name() for p in psutil.process_iter())):
    #stay in this loop until the exe has been closed
    continue
read_distance_time = time.time() - read_distance_start_time
read_distance_time = round(read_distance_time, 2)

#Time Scene One
#Time Scene Two
#Time Scene Three


path_list = []
path_list.append(scene_1_path)
path_list.append(scene_2_path)
path_list.append(scene_3_path)

file_list = []
file_list.append(scene_1_file)
file_list.append(scene_2_file)
file_list.append(scene_3_file)
  
#List to save the run times of each program
time_list = [None] * 3

#Run the three scenes in a random order
for i in range(3):
    
    scene_start_time = None
    scene_time = None
	
    if(i < 2):
        rand_limit = 2 - i
        rand_scene_pos = random.randint(0,rand_limit)
    else:
        rand_scene_pos = 0

	#Save start time for the scene
    scene_start_time = time.time()
	
	#Open the scene
    call(path_list[rand_scene_pos])
    while(file_list[rand_scene_pos] in (p.name() for p in psutil.process_iter())):
        #stay in this loop until the exe has been closed
        continue
    
	#Save time data
    scene_time = time.time() - scene_start_time
    scene_time = round(scene_time, 2)
	
	#Fill the time array with the times associated with the proper scenes
    if(file_list[rand_scene_pos] == scene_1_file):
	    time_list[0] = scene_time
    elif(file_list[rand_scene_pos] == scene_2_file):
        time_list[1] = scene_time
    else:
        time_list[2] = scene_time
	
    if(i < 2):	
        del path_list[rand_scene_pos]
        del file_list[rand_scene_pos]




#Calculate the full study time
full_study_time = time.time() - full_study_start_time
full_study_time = round(full_study_time, 2)

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

#Create new file to store information about the researcher and times
#FIXME Change the scene 1 time, scene 2 time etc to the names of the scenes
with open(output_path + user_ID + "_main" + ".csv", mode='w', newline='') as output_file:
    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    output_writer.writerow(['Participant UserID', 'Study Admin', 'Date', 'Read Distance Time', 'Scene 1 Time', 'Scene 2 Time', 'Scene 3 Time', 'Full Study Time'])
    output_writer.writerow([user_ID, admin_name, date, read_distance_time, time_list[0], time_list[1], time_list[2], full_study_time])
	
#Remove the .exe from the path names
read_distance_file = read_distance_file[:-4]
scene_1_file = scene_1_file[:-4]
scene_2_file = scene_2_file[:-4]
scene_3_file = scene_3_file[:-4]
	
#Rename the created files with the new names
#FIX ME add a check to see if files exist 
os.rename(os.path.join(output_path, read_distance_file + '.csv'), os.path.join(output_path, user_ID + '_' + read_distance_file + '.csv'))
os.rename(os.path.join(output_path, scene_1_file + '.csv'), os.path.join(output_path, user_ID + '_' + scene_1_file + '.csv'))
os.rename(os.path.join(output_path, scene_2_file + '.csv'), os.path.join(output_path, user_ID + '_' + scene_2_file + '.csv'))
os.rename(os.path.join(output_path, scene_3_file + '.csv'), os.path.join(output_path, user_ID + '_' + scene_3_file + '.csv'))

	
	
	
	
	
	
