#Replace the paths with the proper paths
read_distance_scene = r"C:\Users\timmonse\Desktop\ReadDistanceStudy\VR Read Distance Study.exe"
foveated_scene = r"C:\Users\timmonse\Documents\Code\Python\GitInsidePy\AutomatedVRStudy\test2Ex.exe"
generator_scene = r"C:\Users\timmonse\Documents\Code\Python\GitInsidePy\AutomatedVRStudy\test3Ex.exe"

#DELETE ME just used for testing
# chrome_exe = r"C:\Users\timmonse\Documents\Code\Python\GitInsidePy\AutomatedVRStudy\ChromeTest.lnk"

# import os 
# os.startfile(chrome_exe)

from subprocess import call
call([read_distance_scene])