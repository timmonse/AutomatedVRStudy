# File:          AutomatedGUI.py
# Author:        Evan Timmons
# Date:          10/10/2019
# ISU Email:     timmonse@iastate.edu
# Description:   This program automates the study process for the 2019 ARLAB user study


import PySimpleGUI as sg      
import csv

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
	 sg.InputText("C:\\Users\\timmonse\\Desktop\\ReadDistanceStudy\\Read Distance Study.exe"), sg.FileBrowse()],
	 
	#FIX ME ADD NAME OF FOLDER and change the paths
	[sg.Text('Supriya Study 1', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\Users\\timmonse\\Documents\\Code\\Python\\GitInsidePy\\AutomatedVRStudy\\testEx.exe"), sg.FileBrowse()],
	 
	[sg.Text('Supriya Study 2', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\Users\\timmonse\\Documents\\Code\\Python\\GitInsidePy\\AutomatedVRStudy\\test2Ex.exe"), sg.FileBrowse()],
	 
	[sg.Text('Supriya Study 3', size=(35, 1))],      
	[sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\Users\\timmonse\\Documents\\Code\\Python\\GitInsidePy\\AutomatedVRStudy\\test3Ex.exe"), sg.FileBrowse()],
	 
	 [sg.Text('_'  * 80)], 
	 
    [sg.Text('Output Folder', size=(35, 1))],      
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
	 sg.InputText("C:\\Users\\timmonse\\Desktop\\testOutput\\"), sg.FolderBrowse()],
	 
	
	[sg.Text('_'  * 80)], 
	 
	[sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
]      


window = sg.Window('VR User Study', layout, default_element_size=(40, 1), grab_anywhere=False)      

event, values = window.Read() 

#Check if want submission
if event == 'Submit':
	admin_name = values[1]
	user_ID = values[2]
	read_distance_path = values[3]
	scene_1_path = values[4]
	scene_2_path = values[5]
	scene_3_path = values[6]
	output_path = values[7]
	
	#Test variables DELETE ME
	# print(admin_name)
	# print(user_ID)
	# print(read_distance_path)
	# print(scene_1_path)
	# print(scene_2_path)
	# print(scene_3_path)
	# print(output_path)
	
	



	
  

# sg.Popup('Title',      
		 # 'The results of the window.',      
		 # 'The button clicked was "{}"'.format(event),      
		 # 'The values are', values)   		 

#window.Close()   


# !!!!!     END OF GUI     !!!!! !!!!!     END OF GUI     !!!!! !!!!!     END OF GUI     !!!!! !!!!!     END OF GUI     !!!!!

# List of all three scene paths
# scene_list = []
# scene_list.append(read_distance_scene)
# scene_list.append(foveated_scene)
# scene_list.append(generator_scene)

# #Randomly choose the order to open the scenes and then open them
# for i in range(3):
    # rand_limit = 2 - i
    # rand_scene_pos = random.randint(0,rand_limit)

	# #Open the scene
    # call([folder_path + scene_list[rand_scene_pos]])
    # while(scene_list[rand_scene_pos] in (p.name() for p in psutil.process_iter())):
        # #stay in this loop until the exe has been closed
        # continue
    # del scene_list[rand_scene_pos]
	
with open(output_path + user_ID + "_main" + ".csv", mode='w', newline='') as output_file:
    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    output_writer.writerow(['Study Admin', 'Participant UserID', 'Time 1', 'Time 2', 'Time 3', 'Time 4',])
    output_writer.writerow([admin_name, user_ID, 'FIXME', 'FIXME', 'FIXME', 'FIXME'])
	
	
	
	
	
	
