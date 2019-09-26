from subprocess import call
import random
import psutil  

#Replace the paths with the proper paths
read_distance_scene = "VR Read Distance Study.exe"
foveated_scene = "test2Ex.exe"
generator_scene = "test3Ex.exe"

folder_path = "C:\\Users\\timmonse\\Desktop\\ReadDistanceStudy\\"

read_distance_path = folder_path + read_distance_scene
foveated_path = folder_path + foveated_scene
generator_path = folder_path + generator_scene

scene_list = []
scene_list.append(read_distance_scene)
scene_list.append(foveated_scene)
scene_list.append(generator_scene)

#Randomly choose the order to open the scenes and then open them
for i in range(3):
    rand_limit = 2 - i
    rand_scene_pos = random.randint(0,rand_limit)

	#Open the scene
    call([folder_path + scene_list[rand_scene_pos]])
    while(scene_list[rand_scene_pos] in (p.name() for p in psutil.process_iter())):
        #stay in this loop until the exe has been closed
        continue
    del scene_list[rand_scene_pos]
    
    