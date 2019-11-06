# File:          AutomatedGUI.py
# Author:        Evan Timmons
# Date:          10/17/2019
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
import shutil

sg.ChangeLookAndFeel('SystemDefault')      

selectedButton = 'o';
selectedScene = 'none'

# ------ Menu Definition ------ #      
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
			['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
			['Help', 'About...'], ]      

# ------ Column Definition ------ #      
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
		   [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
		   [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
		   [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]   
		   
def buttonR1():
    global selectedButton
    selectedButton = 'one'
    window.Element('Radius One').Update(button_color=('white', 'black'))
    window.Element('Radius Two').Update(button_color=('white', 'midnightblue'))
    window.Element('Radius Three').Update(button_color=('white', 'midnightblue'))

def buttonR2():
    global selectedButton
    selectedButton = 'two'	
    window.Element('Radius One').Update(button_color=('white', 'midnightblue'))
    window.Element('Radius Two').Update(button_color=('white', 'black'))
    window.Element('Radius Three').Update(button_color=('white', 'midnightblue'))

def buttonR3():
    global selectedButton
    selectedButton = 'three'
    window.Element('Radius One').Update(button_color=('white', 'midnightblue'))
    window.Element('Radius Two').Update(button_color=('white', 'midnightblue'))
    window.Element('Radius Three').Update(button_color=('white', 'black'))

# Lookup dictionary that maps button to function to call
func_dict = {'Radius One':buttonR1, 'Radius Two':buttonR2, 'Radius Three':buttonR3}	

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
	 sg.InputText("C:\\UserStudyMain\\ReadDistanceBuild\\ReadDistanceBuild.exe"), sg.FileBrowse()],
	 
	#FIX ME ADD NAME OF FOLDER and change the paths
	[sg.Text('Non Foveated Rendering', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\UserStudyMain\\NonFRBuild\\NonFR.exe"), sg.FileBrowse()],
	 
	[sg.Text('Radius One', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\UserStudyMain\\R1FR\\R1FR.exe"), sg.FileBrowse()],
	 
	[sg.Text('Radius Two', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\UserStudyMain\\R2FR\\R2FR.exe"), sg.FileBrowse()],
	 
	[sg.Text('Radius Three', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\UserStudyMain\\R3FR\R3FR.exe"), sg.FileBrowse()],
	 
	[sg.Text('Please choose a study to run', auto_size_text=True)],
    [sg.Button('Radius One',  key='Radius One'), sg.Button('Radius Two', key='Radius Two'), sg.Button('Radius Three', key='Radius Three')],
	 
	 [sg.Text('_'  * 80)], 
	 
    [sg.Text('Output Folder', size=(35, 1))],      
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\UserStudyMain\\Output\\"), sg.FolderBrowse()],
	 
	
	[sg.Text('_'  * 80)], 
	 
	[sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
]      

window = sg.Window('VR User Study', layout, default_element_size=(40, 1), grab_anywhere=False, default_button_element_size=(40,1)) 
window.Finalize();   

#Verify proper selections before continuing
while True:
    event, values = window.Read() 
    if event == 'Cancel':
	    sys.exit();
    elif ((event == 'Submit') and ((values[2] == "Example: U0001") or (values[1] == "Example: Evan Timmons"))):
            sg.Popup('Make sure to change the first two input fields')
    elif((event == 'Submit') and (selectedButton == 'o')):
            sg.Popup('Please select a radius')
    elif event == 'Submit':
        break;
    else:
        try:
            func_to_call = func_dict[event]   # look for a match in the function dictionary
            func_to_call()                    # if successfully found a match, call the function found
            wait(3)
        except:
            pass


sg.PopupOK("You selected Radius " + selectedButton) 

# !!!!!     END OF GUI     !!!!! !!!!!     END OF GUI     !!!!! !!!!!     END OF GUI     !!!!! !!!!!     END OF GUI     !!!!!
#Assign names to GUI inputs
admin_name = values[1]
user_ID = values[2]
read_distance_filepath = values[3]
NonFRBuild_filepath = values[4]
R1FR_filepath = values[5]
R2FR_filepath = values[6]
R3FR_filepath = values[7]

output_path = values[8]

read_distance_file = os.path.basename(read_distance_filepath) 
NonFRBuild_file = os.path.basename(NonFRBuild_filepath) 
R1FR_file = os.path.basename(R1FR_filepath) 
R2FR_file = os.path.basename(R2FR_filepath) 
R3FR_file = os.path.basename(R3FR_filepath) 

read_distance_path = read_distance_filepath.replace(read_distance_file,"")
NonFRBuild_path = NonFRBuild_filepath.replace(NonFRBuild_file,"")
R1FR_path = R1FR_filepath.replace(R1FR_file,"")
R2FR_path = R2FR_filepath.replace(R2FR_file,"")
R3FR_path = R3FR_filepath.replace(R3FR_file,"")

#Remove the .exe from the path names
read_distance_filebare = read_distance_file[:-4]
NonFRBuild_filebare = NonFRBuild_file[:-4]
R1FR_filebare = R1FR_file[:-4]
R2FR_filebare = R2FR_file[:-4]
R3FR_filebare = R3FR_file[:-4]

# Test variables DELETE ME
# print("admin_name " + admin_name)
# print(user_ID)
# print(read_distance_filepath)
# print(NonFRBuild_filepath)
# print(R1FR_filepath)
# print(R2FR_filepath)
# print(R3FR_filepath)
# print(output_path)

# print(read_distance_file)
# print(NonFRBuild_file)
# print(R1FR_file)
# print(R2FR_file)
# print(R3FR_file)

#print("read_distance_path " + read_distance_path)

#Save the start time to record the length of the full study
full_study_start_time = time.time()
	

#Time Read Distance Scene
read_distance_start_time = time.time()
#Open read distance scene and stay until close
call(read_distance_filepath)
while(read_distance_file in (p.name() for p in psutil.process_iter())):
    #stay in this loop until the exe has been closed
    continue
read_distance_time = time.time() - read_distance_start_time
read_distance_time = round(read_distance_time, 2)

#Time Scene One
#Time Scene Two
#Time Scene Three


path_list = []
path_list.append(NonFRBuild_filepath)
path_list.append(R1FR_filepath)
path_list.append(R2FR_filepath)
path_list.append(R3FR_filepath)

file_list = []
file_list.append(NonFRBuild_file)
file_list.append(R1FR_file)
file_list.append(R2FR_file)
file_list.append(R3FR_file)
  
#List to save the run times of each program
time_list = [None] * 3

scene_order = ""

#Stack for scenes to be run during this session
scene_stack = []
scene_stack.append(NonFRBuild_file)

# Assign study scene names
if(selectedButton == 'one'):
    scene_stack.append(R1FR_file)
    scene_stack.append(R1FR_file)
elif(selectedButton == 'two'):
    scene_stack.append(R2FR_file)
    scene_stack.append(R2FR_file)
elif(selectedButton == 'three'):
    scene_stack.append(R3FR_file)
    scene_stack.append(R3FR_file)

#Choose random order for scenes
random.shuffle(scene_stack)

print("PRINTING THE STACK BELOW")
print(scene_stack)

#Run until the scene stack is empty
#The stack is shuffled so the scenes will run in random order
while scene_stack:
    scene_start_time = None
    scene_time = None
	
    current_scene_file = scene_stack.pop()
    print(current_scene_file)
    if(current_scene_file == NonFRBuild_file):
        current_scene_filepath = NonFRBuild_filepath
    elif(current_scene_file == R1FR_file):
        current_scene_filepath = R1FR_filepath
    elif(current_scene_file == R2FR_file):
        current_scene_filepath = R2FR_filepath
    elif(current_scene_file == R3FR_file):
        current_scene_filepath = R3FR_filepath
	
    scene_start_time = time.time()
	
    call(current_scene_filepath)
    while(current_scene_file in (p.name() for p in psutil.process_iter())):
        #stay in this loop until the exe has been closed
        continue
    
	#Save time data
    scene_time = time.time() - scene_start_time
    scene_time = round(scene_time, 2)
	
	#Save the ordering of the scenes
    scene_order +=  current_scene_file[:-4] + ", "
	
	#Create an ordered time list that can be read to the main csv
    if((current_scene_file == R1FR_file) or (current_scene_file == R2FR_file) or (current_scene_file == R3FR_file)):
        #Set the name for the task completetion time file
        if(current_scene_file == R1FR_file):
            file_FR = open(os.path.join(R1FR_path, R1FR_filebare + '_TasksCompletionTime.txt'))
        elif(current_scene_file == R2FR_file):
            file_FR = open(os.path.join(R2FR_path, R2FR_filebare + '_TasksCompletionTime.txt'))
        elif(current_scene_file == R3FR_file):
            file_FR = open(os.path.join(R3FR_path, R3FR_filebare + '_TasksCompletionTime.txt'))
					
        if(time_list[0] is None):
            time_list[0] = scene_time
            for line in file_FR:
                FR_Realtime_1 = line
            file_FR.close()
            if(current_scene_file == R1FR_file):
                shutil.copy(os.path.join(R1FR_path, R1FR_filebare + '_TrackingData.txt'), os.path.join(output_path, user_ID + '_' + R1FR_filebare + '_TrackingData.txt'))
            elif(current_scene_file == R2FR_file):
                shutil.copy(os.path.join(R2FR_path, R2FR_filebare + '_TrackingData.txt'), os.path.join(output_path, user_ID + '_' + R2FR_filebare + '_TrackingData.txt'))
            elif(current_scene_file == R3FR_file):
                shutil.copy(os.path.join(R3FR_path, R3FR_filebare + '_TrackingData.txt'), os.path.join(output_path, user_ID + '_' + R3FR_filebare + '_TrackingData.txt'))
        else:
            time_list[1] = scene_time
            for line in file_FR:
                FR_Realtime_2 = line
            file_FR.close()
            if(current_scene_file == R1FR_file):
                shutil.copy(os.path.join(R1FR_path, R1FR_filebare + '_TrackingData.txt'), os.path.join(output_path, user_ID + '_' + R1FR_filebare + '_TrackingData_2.txt'))
            elif(current_scene_file == R2FR_file):
                shutil.copy(os.path.join(R2FR_path, R2FR_filebare + '_TrackingData.txt'), os.path.join(output_path, user_ID + '_' + R2FR_filebare + '_TrackingData_2.txt'))
            elif(current_scene_file == R3FR_file):
                shutil.copy(os.path.join(R3FR_path, R3FR_filebare + '_TrackingData.txt'), os.path.join(output_path, user_ID + '_' + R3FR_filebare + '_TrackingData_2.txt'))
    #Save the time for the NonFR file
    else:
        time_list[2] = scene_time

#Open NonFR file and save the time
file_NonFR = open(os.path.join(NonFRBuild_path, NonFRBuild_filebare + '_TasksCompletionTime.txt'))

for line in file_NonFR:
    NonFR_Realtime = line;
file_NonFR.close()

#Calculate the full study time
full_study_time = time.time() - full_study_start_time
full_study_time = round(full_study_time, 2)

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
	
#Rename the created files with the new names and move them to the output folder
#FIX ME add a check to see if files exist 
os.rename(os.path.join(read_distance_path, "ReadDistanceBuild_Data\\output\\" + read_distance_filebare + '.csv'), os.path.join(output_path, user_ID + '_' + read_distance_filebare + '.csv'))

shutil.copy(os.path.join(NonFRBuild_path, NonFRBuild_filebare + '_TrackingData.txt'), os.path.join(output_path, user_ID + '_' + NonFRBuild_filebare + '_TrackingData.txt'))

#Create new file to store information about the researcher and times
with open(output_path + user_ID + "_main" + ".csv", mode='w', newline='') as output_file:
    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    output_writer.writerow(['Participant UserID', 'Study Admin', 'Date', 'Scene Order', 'Read Distance Time', 'FR Time One', 'FR Time Two', 'NonFR Time', 'Full Study Time'])
    output_writer.writerow([user_ID, admin_name, date, 'Read Distance Scene,' + scene_order, read_distance_time, time_list[0], time_list[1], time_list[2], full_study_time])
    output_writer.writerow(['', '', '', '', '', FR_Realtime_1, FR_Realtime_2, NonFR_Realtime, ''])

	
	
	
	
	
	
