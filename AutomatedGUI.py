import PySimpleGUI as sg      

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
	[sg.Text('UserID')],      
	[sg.InputText('Example: U0001')],
	
	#[sg.Frame(layout=[      
	#[sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],      
	#[sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],      
	# [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
	 # sg.Multiline(default_text='A second multi-line', size=(35, 3))],      
	# [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),      
	 # sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],      
	# [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],      
	# [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),      
	 # sg.Frame('Labelled Group',[[      
	 # sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),      
	 # sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),      
	 # sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),      
	 # sg.Column(column1, background_color='#F7F3EC')]])],   
	 
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
	 
	[sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
]      


window = sg.Window('VR User Study', layout, default_element_size=(40, 1), grab_anywhere=False)      

event, values = window.Read() 

#Check if want submission
if event == 'Submit':
	userID = values[1]
	read_distance_path = values[2]
	scene_1_path = values[3]
	scene_2_path = values[4]
	scene_3_path = values[5]

	
window.Close();     

sg.Popup('Title',      
		 'The results of the window.',      
		 'The button clicked was "{}"'.format(event),      
		 'The values are', values)   		 




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